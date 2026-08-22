# Project Structure: milk project_updated

```text
milk project_updated/
    .gitignore
    database.py
    error_log.txt
    main.py
    models.py
    README.md
    requirements.txt
    schemas.py
    train_pipeline.py
    gobioai-dashboard/
        .gitignore
        .oxlintrc.json
        index.html
        package.json
        postcss.config.js
        README.md
        tailwind.config.js
        vite.config.js
        public/
            favicon.svg
            icons.svg
        src/
            App.css
            App.jsx
            index.css
            main.jsx
            assets/
                hero.png
                react.svg
                vite.svg
            components/
                AnalyticsView.jsx
                Layout.jsx
                LiveDashboard.jsx
    machine_learning/
        feature_engineering.py
        predict.py
        preprocessing.py
        train_models.py
        __init__.py
        models/
            energy_model.pkl
            fault_model.pkl
            heating_model.pkl
    routers/
        device.py
        prediction.py
        __init__.py
    services/
        industrial_logic.py
        __init__.py
```

# File Contents

## database.py

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Fetch the secure database URL
# If the variable isn't found, it will prevent accidental connection to a default database
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is missing. Check your .env file.")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## error_log.txt

*Could not read file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte*

## main.py

```python
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

```

## models.py

```python
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
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

```

## README.md

```markdown
"# milk_project_updated" 

```

## requirements.txt

*Could not read file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte*

## schemas.py

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

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

```

## train_pipeline.py

```python
import random
from datetime import datetime, timedelta
from database import SessionLocal
import models
from machine_learning.preprocessing import preprocess_telemetry
from machine_learning.feature_engineering import generate_features
from machine_learning.train_models import PasteurizationModelTrainer

def run_training_pipeline():
    db = SessionLocal()
    
    # 1. Database Check & Synthetic Data Injection
    record_count = db.query(models.SensorData).count()
    if record_count < 100:
        print(f"\n[Warning] Only {record_count} rows found. Injecting 500 simulated historical records...")
        base_time = datetime.utcnow() - timedelta(days=7)
        for i in range(500):
            # Simulating a realistic thermal heating curve
            temp = 25.0 + (i % 100) * 0.5 
            new_record = models.SensorData(
                machine_id="MP001",
                timestamp=base_time + timedelta(minutes=i),
                mode="AUTO",
                process="HEATING" if temp < 72 else "HOLDING",
                temperature=temp + random.uniform(-1.0, 1.0), # Add thermal noise
                target_temperature=75.0,
                voltage=230.0 + random.uniform(-5.0, 5.0),
                power=2.5 + random.uniform(-0.2, 0.2),
                heater_status=True if temp < 75 else False,
                wifi_connected=True
            )
            db.add(new_record)
        db.commit()
        print("[Success] Simulated historical data injected into PostgreSQL.")

    # 2. Extract Data for ML
    print("\n[Extraction] Extracting historical SensorData from PostgreSQL...")
    records = db.query(models.SensorData).all()
    
    # Convert SQLAlchemy ORM objects to a list of standard dictionaries
    raw_data = []
    for r in records:
        row_dict = {column.name: getattr(r, column.name) for column in r.__table__.columns}
        raw_data.append(row_dict)
        
    db.close()

    # 3. Run the Preprocessing & Engineering Pipeline
    print("\n[Pipeline] Pushing data through ML Pipeline...")
    df_clean = preprocess_telemetry(raw_data)
    df_features = generate_features(df_clean)

    # 4. Train the Models
    print("\n[Training] Initializing Random Forest & Isolation Forest Training...")
    trainer = PasteurizationModelTrainer(df_features)
    
    # We will train a Regressor to predict Power Consumption (Energy Optimization)
    if 'power' in df_features.columns:
        trainer.train_numerical('power', 'energy_model.pkl')
        
    # We will train a Classifier to predict Heater Status (Control Systems)
    # Using 'heater_status' which was converted to 1/0 during preprocessing
    if 'heater_status' in df_features.columns:
        trainer.train_categorical('heater_status', 'heating_model.pkl')
        
    # We will train an Isolation Forest to detect sensor anomalies (Fault Detection)
    trainer.train_anomaly_detection('fault_model.pkl')
    
    print("\n[Complete] Pipeline Execution Complete!")

if __name__ == "__main__":
    run_training_pipeline()

```

## gobioai-dashboard\.oxlintrc.json

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "oxc"],
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}

```

## gobioai-dashboard\index.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>gobioai-dashboard</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

```

## gobioai-dashboard\package.json

```json
{
  "name": "gobioai-dashboard",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "oxlint",
    "preview": "vite preview"
  },
  "dependencies": {
    "@tailwindcss/postcss": "^4.3.2",
    "autoprefixer": "^10.5.2",
    "axios": "^1.18.1",
    "lucide-react": "^1.24.0",
    "postcss": "^8.5.16",
    "react": "^19.2.7",
    "react-dom": "^19.2.7",
    "react-router-dom": "^7.18.1",
    "recharts": "^3.9.2",
    "tailwindcss": "^4.3.2"
  },
  "devDependencies": {
    "@types/react": "^19.2.17",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.3",
    "oxlint": "^1.71.0",
    "vite": "^8.1.1"
  }
}

```

## gobioai-dashboard\postcss.config.js

```js
export default {
  plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {},
  },
}

```

## gobioai-dashboard\README.md

```markdown
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.

