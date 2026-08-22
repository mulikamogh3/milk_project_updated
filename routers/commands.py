from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
import models, schemas
from database import get_db, SessionLocal
from services.websocket_manager import manager

# Create the router
router = APIRouter(tags=["Machine Commands & WebSockets"])

# ==========================================
# 1. DASHBOARD -> BACKEND (Create Command)
# ==========================================
@router.post("/device/{machine_id}/commands", response_model=schemas.CommandResponseSchema)
async def create_command(machine_id: str, payload: schemas.CommandCreateSchema, db: Session = Depends(get_db)):
    # 1. Generate a globally unique command ID
    cmd_id = f"CMD_{uuid.uuid4().hex[:8].upper()}"
    
    # 2. Save to database as PENDING (Dashboard -> Cloud)
    new_command = models.Command(
        command_id=cmd_id,
        machine_id=machine_id,
        command=payload.command,
        parameters=payload.parameters,
        status="PENDING"
    )
    db.add(new_command)
    db.commit()
    db.refresh(new_command)
    
    # 3. Attempt to push to ESP32 immediately via WebSocket
    ws_payload = {
        "type": "COMMAND",
        "command_id": cmd_id,
        "machine_id": machine_id,
        "command": payload.command,
        "parameters": payload.parameters
    }
    
    # If the ESP32 is online, this sends the command and updates status to SENT
    sent = await manager.send_to_machine(machine_id, ws_payload)
    if sent:
        new_command.status = "SENT"
        new_command.sent_at = datetime.utcnow()
        db.commit()
    
    # 4. Return the tracking ID to the React dashboard
    return {
        "command_id": new_command.command_id,
        "machine_id": new_command.machine_id,
        "command": new_command.command,
        "status": new_command.status,
        "created_at": new_command.created_at
    }

# ==========================================
# 2. ESP32 -> BACKEND (HTTP Fallback Ack)
# ==========================================
@router.post("/device/command-result")
async def receive_command_result(payload: schemas.CommandResultSchema, db: Session = Depends(get_db)):
    # 1. Find the command in the ledger
    command_record = db.query(models.Command).filter(models.Command.command_id == payload.command_id).first()
    if not command_record:
        raise HTTPException(status_code=404, detail="Command not found")
        
    # 2. Duplicate Execution Protection
    if command_record.status in ["EXECUTED", "REJECTED", "FAILED", "ALREADY_EXECUTED"]:
        return {"status": "ALREADY_EXECUTED", "command_id": payload.command_id}
        
    # 3. Mark as Executed
    command_record.status = payload.status
    command_record.executed_at = datetime.utcnow()
    command_record.error_reason = payload.reason
    db.commit()
    
    # 4. Broadcast this confirmation to the React Dashboard immediately
    await manager.broadcast_machine_state({
        "type": "COMMAND_RESULT",
        "command_id": payload.command_id,
        "status": payload.status,
        "process_state": payload.process_state
    })
        
    return {"status": "success", "message": "Command execution logged successfully."}

# ==========================================
# 3. WEBSOCKET ROUTES
# ==========================================
@router.websocket("/device/ws/{machine_id}")
async def websocket_machine_endpoint(websocket: WebSocket, machine_id: str):
    """The real-time connection for the ESP32 Hardware."""
    await manager.connect_machine(machine_id, websocket)
    try:
        while True:
            # Listen for live acknowledgements from the ESP32
            data = await websocket.receive_json()
            if data.get("type") == "COMMAND_RESULT":
                # Update the database via an isolated session
                db = SessionLocal()
                try:
                    cmd = db.query(models.Command).filter(models.Command.command_id == data.get("command_id")).first()
                    if cmd and cmd.status not in ["EXECUTED", "REJECTED"]:
                        cmd.status = data.get("status")
                        cmd.executed_at = datetime.utcnow()
                        db.commit()
                        # Forward the confirmation to the dashboard UI
                        await manager.broadcast_machine_state(data)
                finally:
                    db.close()
    except WebSocketDisconnect:
        manager.disconnect_machine(machine_id)

@router.websocket("/ws/dashboard")
async def websocket_dashboard_endpoint(websocket: WebSocket):
    """The real-time connection for the React Dashboard."""
    await manager.connect_dashboard(websocket)
    try:
        while True:
            # The dashboard mostly listens, but we keep the connection open
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect_dashboard(websocket)
