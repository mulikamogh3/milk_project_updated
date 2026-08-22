from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, ForeignKey
from database import Base
import datetime

class SensorData(Base):
    __tablename__ = "sensor_data"

    # 1. Base Info
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    uptime_sec = Column(Integer)

    # 2. Process Info
    mode = Column(String)
    process = Column(String)
    process_step = Column(Integer)
    process_running = Column(Boolean)
    process_paused = Column(Boolean)
    process_completed = Column(Boolean)
    emergency_stop = Column(Boolean)
    batch_number = Column(Integer)
    recipe_name = Column(String)

    # 3. Thermal Data
    temperature = Column(Float)
    target_temperature = Column(Float)
    holding_time_sec = Column(Integer)
    holding_elapsed_sec = Column(Integer)
    holding_remaining_sec = Column(Integer)
    cooling_target_temperature = Column(Float)

    # 4. Hardware Relays
    heater_enabled = Column(Boolean)
    heater_status = Column(String) # ESP32 sends "ON"/"OFF" now instead of True/False
    cooler_enabled = Column(Boolean)
    cooler_status = Column(String)
    stirrer_enabled = Column(Boolean)
    stirrer_status = Column(String)

    # 5. Electrical Data
    voltage = Column(Float)
    current = Column(Float)
    power = Column(Float)
    energy = Column(Float)
    frequency = Column(Float)
    power_factor = Column(Float)

    # 6. Runtimes & System
    heater_runtime_sec = Column(Integer)
    cooler_runtime_sec = Column(Integer)
    stirrer_runtime_sec = Column(Integer)
    wifi_connected = Column(Boolean)
    alarm = Column(Boolean)
    device_status = Column(String)

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, unique=True, index=True)
    name = Column(String, default="Pasteurizer Node")
    online = Column(Boolean, default=False)
    last_seen = Column(DateTime, default=datetime.datetime.utcnow)

    # State
    mode = Column(String, default="MANUAL")
    process_state = Column(String, default="IDLE")
    auto_running = Column(Boolean, default=False)
    emergency_stop = Column(Boolean, default=False)

    # Recipe & Physics
    temperature = Column(Float, default=0.0)
    target_temperature = Column(Float, default=72.0)
    cool_temperature = Column(Float, default=35.0)
    hysteresis = Column(Float, default=1.0)
    hold_time_minutes = Column(Integer, default=15)

    # Hardware Relays
    heater = Column(Boolean, default=False)
    stirrer = Column(Boolean, default=False)
    cooler = Column(Boolean, default=False)

    # Electrical
    voltage = Column(Float, default=0.0)
    current = Column(Float, default=0.0)
    power = Column(Float, default=0.0)
    energy = Column(Float, default=0.0)
    frequency = Column(Float, default=0.0)
    power_factor = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    command_id = Column(String, unique=True, index=True) # e.g., CMD_10025
    machine_id = Column(String, index=True)
    command = Column(String) # e.g., AUTO_START, SET_RECIPE
    parameters = Column(JSON, default={})
    status = Column(String, default="CREATED") # CREATED, PENDING, SENT, EXECUTED, FAILED
    error_reason = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)
    received_at = Column(DateTime, nullable=True)
    executed_at = Column(DateTime, nullable=True)