```

## gobioai-dashboard\tailwind.config.js

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

## gobioai-dashboard\vite.config.js

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

## gobioai-dashboard\src\App.css

```css
.counter {
  font-size: 16px;
  padding: 5px 10px;
  border-radius: 5px;
  color: var(--accent);
  background: var(--accent-bg);
  border: 2px solid transparent;
  transition: border-color 0.3s;
  margin-bottom: 24px;

  &:hover {
    border-color: var(--accent-border);
  }
  &:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }
}

.hero {
  position: relative;

  .base,
  .framework,
  .vite {
    inset-inline: 0;
    margin: 0 auto;
  }

  .base {
    width: 170px;
    position: relative;
    z-index: 0;
  }

  .framework,
  .vite {
    position: absolute;
  }

  .framework {
    z-index: 1;
    top: 34px;
    height: 28px;
    transform: perspective(2000px) rotateZ(300deg) rotateX(44deg) rotateY(39deg)
      scale(1.4);
  }

  .vite {
    z-index: 0;
    top: 107px;
    height: 26px;
    width: auto;
    transform: perspective(2000px) rotateZ(300deg) rotateX(40deg) rotateY(39deg)
      scale(0.8);
  }
}

#center {
  display: flex;
  flex-direction: column;
  gap: 25px;
  place-content: center;
  place-items: center;
  flex-grow: 1;

  @media (max-width: 1024px) {
    padding: 32px 20px 24px;
    gap: 18px;
  }
}

#next-steps {
  display: flex;
  border-top: 1px solid var(--border);
  text-align: left;

  & > div {
    flex: 1 1 0;
    padding: 32px;
    @media (max-width: 1024px) {
      padding: 24px 20px;
    }
  }

  .icon {
    margin-bottom: 16px;
    width: 22px;
    height: 22px;
  }

  @media (max-width: 1024px) {
    flex-direction: column;
    text-align: center;
  }
}

#docs {
  border-right: 1px solid var(--border);

  @media (max-width: 1024px) {
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
}

#next-steps ul {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 8px;
  margin: 32px 0 0;

  .logo {
    height: 18px;
  }

  a {
    color: var(--text-h);
    font-size: 16px;
    border-radius: 6px;
    background: var(--social-bg);
    display: flex;
    padding: 6px 12px;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    transition: box-shadow 0.3s;

    &:hover {
      box-shadow: var(--shadow);
    }
    .button-icon {
      height: 18px;
      width: 18px;
    }
  }

  @media (max-width: 1024px) {
    margin-top: 20px;
    flex-wrap: wrap;
    justify-content: center;

    li {
      flex: 1 1 calc(50% - 8px);
    }

    a {
      width: 100%;
      justify-content: center;
      box-sizing: border-box;
    }
  }
}

#spacer {
  height: 88px;
  border-top: 1px solid var(--border);
  @media (max-width: 1024px) {
    height: 48px;
  }
}

.ticks {
  position: relative;
  width: 100%;

  &::before,
  &::after {
    content: '';
    position: absolute;
    top: -4.5px;
    border: 5px solid transparent;
  }

  &::before {
    left: 0;
    border-left-color: var(--border);
  }
  &::after {
    right: 0;
    border-right-color: var(--border);
  }
}

```

## gobioai-dashboard\src\App.jsx

```javascript
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import LiveDashboard from './components/LiveDashboard';
import AnalyticsView from './components/AnalyticsView';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* The Layout acts as the shell (Sidebar/Navbar) */}
        <Route path="/" element={<Layout />}>
          {/* Default page is the Live Dashboard */}
          <Route index element={<LiveDashboard />} />
          {/* Analytics page */}
          <Route path="analytics" element={<AnalyticsView />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

```

## gobioai-dashboard\src\index.css

```css
@import "tailwindcss";

```

## gobioai-dashboard\src\main.jsx

```javascript
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

```

## gobioai-dashboard\src\components\AnalyticsView.jsx

```javascript
import { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  LineChart, Line, AreaChart, Area, XAxis, YAxis, 
  CartesianGrid, Tooltip, Legend, ResponsiveContainer 
} from 'recharts';
import { Activity, Zap } from 'lucide-react';

export default function AnalyticsView() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        // Fetch the last 50 data points from the new endpoint
        const response = await axios.get('https://gobio-platform-cloud-h59g.onrender.com/device/history');
        setHistory(response.data);
        setError(false);
      } catch (err) {
        console.error("Failed to fetch history:", err);
        setError(true);
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
    // Refresh the charts every 5 seconds to show new data flowing in
    const interval = setInterval(fetchHistory, 5000);
    return () => clearInterval(interval);
  }, []);

  if (error) return <div className="p-8 text-red-500 font-bold">Failed to load analytics database.</div>;
  if (loading) return <div className="p-8 text-blue-400 font-bold animate-pulse">Crunching historical data...</div>;

  return (
    <div className="max-w-6xl mx-auto flex flex-col gap-6 animate-in fade-in duration-500 pb-10">
      
      {/* Header */}
      <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50">
        <h1 className="text-3xl font-bold text-white mb-2">Historical Analytics</h1>
        <p className="text-slate-400 font-medium">Live visualization of the Pasteurizer's thermal and electrical telemetry.</p>
      </div>

      {/* Chart 1: Thermal Curve */}
      <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50">
        <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-2">
          <Activity className="w-6 h-6 text-red-400" />
          Thermal Pasteurization Curve
        </h2>
        <div className="h-[350px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={history} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
              <XAxis dataKey="time" stroke="#94a3b8" fontSize={12} tickMargin={10} />
              <YAxis stroke="#94a3b8" fontSize={12} domain={['auto', 'auto']} tickFormatter={(value) => `${value}°`} />
              <Tooltip 
                contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', color: '#fff' }}
                itemStyle={{ fontWeight: 'bold' }}
              />
              <Legend verticalAlign="top" height={36} iconType="circle" />
              <Line 
                type="monotone" 
                name="Actual Temp (°C)" 
                dataKey="temperature" 
                stroke="#ef4444" 
                strokeWidth={3}
                dot={false}
                activeDot={{ r: 6, fill: '#ef4444', stroke: '#0f172a', strokeWidth: 2 }}
              />
              <Line 
                type="monotone" 
                name="Target Temp (°C)" 
                dataKey="target" 
                stroke="#64748b" 
                strokeWidth={2} 
                strokeDasharray="5 5"
                dot={false}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Chart 2: Energy Consumption */}
      <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50">
        <h2 className="text-xl font-bold text-white mb-6 flex items-center gap-2">
          <Zap className="w-6 h-6 text-yellow-400" />
          Power Draw & Efficiency
        </h2>
        <div className="h-[250px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={history} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
              <defs>
                <linearGradient id="colorPower" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#eab308" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="#eab308" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
              <XAxis dataKey="time" stroke="#94a3b8" fontSize={12} tickMargin={10} />
              <YAxis stroke="#94a3b8" fontSize={12} tickFormatter={(value) => `${value} W`} />
              <Tooltip 
                contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', color: '#fff' }}
              />
              <Area 
                type="stepAfter" 
                name="Power (Watts)" 
                dataKey="power" 
                stroke="#eab308" 
                strokeWidth={2}
                fillOpacity={1} 
                fill="url(#colorPower)" 
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

    </div>
  );
}

