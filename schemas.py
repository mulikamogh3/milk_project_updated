from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

class DeviceBase(BaseModel):
    machine_id: str

class LiveData(BaseModel):
    machine_id: str
    online: bool = True
    mode: str = "AUTO"
    process_state: str = "HEATING"
    
    temperature: float = 0.0
    target_temperature: float = 0.0
    cooling_temperature: float = 0.0
    max_temperature: float = 0.0
    
    holding_time_sec: int = 0
    holding_elapsed_sec: int = 0
    holding_remaining_sec: int = 0
    
    heater: bool = False
    stirrer: bool = False
    cooler: bool = False
    
    running: bool = False
    emergency: bool = False
    fault: bool = False
    fault_code: Optional[str] = None
    
    voltage: float = 0.0
    current: float = 0.0
    power: float = 0.0
    energy: float = 0.0
    frequency: float = 0.0
    power_factor: float = 0.0
    
    last_command: Optional[str] = None
    last_command_id: Optional[str] = None
    command_status: Optional[str] = None

class ManualCommand(DeviceBase):
    mode: str = Field(default="MANUAL")
    command: str
    heater_state: bool
    cooler_state: bool
    stirrer_state: bool

class AutoCommand(DeviceBase):
    mode: str = Field(default="AUTO")
    command: str
    recipe_name: str
    target_temperature: float
    holding_time_sec: int

class StartPasteurizationPayload(DeviceBase):
    command: str = Field(default="START_PASTEURIZATION")
    method: str = Field(..., description="LTLT, HTST, or CUSTOM")
    target_temperature: float = Field(..., ge=0.0, le=100.0)
    holding_time_sec: int = Field(..., ge=0)
    cooling_temperature: float = Field(..., ge=0.0, le=100.0)
    max_temperature: float = Field(..., ge=0.0, le=120.0)

class RecipeParameters(BaseModel):
    target_temperature: float = Field(..., ge=0, le=100)
    cool_temperature: float = Field(..., ge=0, le=50)
    hold_time_minutes: int = Field(..., ge=0, le=60)
    hysteresis: float = Field(default=1.0)

class CommandCreateSchema(BaseModel):
    command: str # e.g., AUTO_START, SET_RECIPE
    parameters: Optional[Dict[str, Any]] = {}

class CommandResponseSchema(BaseModel):
    command_id: str
    machine_id: str
    command: str
    status: str
    created_at: datetime

class CommandResultSchema(BaseModel):
    machine_id: str
    command_id: str
    command: str
    status: str # EXECUTED, REJECTED
    process_state: Optional[str] = None
    auto_running: Optional[bool] = None
    reason: Optional[str] = None
