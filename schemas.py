from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

class DeviceBase(BaseModel):
    machine_id: str

class LiveData(DeviceBase):
    # Core fields (Keep these required - no default value)
    temperature: float
    target_temperature: float
    
    # Static data
    type: str = "live_data"
    machine_name: Optional[str] = None
    serial_number: Optional[str] = None
    firmware_version: Optional[str] = None
    hardware_version: Optional[str] = None
    
    # Make everything else optional by adding defaults!
    timestamp: Optional[datetime] = None
    uptime_sec: int = 0
    
    mode: str = "heating"
    process: str = "pasteurization"
    process_step: int = 1
    process_running: bool = True
    process_paused: bool = False
    process_completed: bool = False
    emergency_stop: bool = False
    batch_number: int = 0
    recipe_name: str = "Default"
    
    holding_time_sec: int = 0
    holding_elapsed_sec: int = 0
    holding_remaining_sec: int = 0
    cooling_target_temperature: float = 0.0
    
    heater_enabled: bool = False
    heater_status: str = "OFF"
    heater_on_temperature: float = 0.0
    heater_off_temperature: float = 0.0
    
    cooler_enabled: bool = False
    cooler_status: str = "OFF"
    cooler_on_temperature: float = 0.0
    cooler_off_temperature: float = 0.0
    
    stirrer_enabled: bool = False
    stirrer_status: str = "OFF"
    
    voltage: float = 0.0
    current: float = 0.0
    power: float = 0.0
    energy: float = 0.0
    frequency: float = 0.0
    power_factor: float = 0.0
    
    heater_runtime_sec: int = 0
    cooler_runtime_sec: int = 0
    stirrer_runtime_sec: int = 0
    
    wifi_connected: bool = True
    wifi_ssid: Optional[str] = None
    wifi_rssi: Optional[int] = None
    server_connected: Optional[bool] = None
    last_sync_sec: Optional[int] = None
    alarm: bool = False
    alarm_code: Optional[int] = None
    alarm_message: Optional[str] = None
    device_status: str = "ACTIVE"

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