```

## gobioai-dashboard\src\components\Layout.jsx

```javascript
import { Outlet, Link, useLocation } from 'react-router-dom';
import { Activity, BarChart2, Droplet } from 'lucide-react';

export default function Layout() {
  const location = useLocation();

  return (
    <div className="flex h-screen bg-slate-900 text-slate-100 font-sans">
      {/* Sidebar */}
      <div className="w-64 bg-slate-950 border-r border-slate-800 p-4 flex flex-col gap-6">
        <div className="flex items-center gap-3 text-2xl font-bold text-white px-2 mt-4">
          <Droplet className="w-8 h-8 text-blue-500 fill-blue-500" />
          GoBioAI
        </div>
        
        <div className="text-xs font-bold tracking-wider text-slate-500 uppercase px-2 mt-4">Main Menu</div>
        
        <nav className="flex flex-col gap-1">
          <Link 
            to="/" 
            className={`flex items-center gap-3 p-3 rounded-xl transition-all font-medium ${location.pathname === '/' ? 'bg-blue-600/10 text-blue-400' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'}`}
          >
            <Activity className="w-5 h-5" />
            Live Dashboard
          </Link>
          <Link 
            to="/analytics" 
            className={`flex items-center gap-3 p-3 rounded-xl transition-all font-medium ${location.pathname === '/analytics' ? 'bg-blue-600/10 text-blue-400' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'}`}
          >
            <BarChart2 className="w-5 h-5" />
            Analytics
          </Link>
        </nav>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 overflow-auto bg-slate-900 p-8">
        <Outlet />
      </div>
    </div>
  );
}

```

## gobioai-dashboard\src\components\LiveDashboard.jsx

```javascript
import { useState, useEffect } from 'react';
import axios from 'axios';
import { Thermometer, Zap, Wifi, Clock, Power, BrainCircuit, ShieldCheck, AlertTriangle } from 'lucide-react';

