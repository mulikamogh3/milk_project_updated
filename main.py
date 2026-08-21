from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  # <-- We are importing uvicorn directly now
from database import engine
import models
from routers import device
from routers import prediction
from pydantic import BaseModel

# Import your newly created logic engine!
from services.industrial_logic import check_industrial_safety_override, calculate_heater_decision

class SensorPayload(BaseModel):
    temperature: float
    voltage: float
    power: float
    target_temperature: float = 72.0

# Safely create tables during startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    print("✅ PostgreSQL GoBioAI Vault connected and tables verified.")
    yield

app = FastAPI(title="Milk Pasteurization IoT Backend", lifespan=lifespan)

# CORS Middleware (The Bridge)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173","https://gobio-platform-cloud-numm.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Add Request Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("========================================")
    print("METHOD :", request.method)
    print("URL    :", request.url)
    print("HEADERS:", dict(request.headers))
    
    response = await call_next(request)
    
    print("STATUS :", response.status_code)
    print("========================================")
    return response

# 2. Add Test Health Check Endpoint
@app.get("/ping")
def ping():
    return {"status": "OK"}

@app.post("/device/data")
def receive_device_data(payload: SensorPayload):
    # Step 1: Save data to PostgreSQL here...
    
    # Step 2: Run the Industrial Safety Check first!
    # Passing a dict because check_industrial_safety_override expects a dictionary
    safety_action = check_industrial_safety_override({
        "temperature": payload.temperature,
        "voltage": payload.voltage,
        "power": payload.power
    })
    
    override_needed = safety_action is not None
    
    if override_needed:
        # Instantly return the emergency shutoff command to the ESP32
        return {
            "status": "safety_override_active",
            "command": safety_action 
        }

    # Step 3: If safe, calculate the normal heating/cooling decision
    normal_action = calculate_heater_decision(
        temperature=payload.temperature,
        target_temperature=payload.target_temperature
    )

    # Step 4: Send the calculated instructions back to the hardware
    return {
        "status": "success",
        "command": normal_action
    }

app.include_router(device.router)
app.include_router(prediction.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Milk Pasteurization IoT Backend API"}
