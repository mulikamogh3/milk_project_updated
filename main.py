from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  # <-- We are importing uvicorn directly now
from database import engine
import models
from routers import device
from routers import prediction

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


app.include_router(device.router)
app.include_router(prediction.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Milk Pasteurization IoT Backend API"}