export default function LiveDashboard() {
  const [sensorData, setSensorData] = useState(null);
  const [error, setError] = useState(false);
  
  // New State for Machine Learning Predictions
  const [aiPredictions, setAiPredictions] = useState({ anomaly: null, heater_prediction: null });

  // 1. Fetch Live Data from PostgreSQL
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://gobio-platform-cloud-h59g.onrender.com/device/live');
        setSensorData(response.data);
        setError(false);
      } catch (err) {
        console.error("Error fetching live data:", err);
        setError(true);
      }
    };

    fetchData(); 
    const interval = setInterval(fetchData, 2000); 
    return () => clearInterval(interval);
  }, []);

  // 2. Fetch AI Predictions whenever new data arrives
  useEffect(() => {
    if (!sensorData) return;

    const fetchPredictions = async () => {
      try {
        // Send the current sensor state to the AI endpoints
        const anomalyRes = await axios.post('https://gobio-platform-cloud-h59g.onrender.com/prediction/anomaly', sensorData);
        const heatingRes = await axios.post('https://gobio-platform-cloud-h59g.onrender.com/prediction/heating', sensorData);
        
        setAiPredictions({
          anomaly: anomalyRes.data.anomaly_detected,
          heater_prediction: heatingRes.data.prediction
        });
      } catch (err) {
        console.error("AI Prediction Error:", err);
      }
    };

    fetchPredictions();
  }, [sensorData]); // This triggers every time sensorData changes

  if (error) return <div className="p-8 text-xl font-bold text-red-500 flex items-center justify-center h-full">Error connecting to backend API. Is FastAPI running?</div>;
  // Check if the data is empty or hasn't loaded yet
  if (!sensorData || Object.keys(sensorData).length === 0) {
    return (
      <div style={{ padding: "50px", textAlign: "center", color: "white" }}>
        <h2>🔌 GoBioAI System Online</h2>
        <p>Waiting for the ESP32 hardware to transmit the first sensor payload...</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-6 max-w-6xl mx-auto animate-in fade-in duration-500 pb-10">
        {/* Header */}
        <div className="flex justify-between items-center bg-slate-800 p-6 rounded-3xl border border-slate-700/50 shadow-xl">
            <div>
                <h1 className="text-3xl font-bold text-white mb-2">Live Pasteurization Monitor</h1>
                <p className="text-slate-400 flex items-center gap-2 font-medium">
                    <span className="bg-slate-900 px-3 py-1 rounded-lg text-sm text-blue-400 font-mono tracking-wider shadow-inner">ID: {sensorData.machine_id}</span>
                    <span className="text-slate-600">•</span>
                    Last Updated: {new Date(sensorData.timestamp).toLocaleTimeString()}
                </p>
            </div>
            <div className={`px-5 py-2.5 rounded-full font-bold flex items-center gap-2 shadow-lg ${sensorData.process === 'HEATING' ? 'bg-orange-500/10 text-orange-400 border border-orange-500/30' : 'bg-green-500/10 text-green-400 border border-green-500/30'}`}>
                <Clock className="w-5 h-5" />
                {sensorData.process} MODE ({sensorData.mode})
            </div>
        </div>

        {/* Existing Metrics Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Temperature Card */}
            <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 relative overflow-hidden group hover:border-red-500/30 transition-colors">
                <div className="absolute -top-4 -right-4 p-4 opacity-10 group-hover:opacity-20 group-hover:scale-110 transition-all duration-300">
                    <Thermometer className="w-32 h-32 text-red-500" />
                </div>
                <h3 className="text-slate-400 font-medium mb-1">Current Temperature</h3>
                <div className="text-5xl font-black text-white flex items-baseline gap-1 mt-2">
                    {sensorData.temperature.toFixed(1)}<span className="text-2xl text-slate-500">°C</span>
                </div>
                <div className="mt-6 text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-3 rounded-xl">
                    <span>Target</span>
                    <span className="text-white font-bold">{sensorData.target_temperature}°C</span>
                </div>
            </div>

            {/* Voltage Card */}
            <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 relative overflow-hidden group hover:border-yellow-500/30 transition-colors">
                <div className="absolute -top-4 -right-4 p-4 opacity-10 group-hover:opacity-20 group-hover:scale-110 transition-all duration-300">
                    <Zap className="w-32 h-32 text-yellow-500" />
                </div>
                <h3 className="text-slate-400 font-medium mb-1">Voltage Input</h3>
                <div className="text-5xl font-black text-white flex items-baseline gap-1 mt-2">
                    {sensorData.voltage.toFixed(1)}<span className="text-2xl text-slate-500">V</span>
                </div>
                <div className="mt-6 text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-3 rounded-xl">
                    <span>Power Output</span>
                    <span className="text-white font-bold">{sensorData.power.toFixed(2)} kW</span>
                </div>
            </div>

            {/* Heater Status Card */}
            <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 relative overflow-hidden group hover:border-orange-500/30 transition-colors">
                <div className="absolute -top-4 -right-4 p-4 opacity-10 group-hover:opacity-20 group-hover:scale-110 transition-all duration-300">
                    <Power className="w-32 h-32 text-orange-500" />
                </div>
                <h3 className="text-slate-400 font-medium mb-1">Heater Relay</h3>
                <div className={`mt-4 inline-flex items-center justify-center w-16 h-16 rounded-2xl ${sensorData.heater_status ? 'bg-orange-500 text-white shadow-[0_0_30px_rgba(249,115,22,0.3)]' : 'bg-slate-900 text-slate-600'} transition-all duration-500`}>
                    <Power className={`w-8 h-8 ${sensorData.heater_status ? 'animate-pulse' : ''}`} />
                </div>
                <div className="mt-6 text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-3 rounded-xl">
                    <span>Status</span>
                    <span className={`font-bold ${sensorData.heater_status ? 'text-orange-400' : 'text-slate-500'}`}>{sensorData.heater_status ? 'ACTIVE' : 'OFF'}</span>
                </div>
            </div>

            {/* AI Heater Decision Card */}
            <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 relative overflow-hidden group hover:border-red-500/30 transition-colors">
                <div className="absolute -top-6 -right-4 p-4 opacity-10 group-hover:opacity-20 group-hover:scale-110 transition-all duration-300">
                    <span className="text-8xl">🔥</span>
                </div>
                <h3 className="text-slate-400 font-medium mb-1 flex items-center gap-2">
                    🔥 AI Heater Decision
                </h3>
                <div className="text-5xl font-black text-white flex items-baseline gap-1 mt-2">
                    {sensorData.heater_decision?.recommended_power ?? 0}<span className="text-2xl text-slate-500">%</span>
                </div>
                
                {/* Progress Bar */}
                <div className="w-full h-3 bg-slate-900 rounded-full mt-4 overflow-hidden shadow-inner border border-slate-700/50">
                    <div 
                        className="h-full transition-all duration-1000 ease-in-out"
                        style={{ 
                            width: `${sensorData.heater_decision?.recommended_power ?? 0}%`,
                            backgroundColor: (sensorData.heater_decision?.recommended_power ?? 0) === 0 ? '#64748b' :
                                             (sensorData.heater_decision?.recommended_power ?? 0) <= 10 ? '#22c55e' :
                                             (sensorData.heater_decision?.recommended_power ?? 0) <= 25 ? '#0ea5e9' :
                                             (sensorData.heater_decision?.recommended_power ?? 0) <= 50 ? '#eab308' :
                                             (sensorData.heater_decision?.recommended_power ?? 0) <= 75 ? '#f97316' : '#ef4444'
                        }}
                    />
                </div>
                
                <div className="mt-5 flex flex-col gap-2">
                    <div className="text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-2.5 rounded-xl">
                        <span>Action</span>
                        <span className="text-white font-bold text-right">{sensorData.heater_decision?.action ?? 'N/A'}</span>
                    </div>
                    <div className="text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-2.5 rounded-xl">
                        <span>Status</span>
                        <span className="text-white font-bold text-right">{sensorData.heater_decision?.status ?? 'N/A'}</span>
                    </div>
                    <div className="text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-2.5 rounded-xl">
                        <span>Diff</span>
                        <span className="text-white font-bold text-right">
                            {sensorData.heater_decision?.difference ?? 0}°C 
                            {sensorData.temperature < sensorData.target_temperature ? ' Below Target' : 
                             (sensorData.temperature > sensorData.target_temperature ? ' Above Target' : ' At Target')}
                        </span>
                    </div>
                </div>
            </div>

            {/* WiFi Status Card */}
            <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 relative overflow-hidden group hover:border-blue-500/30 transition-colors">
                <div className="absolute -top-4 -right-4 p-4 opacity-10 group-hover:opacity-20 group-hover:scale-110 transition-all duration-300">
                    <Wifi className="w-32 h-32 text-blue-500" />
                </div>
                <h3 className="text-slate-400 font-medium mb-1">ESP32 Connection</h3>
                <div className={`mt-4 inline-flex items-center justify-center w-16 h-16 rounded-2xl ${sensorData.wifi_connected ? 'bg-blue-500 text-white shadow-[0_0_30px_rgba(59,130,246,0.3)]' : 'bg-red-500 text-white shadow-[0_0_30px_rgba(239,68,68,0.3)]'} transition-all duration-500`}>
                    <Wifi className="w-8 h-8" />
                </div>
                <div className="mt-6 text-sm text-slate-400 flex justify-between items-center bg-slate-900/50 p-3 rounded-xl">
                    <span>Network</span>
                    <span className={`font-bold ${sensorData.wifi_connected ? 'text-blue-400' : 'text-red-400'}`}>{sensorData.wifi_connected ? 'STABLE' : 'DISCONNECTED'}</span>
                </div>
            </div>
        </div>

        {/* --- NEW MACHINE LEARNING INSIGHTS SECTION --- */}
        <div className="mt-4">
            <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
                <BrainCircuit className="w-6 h-6 text-purple-400" /> 
                Live AI Insights
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                
                {/* Anomaly Detection AI */}
                <div className={`p-6 rounded-3xl shadow-xl border flex items-center gap-6 transition-colors ${aiPredictions.anomaly ? 'bg-red-900/20 border-red-500/50' : 'bg-slate-800 border-slate-700/50'}`}>
                    <div className={`p-4 rounded-2xl ${aiPredictions.anomaly ? 'bg-red-500/20 text-red-400' : 'bg-emerald-500/20 text-emerald-400'}`}>
                        {aiPredictions.anomaly ? <AlertTriangle className="w-10 h-10" /> : <ShieldCheck className="w-10 h-10" />}
                    </div>
                    <div>
                        <h3 className="text-slate-400 font-medium text-sm tracking-wider uppercase mb-1">System Health (Isolation Forest)</h3>
                        {aiPredictions.anomaly === null ? (
                            <div className="text-2xl font-bold text-slate-500 animate-pulse">Analyzing...</div>
                        ) : (
                            <div className={`text-2xl font-bold ${aiPredictions.anomaly ? 'text-red-400' : 'text-emerald-400'}`}>
                                {aiPredictions.anomaly ? 'ANOMALY DETECTED' : 'OPTIMAL'}
                            </div>
                        )}
                        <p className="text-slate-500 text-sm mt-1">Constantly checking physics for mechanical failures.</p>
                    </div>
                </div>

                {/* AI Heater Control Prediction */}
                <div className="bg-slate-800 p-6 rounded-3xl shadow-xl border border-slate-700/50 flex items-center gap-6">
                    <div className="p-4 rounded-2xl bg-purple-500/20 text-purple-400">
                        <BrainCircuit className="w-10 h-10" />
                    </div>
                    <div>
                        <h3 className="text-slate-400 font-medium text-sm tracking-wider uppercase mb-1">AI Heater Target (Random Forest)</h3>
                        {aiPredictions.heater_prediction === null ? (
                            <div className="text-2xl font-bold text-slate-500 animate-pulse">Calculating...</div>
                        ) : (
                            <div className="text-2xl font-bold text-white">
                                {aiPredictions.heater_prediction === 1.0 ? 'SHOULD BE ON' : 'SHOULD BE OFF'}
                            </div>
                        )}
                        <p className="text-slate-500 text-sm mt-1">Predicting optimal thermal state based on historical data.</p>
                    </div>
                </div>

            </div>
        </div>
    </div>
  );
}

