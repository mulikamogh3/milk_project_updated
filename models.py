from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, ForeignKey
from database import Base
import datetime

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    online = Column(Boolean, default=True)
    mode = Column(String)
    process_state = Column(String)
    
    temperature = Column(Float)
    target_temperature = Column(Float)
    cooling_temperature = Column(Float)
    
    holding_time_sec = Column(Integer)
    holding_elapsed_sec = Column(Integer)
    holding_remaining_sec = Column(Integer)
    
    max_temperature = Column(Float)
    
    heater = Column(Boolean)
    stirrer = Column(Boolean)
    cooler = Column(Boolean)
    
    running = Column(Boolean)
    emergency = Column(Boolean)
    fault = Column(Boolean)
    fault_code = Column(String, nullable=True)
    
    voltage = Column(Float)
    current = Column(Float)
    power = Column(Float)
    energy = Column(Float)
    frequency = Column(Float)
    power_factor = Column(Float)
    
    last_command = Column(String, nullable=True)
    last_command_id = Column(String, nullable=True)
    command_status = Column(String, nullable=True)

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
    method = Column(String, nullable=True) # LTLT, HTST, CUSTOM
    parameters = Column(JSON, default={})
    status = Column(String, default="CREATED") # CREATED, PENDING, SENT, EXECUTED, FAILED
    error_reason = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)
    received_at = Column(DateTime, nullable=True)
    executed_at = Column(DateTime, nullable=True)

class PasteurizationBatch(Base):
    __tablename__ = "pasteurization_batches"

    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(String, unique=True, index=True)
    machine_id = Column(String, index=True)
    method = Column(String) # LTLT, HTST, CUSTOM
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    final_heating_temp = Column(Float, nullable=True)
    final_cooling_temp = Column(Float, nullable=True)
    status = Column(String, default="IN_PROGRESS") # IN_PROGRESS, COMPLETED, FAILED
