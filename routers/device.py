from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid
import schemas
import models
from database import get_db
from services.industrial_logic import calculate_heater_decision, check_industrial_safety_override

router = APIRouter(
    prefix="/device",
    tags=["IoT Device Endpoints"]
)

# ==========================================
# 1. UI Command Intake (React -> Backend)
# ==========================================
@router.post("/command")
def receive_ui_command(payload: schemas.StartPasteurizationPayload, db: Session = Depends(get_db)):
    date_str = datetime.utcnow().strftime("%Y%m%d")
    unique_suffix = str(uuid.uuid4().hex)[:4].upper()
    cmd_id = f"CMD_{date_str}_{unique_suffix}"
    
    params = {
        "target_temperature": payload.target_temperature,
        "holding_time_sec": payload.holding_time_sec,
        "cooling_temperature": payload.cooling_temperature,
        "max_temperature": payload.max_temperature
    }
    
    new_cmd = models.Command(
        command_id=cmd_id,
        machine_id=payload.machine_id,
        command=payload.command,
        method=payload.method,
        parameters=params,
        status="PENDING",
        created_at=datetime.utcnow()
    )
    
    db.add(new_cmd)
    db.commit()
    
    print(f"📥 Command queued: {cmd_id} ({payload.command} - {payload.method}) for machine {payload.machine_id}")
    
    return {
        "status": "success",
        "message": "Command queued successfully",
        "command_id": cmd_id
    }

# ==========================================
# 1. ESP32 Telemetry Ingestion + Command Delivery
# This is the MAIN entry point for the ESP32.
# It does 3 things:
#   (a) Saves the telemetry snapshot to the database
#   (b) Checks if the ESP32 is acknowledging a past command and updates its status
#   (c) Fetches any PENDING command for this machine and sends it back as the response
# ==========================================
@router.post("/data")
def receive_sensor_data(payload: schemas.LiveData, db: Session = Depends(get_db)):

    # --- (a) Save full telemetry snapshot ---
    data_dict = payload.model_dump()
    data_dict['timestamp'] = datetime.utcnow()
    new_data = models.SensorData(**data_dict)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    print(f"✅ Telemetry saved for {payload.machine_id}: Temp={payload.temperature}°C, State={payload.process_state}")

    # --- (b) Process command acknowledgement from ESP32 ---
    # The ESP32 includes last_command_id + command_status in every telemetry packet.
    # If it has executed a command, we update the Command ledger here.
    if payload.last_command_id and payload.command_status in ["EXECUTED", "REJECTED", "FAILED"]:
        cmd_record = db.query(models.Command).filter(
            models.Command.command_id == payload.last_command_id,
            # Only update if not already finalized to avoid double-writes
            models.Command.status.notin_(["EXECUTED", "REJECTED", "FAILED"])
        ).first()
        if cmd_record:
            cmd_record.status = payload.command_status
            cmd_record.executed_at = datetime.utcnow()
            db.commit()
            print(f"📋 Command {payload.last_command_id} acknowledged by ESP32 as: {payload.command_status}")

    # --- (c) Check for a pending command to deliver to this ESP32 ---
    # First, expire any PENDING commands older than 60s that were never picked up
    # (e.g. leftover from server restarts or test runs)
    db.query(models.Command).filter(
        models.Command.machine_id == payload.machine_id,
        models.Command.status == "PENDING",
        models.Command.created_at < (datetime.utcnow() - timedelta(seconds=60))
    ).update({"status": "FAILED", "error_reason": "Expired: not delivered within 60s"})
    db.commit()

    pending_command = db.query(models.Command).filter(
        models.Command.machine_id == payload.machine_id,
        models.Command.status == "PENDING"
    ).order_by(models.Command.created_at.asc()).first()

    if pending_command:
        # Mark it as SENT so we don't re-deliver it on the next poll
        pending_command.status = "SENT"
        pending_command.sent_at = datetime.utcnow()
        db.commit()
        print(f"📤 Dispatching command {pending_command.command_id} ({pending_command.command}) to {payload.machine_id}")

        # Build the command packet the ESP32 expects
        cmd_packet = {
            "command_id": pending_command.command_id,
            "action": pending_command.command,   # e.g. "START_PASTEURIZATION"
            "method": pending_command.method,
        }
        # Merge any extra recipe parameters (target_temperature, hold_time, etc.)
        if pending_command.parameters:
            cmd_packet.update(pending_command.parameters)

        return {
            "status": "success",
            "message": "Telemetry stored. Command dispatched.",
            "command": cmd_packet
        }

    # --- Run safety check for heater decision (no pending command path) ---
    safety_action = check_industrial_safety_override({
        "temperature": payload.temperature,
        "voltage": payload.voltage,
        "power": payload.power
    })
    if safety_action is not None:
        return {
            "status": "safety_override_active",
            "command": safety_action
        }

    # Normal AI heater decision (no commands, no safety issue)
    normal_action = calculate_heater_decision(
        temperature=payload.temperature,
        target_temperature=payload.target_temperature
    )

    return {
        "status": "success",
        "message": "Data safely stored in GoBioAI database",
        "command": None  # No pending command for ESP32
    }

# ==========================================
# 2. Live Data API (Dashboard reads from here)
# ==========================================
@router.get("/live")
def get_live_data(db: Session = Depends(get_db)):
    latest_data = db.query(models.SensorData).order_by(models.SensorData.id.desc()).first()

    if not latest_data:
        return {}

    live_dict = {column.name: getattr(latest_data, column.name) for column in latest_data.__table__.columns}
    live_dict.pop("id", None)

    # Convert datetime to ISO string so React can display it
    if "timestamp" in live_dict and live_dict["timestamp"]:
        live_dict["timestamp"] = live_dict["timestamp"].isoformat()

    # Inject AI Heater Decision Engine data for the dashboard
    temperature = live_dict.get("temperature", 0.0)
    target_temperature = live_dict.get("target_temperature", 0.0)
    live_dict["heater_decision"] = calculate_heater_decision(temperature, target_temperature)

    # Inject the latest command status so the dashboard knows if a command is in-flight
    latest_command = db.query(models.Command).filter(
        models.Command.machine_id == latest_data.machine_id
    ).order_by(models.Command.created_at.desc()).first()

    if latest_command:
        live_dict["active_command"] = {
            "command_id": latest_command.command_id,
            "command": latest_command.command,
            "status": latest_command.status,
        }
    else:
        live_dict["active_command"] = None

    return live_dict

# ==========================================
# 3. History API (for Analytics Charts)
# ==========================================
@router.get("/history")
def get_historical_data(limit: int = 50, db: Session = Depends(get_db)):
    records = db.query(models.SensorData).order_by(models.SensorData.id.desc()).limit(limit).all()

    if not records:
        return []

    records.reverse()

    history_data = []
    for r in records:
        history_data.append({
            "time": r.timestamp.strftime("%H:%M:%S") if r.timestamp else "00:00:00",
            "temperature": round(r.temperature or 0.0, 2),
            "target": round(r.target_temperature or 0.0, 2),
            "power": round(r.power or 0.0, 2)
        })

    return history_data