```

## machine_learning\feature_engineering.py

```python
import pandas as pd
import numpy as np

def generate_features(df):
    """
    Applies feature engineering to the preprocessed GoBioAI telemetry.
    Generates thermal, energetic, and temporal features.
    """
    print(f"\n--- Starting Feature Engineering ---")
    df = df.copy()

    # 1. Thermal Features
    if 'temperature' in df.columns and 'target_temperature' in df.columns:
        df['temp_diff_from_target'] = df['temperature'] - df['target_temperature']
        df['temp_rate_of_change'] = df['temperature'].diff().fillna(0)

    # 2. Energetic Features
    if 'power' in df.columns:
        df['power_trend'] = df['power'].diff().fillna(0)
        # Assuming readings are every second; cumulative power over time
        df['energy_consumed_ws'] = df['power'].cumsum() 

    # 3. Runtime Features (Cumulative sum of active states)
    if 'heater_status' in df.columns:
        df['heater_runtime_sec'] = df['heater_status'].cumsum()
    
    # 4. Process Percentages (Simplified heuristics)
    if 'target_temperature' in df.columns and 'temperature' in df.columns:
        # Prevent division by zero
        safe_target = df['target_temperature'].replace(0, 1)
        df['heating_progress_pct'] = (df['temperature'] / safe_target) * 100
        df['heating_progress_pct'] = df['heating_progress_pct'].clip(0, 100)

    # Drop any new NaNs created by diff() functions
    df = df.fillna(0)

    print(f"Features generated: {list(df.columns)}")
    print(f"--- Feature Engineering Complete ---\n")
    
    return df

