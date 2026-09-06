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
# The dashboard calls this to queue a command.
# The command is stored as PENDING and the ESP32
# picks it up on its next HTTP telemetry POST.
# ==========================================
@router.post("/device/{machine_id}/commands", response_model=schemas.CommandResponseSchema)
async def create_command(machine_id: str, payload: schemas.CommandCreateSchema, db: Session = Depends(get_db)):
    # 1. Generate a globally unique command ID
    cmd_id = f"CMD_{uuid.uuid4().hex[:8].upper()}"

    # 2. Save to database as PENDING
    new_command = models.Command(
        command_id=cmd_id,
        machine_id=machine_id,
        command=payload.command,
        parameters=payload.parameters or {},
        status="PENDING"
    )
    db.add(new_command)
    db.commit()
    db.refresh(new_command)

    print(f"📥 Command queued: {cmd_id} ({payload.command}) for machine {machine_id}")

    # 3. Return the tracking info to the React dashboard
    return {
        "command_id": new_command.command_id,
        "machine_id": new_command.machine_id,
        "command": new_command.command,
        "status": new_command.status,
        "created_at": new_command.created_at
    }

# ==========================================
# 2. WEBSOCKET: Dashboard real-time updates
# The React dashboard connects here to receive
# live state pushes (optional enhancement).
# ==========================================
@router.websocket("/ws/dashboard")
async def websocket_dashboard_endpoint(websocket: WebSocket):
    """The real-time connection for the React Dashboard."""
    await manager.connect_dashboard(websocket)
    try:
        while True:
            # The dashboard mostly listens, keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect_dashboard(websocket)