```

## machine_learning\predict.py

```python
import os
import joblib
import pandas as pd
from fastapi import HTTPException
from machine_learning.preprocessing import preprocess_telemetry
from machine_learning.feature_engineering import generate_features

MODEL_DIR = "machine_learning/models/"

def load_model(model_name: str):
    """Loads a trained Joblib model from disk safely."""
    filepath = os.path.join(MODEL_DIR, model_name)
    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=404, 
            detail=f"Model '{model_name}' not found. Please train the model first."
        )
    return joblib.load(filepath)

def make_prediction(live_json_data: dict, model_name: str):
    """
    1. Accepts raw JSON from the ESP32.
    2. Runs it through the preprocessing pipeline.
    3. Runs it through feature engineering.
    4. Feeds it to the loaded model and returns the result.
    """
    try:
        # Remove UI injected payload from the ML pipeline to prevent Pandas crash
        if isinstance(live_json_data, dict) and "heater_decision" in live_json_data:
            # We use copy() so we don't mutate the original request dictionary
            clean_data = live_json_data.copy()
            del clean_data["heater_decision"]
        else:
            clean_data = live_json_data
            
        # Step 1 & 2: Clean and Engineer
        df_clean = preprocess_telemetry(clean_data)
        df_features = generate_features(df_clean)
        
        # Step 3: Load Model
        model = load_model(model_name)
        
        # Step 4: Predict (Aligning columns to match training data)
        if hasattr(model, 'feature_names_in_'):
            # Convert existing columns to numeric, coercing any errors to 0
            for col in df_features.columns:
                df_features[col] = pd.to_numeric(df_features[col], errors='coerce').fillna(0)
            
            # Fill missing model features with 0
            for col in model.feature_names_in_:
                if col not in df_features.columns:
                    df_features[col] = 0.0
            
            # Keep only the trained features in the exact training order
            df_features = df_features[list(model.feature_names_in_)]
            
        prediction = model.predict(df_features)
        
        return {"status": "success", "prediction": float(prediction[0])}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

```

## machine_learning\preprocessing.py

```python
import pandas as pd
import numpy as np

def preprocess_telemetry(raw_data):
    """
    Automatically preprocesses raw ESP32 JSON telemetry for the ML pipeline.
    Handles both single JSON objects (live prediction) and lists of objects (batch training).
    """
    # 1. Detect single object vs list and convert to DataFrame
    if isinstance(raw_data, dict):
        df = pd.DataFrame([raw_data])
    elif isinstance(raw_data, list):
        df = pd.DataFrame(raw_data)
    else:
        raise ValueError("Input must be a JSON object (dict) or a list of objects.")

    print(f"\n--- Initial DataFrame Shape: {df.shape} ---")
    
    # 2. Remove duplicates
    initial_len = len(df)
    df = df.drop_duplicates()
    
    # 3. Handle missing values 
    df = df.ffill().bfill()
    
    # 4. Convert ON/OFF and TRUE/FALSE into 1/0
    bool_mapping = {True: 1, False: 0, "TRUE": 1, "FALSE": 0, "ON": 1, "OFF": 0, "on": 1, "off": 0}
    for col in df.columns:
        if df[col].apply(lambda x: x in bool_mapping.keys()).any():
            df[col] = df[col].map(bool_mapping).fillna(df[col])

    # 5. Convert AUTO/MANUAL into numerical values
    if 'mode' in df.columns:
        mode_mapping = {"AUTO": 1, "MANUAL": 0, "auto": 1, "manual": 0}
        df['mode'] = df['mode'].map(mode_mapping).fillna(df['mode'])

    # 6. Encode categorical columns (process, device_status)
    if 'process' in df.columns:
        df = pd.get_dummies(df, columns=['process'], dummy_na=False, dtype=int)
        
    if 'device_status' in df.columns:
        df = pd.get_dummies(df, columns=['device_status'], dummy_na=False, dtype=int)

    # 7. Convert timestamps into datetime and generate features
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['day'] = df['timestamp'].dt.day
        df['month'] = df['timestamp'].dt.month

    # 8. Remove unnecessary columns
    cols_to_drop = ['machine_id', 'serial_number', 'firmware_version', 'hardware_version', 'wifi_ssid', 'timestamp']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

    # 9. Detect invalid sensor values and filter them (only for batch training)
    # We don't filter during live inference (single row) so we don't return an empty DataFrame
    if len(df) > 1:
        if 'temperature' in df.columns:
            df = df[(df['temperature'] >= 0.0) & (df['temperature'] <= 150.0)]
        if 'voltage' in df.columns:
            df = df[(df['voltage'] >= 0.0) & (df['voltage'] <= 300.0)]

    print(f"--- Preprocessing Complete ---")
    print(f"Rows removed (duplicates/invalid): {initial_len - len(df)}")
    print(f"Final Shape: {df.shape}")
    print(f"Columns ready for engineering: {list(df.columns)}\n")

    return df
```

## machine_learning\train_models.py

```python
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, IsolationForest
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, classification_report
import numpy as np

class PasteurizationModelTrainer:
    def __init__(self, data: pd.DataFrame, model_dir="machine_learning/models/"):
        df = data.copy()
        if 'id' in df.columns:
            df = df.drop(columns=['id'])
            
        # Convert all columns to numeric, coercing strings/errors to NaN, then fill with 0
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
        self.data = df
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)

    def split_data(self, target_col):
        X = self.data.drop(columns=[target_col])
        y = self.data[target_col]
        # 80/20 Split as requested
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_numerical(self, target_col, model_name):
        print(f"\nTraining Regressor for: {target_col}")
        X_train, X_test, y_train, y_test = self.split_data(target_col)
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        
        # Evaluation
        print(f"MAE: {mean_absolute_error(y_test, predictions):.4f}")
        print(f"RMSE: {np.sqrt(mean_squared_error(y_test, predictions)):.4f}")
        print(f"R2 Score: {r2_score(y_test, predictions):.4f}")
        
        self.save_model(model, model_name)

    def train_categorical(self, target_col, model_name):
        print(f"\nTraining Classifier for: {target_col}")
        X_train, X_test, y_train, y_test = self.split_data(target_col)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        
        # Evaluation
        print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
        print("Classification Report:\n", classification_report(y_test, predictions))
        
        self.save_model(model, model_name)

    def train_anomaly_detection(self, model_name="fault_model.pkl"):
        print(f"\nTraining Isolation Forest for Anomaly Detection")
        # Isolation forest doesn't need a target column
        model = IsolationForest(contamination=0.05, random_state=42)
        model.fit(self.data)
        
        print("Isolation Forest trained successfully on full dataset.")
        self.save_model(model, model_name)

    def save_model(self, model, filename):
        filepath = os.path.join(self.model_dir, filename)
        joblib.dump(model, filepath)
        print(f"[Success] Model saved to {filepath}")

# --- Example Usage (We will trigger this later from the API) ---
# if __name__ == "__main__":
#     trainer = PasteurizationModelTrainer(df)
#     trainer.train_numerical('time_to_target', 'heating_model.pkl')
#     trainer.train_anomaly_detection('fault_model.pkl')

```

## machine_learning\__init__.py

```python

```

## routers\device.py

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import schemas
import models
from database import get_db
from services.industrial_logic import calculate_heater_decision

router = APIRouter(
    prefix="/device",
    tags=["IoT Device Endpoints"]
)

# 1. The Ingestion API (For the ESP32)
@router.post("/data")
def receive_sensor_data(payload: schemas.LiveData, db: Session = Depends(get_db)):
    
    # 1. Convert the massive Pydantic payload into a dictionary
    # We exclude fields that exist in the JSON but not in our models.py database table
    data_dict = payload.model_dump(exclude={
        'type', 'machine_name', 'serial_number', 'firmware_version', 
        'hardware_version', 'wifi_ssid', 'wifi_rssi', 'server_connected', 
        'last_sync_sec', 'alarm_code', 'alarm_message',
        'heater_on_temperature', 'heater_off_temperature',
        'cooler_on_temperature', 'cooler_off_temperature'
    })
    
    # 2. The timestamp is now auto-parsed into a DateTime object by Pydantic
    # We just need to handle the case where it might be missing (None)
    data_dict['timestamp'] = payload.timestamp if payload.timestamp else datetime.utcnow()

    # 3. The Magic Trick: **data_dict automatically maps all 30 remaining fields into the database!
    new_data = models.SensorData(**data_dict)
    
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    
    print(f"✅ Full Industrial Data saved for {payload.machine_id}: Temp={payload.temperature}°C")
    return {"status": "success", "message": "Data safely stored in GoBioAI database"}

# 2. The LIVE API (Fetching from PostgreSQL)
@router.get("/live")
def get_live_data(db: Session = Depends(get_db)):
    # 1. Fetch the absolute latest row from the vault
    latest_data = db.query(models.SensorData).order_by(models.SensorData.id.desc()).first()
    
    if not latest_data:
        return {}
        
    # 2. Dynamically grab ALL 37 columns from the database row
    live_dict = {column.name: getattr(latest_data, column.name) for column in latest_data.__table__.columns}
    
    # 3. Safely override the heater_status so the React UI doesn't crash, 
    # while preserving the other 36 columns for the AI models!
    live_dict["heater_status"] = (latest_data.heater_status == "ON" or latest_data.heater_status is True)
    
    # 4. Inject Module 3: AI Heater Decision Engine
    temperature = live_dict.get("temperature", 0.0)
    target_temperature = live_dict.get("target_temperature", 0.0)
    live_dict["heater_decision"] = calculate_heater_decision(temperature, target_temperature)
    
    return live_dict

# 3. The HISTORY API (For the Analytics Charts)
@router.get("/history")
def get_historical_data(limit: int = 50, db: Session = Depends(get_db)):
    # Fetch the latest X records, ordered by newest first
    records = db.query(models.SensorData).order_by(models.SensorData.id.desc()).limit(limit).all()
    
    if not records:
        return []
        
    # Reverse the list so it reads chronologically (oldest -> newest) for the chart
    records.reverse()
    
    # Format the data cleanly for Recharts
    history_data = []
    for r in records:
        history_data.append({
            # Format time as HH:MM:SS for the X-axis
            "time": r.timestamp.strftime("%H:%M:%S") if r.timestamp else "00:00:00",
            "temperature": round(r.temperature or 0.0, 2),
            "target": round(r.target_temperature or 0.0, 2),
            "power": round(r.power or 0.0, 2)
        })
        
    return history_data

```

## routers\prediction.py

```python
from fastapi import APIRouter, Body
from machine_learning.predict import make_prediction
from services.industrial_logic import check_industrial_safety_override

# Creates a dedicated router for all /prediction endpoints
router = APIRouter(
    prefix="/prediction",
    tags=["Machine Learning Inference"]
)

@router.post("/heating")
def predict_heating_time(sensor_data: dict = Body(...)):
    """Predicts the remaining heating time based on live ESP32 telemetry."""
    # Assumes you have trained and saved a model named 'heating_model.pkl'
    result = make_prediction(sensor_data, "heating_model.pkl")
    return result

@router.post("/health")
def predict_machine_health(sensor_data: dict = Body(...)):
    """Classifies the current health status of the pasteurizer."""
    # Assumes you have trained and saved a model named 'health_model.pkl'
    result = make_prediction(sensor_data, "health_model.pkl")
    return result

@router.post("/anomaly")
def detect_faults(sensor_data: dict = Body(...)):
    """Uses Isolation Forest to detect if the current reading is an anomaly."""
    
    # 1. Industrial Safety Override (Validates physics BEFORE ML)
    safety_override = check_industrial_safety_override(sensor_data)
    if safety_override:
        return safety_override
        
    # 2. Existing Machine Learning Model Execution
    result = make_prediction(sensor_data, "fault_model.pkl")
    # Isolation Forest returns -1 for anomalies and 1 for normal
    is_anomaly = True if result["prediction"] == -1 else False
    return {"status": "success", "anomaly_detected": is_anomaly}

```

## routers\__init__.py

```python
# Init file for routers package

```

## services\industrial_logic.py

```python
import datetime

def check_industrial_safety_override(sensor_data: dict):
    """
    Validates industrial safety limits BEFORE the ML model executes.
    Returns a forced response dictionary if safe limits are exceeded.
    Returns None if all values are within safe operating limits.
    """
    try:
        temperature = float(sensor_data.get("temperature", 0.0))
        power = float(sensor_data.get("power", 0.0))
        voltage = float(sensor_data.get("voltage", 0.0))
    except (TypeError, ValueError):
        return None

    reason = None
    if temperature > 100:
        reason = "Temperature exceeded safe operating limit (> 100°C)."
    elif power > 2500:
        reason = "Power exceeded safe operating limit (> 2500W)."
    elif voltage > 260:
        reason = "Voltage exceeded safe operating limit (> 260V)."

    if reason:
        # Log the safety override event
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n--- Industrial Safety Override Triggered ---")
        print(f"Timestamp:   {timestamp}")
        print(f"Temperature: {temperature}°C")
        print(f"Voltage:     {voltage}V")
        print(f"Power:       {power}W")
        print(f"Reason:      {reason}")
        print(f"Source:      Industrial Safety Override\n")
        
        return {
            "status": "Critical",
            "anomaly_detected": True,
            "label": "ANOMALY DETECTED",
            "prediction": "Anomaly",
            "confidence": 100,
            "source": "Industrial Safety Override",
            "reason": reason,
            "override": True
        }
        
    return None

def calculate_heater_decision(temperature: float, target_temperature: float) -> dict:
    """
    Module 3: AI Heater Decision Engine
    Calculates the recommended power, action, and status based on temperature differences.
    """
    if temperature < target_temperature:
        difference = target_temperature - temperature
        if difference > 20:
            power = 100
            action = "Maximum Heating"
            status = "Critical Heating Required"
        elif difference > 10:  # 10-20
            power = 75
            action = "Moderate Heating"
            status = "Heating Required"
        elif difference > 5:   # 5-10
            power = 50
            action = "Steady Heating"
            status = "Approaching Target"
        elif difference > 2:   # 2-5
            power = 25
            action = "Fine Tuning"
            status = "Near Target"
        else:                  # <= 2
            power = 10
            action = "Maintain Temperature"
            status = "Stable"
    else:
        difference = temperature - target_temperature
        if difference > 2:     # temperature > target_temperature + 2
            power = 0
            action = "Cooling Recommended"
            status = "Overheating"
        else:                  # temperature >= target_temperature and <= +2
            power = 0
            action = "Turn Heater OFF"
            status = "Pasteurization Temperature Reached"

    return {
        "recommended_power": power,
        "action": action,
        "status": status,
        "difference": round(difference, 2)
    }

```

## services\__init__.py

```python
# init

```
