# Project Structure: milk project_updated

```text
milk project_updated/
    .env
    .gitignore
    README.md
    alembic.ini
    database.py
    error_log.txt
    main.py
    models.py
    requirements.txt
    schemas.py
    train_pipeline.py
    alembic/
        README
        env.py
        script.py.mako
        versions/
            a631c499ce92_add_machine_command_system.py
            b742d500de01_migrate_sensor_data_schema.py
    esp32_controller/
        Config.h
        Hardware.cpp
        Hardware.h
        Network.cpp
        Network.h
        StateMachine.cpp
        StateMachine.h
        esp32_controller.ino
    gobioai-dashboard/
        .gitignore
        .oxlintrc.json
        README.md
        index.html
        package-lock.json
        package.json
        postcss.config.js
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
        __init__.py
        feature_engineering.py
        predict.py
        preprocessing.py
        train_models.py
        models/
            energy_model.pkl
            fault_model.pkl
            heating_model.pkl
    routers/
        __init__.py
        commands.py
        device.py
        prediction.py
    services/
        __init__.py
        industrial_logic.py
        websocket_manager.py
```

# File Contents

## .env

```text
DATABASE_URL="postgresql://neondb_owner:npg_jHJT8i1SYKIk@ep-empty-union-ai3yyr32.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

```

## .gitignore

```text
# Python
venv/
__pycache__/
*.pyc
.env

# React / Node
node_modules/
dist/
.env.local

# Database
*.sqlite3

```

## README.md

```md
"# milk_project_updated" 

```

## alembic.ini

```ini
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file.
sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

```

## database.py

```py
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

```py
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  # <-- We are importing uvicorn directly now
from database import engine
import models
from routers import device
from routers import prediction
from routers import commands
from pydantic import BaseModel

# (Moved logic to routers/device.py)

# Safely create tables during startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    print("[OK] PostgreSQL GoBioAI Vault connected and tables verified.")
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
app.include_router(commands.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Milk Pasteurization IoT Backend API"}

```

## models.py

```py
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
    parameters = Column(JSON, default={})
    status = Column(String, default="CREATED") # CREATED, PENDING, SENT, EXECUTED, FAILED
    error_reason = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)
    received_at = Column(DateTime, nullable=True)
    executed_at = Column(DateTime, nullable=True)

```

## requirements.txt

*Could not read file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte*

## schemas.py

```py
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

```

## train_pipeline.py

```py
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

## alembic\README

```text
Generic single-database configuration.
```

## alembic\env.py

```py
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import models
from database import Base, SQLALCHEMY_DATABASE_URL

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

## alembic\script.py.mako

```mako
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}

```

## alembic\versions\a631c499ce92_add_machine_command_system.py

```py
"""add machine command system

Revision ID: a631c499ce92
Revises: 
Create Date: 2026-08-22 18:07:15.263095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a631c499ce92'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('command_id', sa.String(), nullable=True),
    sa.Column('machine_id', sa.String(), nullable=True),
    sa.Column('command', sa.String(), nullable=True),
    sa.Column('parameters', sa.JSON(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('error_reason', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('received_at', sa.DateTime(), nullable=True),
    sa.Column('executed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commands_command_id'), 'commands', ['command_id'], unique=True)
    op.create_index(op.f('ix_commands_id'), 'commands', ['id'], unique=False)
    op.create_index(op.f('ix_commands_machine_id'), 'commands', ['machine_id'], unique=False)
    op.create_table('machines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('machine_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('online', sa.Boolean(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('mode', sa.String(), nullable=True),
    sa.Column('process_state', sa.String(), nullable=True),
    sa.Column('auto_running', sa.Boolean(), nullable=True),
    sa.Column('emergency_stop', sa.Boolean(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('target_temperature', sa.Float(), nullable=True),
    sa.Column('cool_temperature', sa.Float(), nullable=True),
    sa.Column('hysteresis', sa.Float(), nullable=True),
    sa.Column('hold_time_minutes', sa.Integer(), nullable=True),
    sa.Column('heater', sa.Boolean(), nullable=True),
    sa.Column('stirrer', sa.Boolean(), nullable=True),
    sa.Column('cooler', sa.Boolean(), nullable=True),
    sa.Column('voltage', sa.Float(), nullable=True),
    sa.Column('current', sa.Float(), nullable=True),
    sa.Column('power', sa.Float(), nullable=True),
    sa.Column('energy', sa.Float(), nullable=True),
    sa.Column('frequency', sa.Float(), nullable=True),
    sa.Column('power_factor', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_machines_id'), 'machines', ['id'], unique=False)
    op.create_index(op.f('ix_machines_machine_id'), 'machines', ['machine_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_machines_machine_id'), table_name='machines')
    op.drop_index(op.f('ix_machines_id'), table_name='machines')
    op.drop_table('machines')
    op.drop_index(op.f('ix_commands_machine_id'), table_name='commands')
    op.drop_index(op.f('ix_commands_id'), table_name='commands')
    op.drop_index(op.f('ix_commands_command_id'), table_name='commands')
    op.drop_table('commands')
    # ### end Alembic commands ###

```

## alembic\versions\b742d500de01_migrate_sensor_data_schema.py

```py
"""migrate sensor_data to new unified schema

Revision ID: b742d500de01
Revises: a631c499ce92
Create Date: 2026-09-06 16:15:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'b742d500de01'
down_revision: Union[str, Sequence[str], None] = 'a631c499ce92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Migrate sensor_data from the old V1 schema to the new unified schema.
    We use ADD COLUMN + DROP COLUMN approach (safer than rename) so existing
    data is preserved. All new columns are nullable so existing rows are safe.
    """
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    existing_cols = {c['name'] for c in inspector.get_columns('sensor_data')}

    # --- ADD new columns (only if they don't already exist) ---
    new_columns = {
        'online':                sa.Boolean(),
        'process_state':         sa.String(),
        'cooling_temperature':   sa.Float(),
        'heater':                sa.Boolean(),
        'stirrer':               sa.Boolean(),
        'cooler':                sa.Boolean(),
        'running':               sa.Boolean(),
        'emergency':             sa.Boolean(),
        'fault':                 sa.Boolean(),
        'fault_code':            sa.String(),
        'last_command':          sa.String(),
        'last_command_id':       sa.String(),
        'command_status':        sa.String(),
    }
    for col_name, col_type in new_columns.items():
        if col_name not in existing_cols:
            op.add_column('sensor_data', sa.Column(col_name, col_type, nullable=True))
            print(f"  [ADD] column: {col_name}")

    # --- MIGRATE data from old columns into new columns ---
    # Map: old process -> new process_state
    if 'process' in existing_cols and 'process_state' in existing_cols or 'process' in existing_cols:
        conn.execute(sa.text('UPDATE sensor_data SET process_state = "process" WHERE process_state IS NULL'))

    # Map old heater_enabled/heater_status -> new heater (bool)
    if 'heater_enabled' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET heater = (heater_enabled = TRUE OR heater_status = 'ON') WHERE heater IS NULL"
        ))
    if 'cooler_enabled' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET cooler = (cooler_enabled = TRUE OR cooler_status = 'ON') WHERE cooler IS NULL"
        ))
    if 'stirrer_enabled' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET stirrer = (stirrer_enabled = TRUE OR stirrer_status = 'ON') WHERE stirrer IS NULL"
        ))

    # Map old emergency_stop -> emergency
    if 'emergency_stop' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET emergency = emergency_stop WHERE emergency IS NULL"
        ))

    # Map old alarm -> fault
    if 'alarm' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET fault = alarm WHERE fault IS NULL"
        ))

    # Map old process_running -> running
    if 'process_running' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET running = process_running WHERE running IS NULL"
        ))

    # Map old cooling_target_temperature -> cooling_temperature
    if 'cooling_target_temperature' in existing_cols:
        conn.execute(sa.text(
            "UPDATE sensor_data SET cooling_temperature = cooling_target_temperature WHERE cooling_temperature IS NULL"
        ))

    # Default online = TRUE for all historical rows
    conn.execute(sa.text("UPDATE sensor_data SET online = TRUE WHERE online IS NULL"))

    # --- DROP old columns that no longer exist in models.py ---
    old_columns_to_drop = [
        'uptime_sec', 'process', 'process_step', 'process_running',
        'process_paused', 'process_completed', 'emergency_stop',
        'batch_number', 'recipe_name', 'cooling_target_temperature',
        'heater_enabled', 'heater_status',
        'cooler_enabled', 'cooler_status',
        'stirrer_enabled', 'stirrer_status',
        'heater_runtime_sec', 'cooler_runtime_sec', 'stirrer_runtime_sec',
        'wifi_connected', 'alarm', 'device_status',
    ]
    for col_name in old_columns_to_drop:
        if col_name in existing_cols:
            op.drop_column('sensor_data', col_name)
            print(f"  [DROP] column: {col_name}")


def downgrade() -> None:
    """Re-add old columns. Data previously in them is lost."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    existing_cols = {c['name'] for c in inspector.get_columns('sensor_data')}

    old_columns = {
        'uptime_sec': sa.Integer(), 'process': sa.String(), 'process_step': sa.Integer(),
        'process_running': sa.Boolean(), 'process_paused': sa.Boolean(),
        'process_completed': sa.Boolean(), 'emergency_stop': sa.Boolean(),
        'batch_number': sa.Integer(), 'recipe_name': sa.String(),
        'cooling_target_temperature': sa.Float(), 'heater_enabled': sa.Boolean(),
        'heater_status': sa.String(), 'cooler_enabled': sa.Boolean(),
        'cooler_status': sa.String(), 'stirrer_enabled': sa.Boolean(),
        'stirrer_status': sa.String(), 'heater_runtime_sec': sa.Integer(),
        'cooler_runtime_sec': sa.Integer(), 'stirrer_runtime_sec': sa.Integer(),
        'wifi_connected': sa.Boolean(), 'alarm': sa.Boolean(), 'device_status': sa.String(),
    }
    for col_name, col_type in old_columns.items():
        if col_name not in existing_cols:
            op.add_column('sensor_data', sa.Column(col_name, col_type, nullable=True))

    new_cols_to_drop = [
        'online', 'process_state', 'cooling_temperature', 'heater', 'stirrer',
        'cooler', 'running', 'emergency', 'fault', 'fault_code',
        'last_command', 'last_command_id', 'command_status',
    ]
    for col_name in new_cols_to_drop:
        if col_name in existing_cols:
            op.drop_column('sensor_data', col_name)

```

## esp32_controller\Config.h

```h
#ifndef CONFIG_H
#define CONFIG_H

// WiFi Configuration
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// Server API Endpoint
const char* API_ENDPOINT = "http://192.168.1.100:8000/device/data";

// Device Settings
const char* MACHINE_ID = "ESP32_Pasteurizer_01";
const unsigned long TELEMETRY_INTERVAL_MS = 5000;
const unsigned long SERVER_TIMEOUT_MS = 60000;

// Pin Definitions
#define PIN_DS18B20       22
#define PIN_RELAY_HEATER  16
#define PIN_RELAY_STIRRER 17
#define PIN_RELAY_COOLER  27
#define PIN_PZEM_RX       25
#define PIN_PZEM_TX       26

// Process Safety Settings
const float MAX_SAFE_TEMPERATURE = 95.0; // Hard cutoff for heater

// Relay Logic (Change to LOW if relays are active-low)
#define RELAY_ON  HIGH
#define RELAY_OFF LOW

#endif // CONFIG_H

```

## esp32_controller\Hardware.cpp

```cpp
#include "Hardware.h"
#include "Config.h"

Hardware hardware;

Hardware::Hardware() 
    : oneWire(PIN_DS18B20), 
      sensors(&oneWire),
      pzem(Serial2, PIN_PZEM_RX, PIN_PZEM_TX),
      heaterState(false), stirrerState(false), coolerState(false),
      temperature(-127.0), sensorFault(true),
      voltage(0), current(0), power(0), energy(0), frequency(0), powerFactor(0), pzemFault(false)
{
}

void Hardware::init() {
    pinMode(PIN_RELAY_HEATER, OUTPUT);
    pinMode(PIN_RELAY_STIRRER, OUTPUT);
    pinMode(PIN_RELAY_COOLER, OUTPUT);
    
    setHeater(false);
    setStirrer(false);
    setCooler(false);
    
    sensors.begin();
}

void Hardware::update() {
    // Read Temperature
    sensors.requestTemperatures();
    float tempC = sensors.getTempCByIndex(0);
    
    if (tempC == DEVICE_DISCONNECTED_C || tempC < -50.0 || tempC > 150.0) {
        sensorFault = true;
    } else {
        temperature = tempC;
        sensorFault = false;
    }
    
    // Read PZEM
    float v = pzem.voltage();
    if (isnan(v)) {
        pzemFault = true;
    } else {
        pzemFault = false;
        voltage = v;
        current = pzem.current();
        power = pzem.power();
        energy = pzem.energy();
        frequency = pzem.frequency();
        powerFactor = pzem.pf();
    }
}

void Hardware::setHeater(bool state) {
    // Hardware-level safety constraint: never turn on if sensor faulty or over temperature
    if (state && !sensorFault && temperature < MAX_SAFE_TEMPERATURE) {
        digitalWrite(PIN_RELAY_HEATER, RELAY_ON);
        heaterState = true;
    } else {
        digitalWrite(PIN_RELAY_HEATER, RELAY_OFF);
        heaterState = false;
    }
}

void Hardware::setStirrer(bool state) {
    digitalWrite(PIN_RELAY_STIRRER, state ? RELAY_ON : RELAY_OFF);
    stirrerState = state;
}

void Hardware::setCooler(bool state) {
    digitalWrite(PIN_RELAY_COOLER, state ? RELAY_ON : RELAY_OFF);
    coolerState = state;
}

```

## esp32_controller\Hardware.h

```h
#ifndef HARDWARE_H
#define HARDWARE_H

#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <PZEM004Tv30.h>

class Hardware {
public:
    Hardware();
    void init();
    void update();
    
    // Commands
    void setHeater(bool state);
    void setStirrer(bool state);
    void setCooler(bool state);
    
    // Outputs
    bool isHeaterOn() const { return heaterState; }
    bool isStirrerOn() const { return stirrerState; }
    bool isCoolerOn() const { return coolerState; }
    
    // Telemetry
    float getTemperature() const { return temperature; }
    bool isSensorFault() const { return sensorFault; }
    
    float getVoltage() const { return voltage; }
    float getCurrent() const { return current; }
    float getPower() const { return power; }
    float getEnergy() const { return energy; }
    float getFrequency() const { return frequency; }
    float getPowerFactor() const { return powerFactor; }
    bool isPzemFault() const { return pzemFault; }
    
private:
    OneWire oneWire;
    DallasTemperature sensors;
    PZEM004Tv30 pzem;
    
    bool heaterState;
    bool stirrerState;
    bool coolerState;
    
    float temperature;
    bool sensorFault;
    
    float voltage;
    float current;
    float power;
    float energy;
    float frequency;
    float powerFactor;
    bool pzemFault;
};

extern Hardware hardware;

#endif // HARDWARE_H

```

## esp32_controller\Network.cpp

```cpp
#include "Network.h"
#include "Config.h"
#include "Hardware.h"
#include "StateMachine.h"

Network network;

Network::Network() : lastTelemetryTime(0) {}

void Network::init() {
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}

void Network::update() {
    if (WiFi.status() != WL_CONNECTED) {
        return; // Wait for connection
    }
    
    unsigned long now = millis();
    if (now - lastTelemetryTime >= TELEMETRY_INTERVAL_MS) {
        lastTelemetryTime = now;
        sendTelemetry();
    }
}

const char* modeToString(ProcessMode m) {
    switch (m) {
        case MODE_IDLE: return "IDLE";
        case MODE_AUTO: return "AUTO";
        case MODE_MANUAL: return "MANUAL";
        case MODE_EMERGENCY: return "EMERGENCY";
        default: return "UNKNOWN";
    }
}

const char* stateToString(ProcessState s) {
    switch (s) {
        case STATE_IDLE: return "IDLE";
        case STATE_HEATING: return "HEATING";
        case STATE_HOLDING: return "HOLDING";
        case STATE_COOLING: return "COOLING";
        case STATE_COMPLETE: return "COMPLETE";
        case STATE_MANUAL: return "MANUAL";
        case STATE_EMERGENCY: return "EMERGENCY";
        case STATE_FAULT: return "FAULT";
        default: return "UNKNOWN";
    }
}

const char* faultToString(FaultCode f) {
    switch (f) {
        case FAULT_NONE: return "";
        case FAULT_TEMP_SENSOR_ERROR: return "TEMP_SENSOR_ERROR";
        case FAULT_OVER_TEMPERATURE: return "OVER_TEMPERATURE";
        case FAULT_INVALID_COMMAND: return "INVALID_COMMAND";
        case FAULT_EMERGENCY_ACTIVE: return "EMERGENCY_ACTIVE";
        case FAULT_PROCESS_TIMEOUT: return "PROCESS_TIMEOUT";
        case FAULT_SERVER_COMMUNICATION_ERROR: return "SERVER_COMMUNICATION_ERROR";
        case FAULT_PZEM_ERROR: return "PZEM_ERROR";
        default: return "UNKNOWN_ERROR";
    }
}

void Network::sendTelemetry() {
    if (WiFi.status() != WL_CONNECTED) return;
    
    HTTPClient http;
    http.begin(API_ENDPOINT);
    http.addHeader("Content-Type", "application/json");
    
    // Note: If using ArduinoJson v7, change StaticJsonDocument<1024> to JsonDocument
    StaticJsonDocument<1024> doc;
    
    doc["machine_id"] = MACHINE_ID;
    
    // State machine info
    doc["mode"] = modeToString(stateMachine.getMode());
    doc["process_state"] = stateToString(stateMachine.getState());
    doc["running"] = (stateMachine.getMode() == MODE_AUTO && stateMachine.getState() != STATE_IDLE && stateMachine.getState() != STATE_COMPLETE);
    
    // Process settings
    doc["target_temperature"] = stateMachine.getTargetTemp();
    doc["cool_temperature"] = stateMachine.getCoolTemp();
    doc["hold_time_required"] = stateMachine.getHoldTimeRequired();
    doc["hold_time_elapsed"] = stateMachine.getHoldTimeElapsed();
    
    // Hardware outputs & inputs
    doc["temperature"] = hardware.getTemperature();
    doc["heater"] = hardware.isHeaterOn();
    doc["stirrer"] = hardware.isStirrerOn();
    doc["cooler"] = hardware.isCoolerOn();
    
    doc["voltage"] = hardware.getVoltage();
    doc["current"] = hardware.getCurrent();
    doc["power"] = hardware.getPower();
    doc["energy"] = hardware.getEnergy();
    doc["frequency"] = hardware.getFrequency();
    doc["power_factor"] = hardware.getPowerFactor();
    
    // Faults
    doc["fault"] = (stateMachine.getFaultCode() != FAULT_NONE);
    doc["fault_code"] = faultToString(stateMachine.getFaultCode());
    
    // Command confirmation
    doc["last_command_id"] = stateMachine.getLastCommandId();
    doc["last_command"] = stateMachine.getLastCommand();
    doc["command_status"] = stateMachine.getCommandStatus();
    
    String jsonPayload;
    serializeJson(doc, jsonPayload);
    
    int httpResponseCode = http.POST(jsonPayload);
    
    if (httpResponseCode > 0) {
        String response = http.getString();
        
        StaticJsonDocument<512> responseDoc;
        DeserializationError error = deserializeJson(responseDoc, response);
        
        if (!error && responseDoc["status"] == "success" && !responseDoc["command"].isNull()) {
            JsonObject cmdObj = responseDoc["command"].as<JsonObject>();
            processCommand(cmdObj);
        }
    } else {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
    }
    
    http.end();
}

void Network::processCommand(const JsonDocument& cmdDoc) {
    // Because cmdDoc is a JsonDocument (which acts like an Object for root objects)
    String cmdId = cmdDoc["command_id"] | "";
    String action = cmdDoc["action"] | "";
    
    if (cmdId == stateMachine.getLastCommandId() && cmdId != "") {
        return; // Already executed
    }
    
    String status = "FAILED";
    
    if (action == "AUTO_START") {
        float targetTemp = cmdDoc["target_temperature"] | 72.0;
        unsigned long holdTime = cmdDoc["hold_time"] | 15;
        float coolTemp = cmdDoc["cool_temperature"] | 35.0;
        stateMachine.cmdAutoStart(targetTemp, holdTime, coolTemp);
        status = stateMachine.getCommandStatus();
    } else if (action == "STOP") {
        stateMachine.cmdStop();
        status = stateMachine.getCommandStatus();
    } else if (action == "MANUAL_MODE") {
        stateMachine.cmdManualMode();
        status = stateMachine.getCommandStatus();
    } else if (action == "EMERGENCY_STOP") {
        stateMachine.cmdEmergencyStop();
        status = stateMachine.getCommandStatus();
    } else if (action == "CLEAR_EMERGENCY") {
        stateMachine.cmdClearEmergency();
        status = stateMachine.getCommandStatus();
    } else if (action == "RESET") {
        stateMachine.cmdReset();
        status = stateMachine.getCommandStatus();
    } else if (action == "HEATER_ON") {
        stateMachine.cmdSetHeater(true);
        status = stateMachine.getCommandStatus();
    } else if (action == "HEATER_OFF") {
        stateMachine.cmdSetHeater(false);
        status = stateMachine.getCommandStatus();
    } else if (action == "STIRRER_ON") {
        stateMachine.cmdSetStirrer(true);
        status = stateMachine.getCommandStatus();
    } else if (action == "STIRRER_OFF") {
        stateMachine.cmdSetStirrer(false);
        status = stateMachine.getCommandStatus();
    } else if (action == "COOLER_ON") {
        stateMachine.cmdSetCooler(true);
        status = stateMachine.getCommandStatus();
    } else if (action == "COOLER_OFF") {
        stateMachine.cmdSetCooler(false);
        status = stateMachine.getCommandStatus();
    } else {
        status = "INVALID_COMMAND";
    }
    
    stateMachine.setLastCommand(cmdId, action, status);
}

```

## esp32_controller\Network.h

```h
#ifndef NETWORK_H
#define NETWORK_H

#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

class Network {
public:
    Network();
    void init();
    void update(); // Handle 5s telemetry tick
    
    bool isConnected() const { return WiFi.status() == WL_CONNECTED; }
    
private:
    unsigned long lastTelemetryTime;
    
    void sendTelemetry();
    void processCommand(const JsonDocument& doc);
};

extern Network network;

#endif // NETWORK_H

```

## esp32_controller\StateMachine.cpp

```cpp
#include "StateMachine.h"
#include "Hardware.h"
#include "Config.h"

StateMachine stateMachine;

StateMachine::StateMachine() 
    : currentMode(MODE_IDLE), currentState(STATE_IDLE), faultCode(FAULT_NONE),
      targetTemperature(72.0), coolTemperature(35.0), holdTimeRequired(15),
      stateStartTime(0), holdTimeElapsed(0), lastUpdateTime(0)
{
}

void StateMachine::init() {
    transitionTo(MODE_IDLE, STATE_IDLE);
}

void StateMachine::update() {
    unsigned long now = millis();
    unsigned long delta = now - lastUpdateTime;
    lastUpdateTime = now;
    
    evaluateSafety();
    
    if (currentMode == MODE_AUTO) {
        evaluateAutoSequence();
    }
    
    if (currentState == STATE_HOLDING) {
        // Only count if temperature is above minimum holding threshold (e.g., target - 0.5)
        if (hardware.getTemperature() >= (targetTemperature - 0.5)) {
            // we will approximate seconds by checking delta since last update.
            // Since this runs fast, better to track ms elapsed and add to a ms counter.
            // But for simplicity, we accumulate delta in ms and convert.
            static unsigned long holdMs = 0;
            holdMs += delta;
            if (holdMs >= 1000) {
                holdTimeElapsed += (holdMs / 1000);
                holdMs %= 1000;
            }
        } else {
            // Drop below temp -> back to heating
            transitionTo(MODE_AUTO, STATE_HEATING);
        }
    }
}

void StateMachine::evaluateSafety() {
    if (hardware.isSensorFault() && currentMode != MODE_EMERGENCY) {
        triggerFault(FAULT_TEMP_SENSOR_ERROR);
    }
    
    if (hardware.getTemperature() >= MAX_SAFE_TEMPERATURE && currentMode != MODE_EMERGENCY) {
        triggerFault(FAULT_OVER_TEMPERATURE);
    }
}

void StateMachine::evaluateAutoSequence() {
    float temp = hardware.getTemperature();
    
    switch (currentState) {
        case STATE_HEATING:
            hardware.setStirrer(true);
            hardware.setCooler(false);
            
            // Simple hysteresis
            if (temp >= targetTemperature) {
                hardware.setHeater(false);
                transitionTo(MODE_AUTO, STATE_HOLDING);
            } else if (temp <= (targetTemperature - 1.0)) {
                hardware.setHeater(true);
            }
            break;
            
        case STATE_HOLDING:
            hardware.setStirrer(true);
            hardware.setCooler(false);
            
            // Hysteresis during holding to keep it at target
            if (temp < targetTemperature) {
                 hardware.setHeater(true);
            } else if (temp >= targetTemperature) {
                 hardware.setHeater(false);
            }
            
            if (holdTimeElapsed >= holdTimeRequired) {
                transitionTo(MODE_AUTO, STATE_COOLING);
            }
            break;
            
        case STATE_COOLING:
            hardware.setHeater(false);
            hardware.setStirrer(true);
            hardware.setCooler(true);
            
            if (temp <= coolTemperature) {
                transitionTo(MODE_AUTO, STATE_COMPLETE);
            }
            break;
            
        case STATE_COMPLETE:
            hardware.setHeater(false);
            hardware.setStirrer(false);
            hardware.setCooler(false);
            break;
            
        default:
            break;
    }
}

void StateMachine::transitionTo(ProcessMode newMode, ProcessState newState) {
    currentMode = newMode;
    currentState = newState;
    stateStartTime = millis();
    
    if (newState == STATE_HOLDING) {
        holdTimeElapsed = 0;
    }
    
    if (newState == STATE_IDLE || newState == STATE_COMPLETE || newState == STATE_FAULT || newState == STATE_EMERGENCY) {
        hardware.setHeater(false);
        hardware.setStirrer(false);
        hardware.setCooler(false);
    }
}

void StateMachine::triggerFault(FaultCode code) {
    faultCode = code;
    transitionTo(currentMode, STATE_FAULT);
    hardware.setHeater(false);
    hardware.setStirrer(false);
    hardware.setCooler(false);
}

void StateMachine::setLastCommand(String cmdId, String action, String status) {
    lastCommandId = cmdId;
    lastCommand = action;
    commandStatus = status;
}

// ---- COMMANDS ----

void StateMachine::cmdAutoStart(float targetTemp, unsigned long holdTime, float coolTemp) {
    if (currentMode == MODE_EMERGENCY || currentState == STATE_FAULT || hardware.isSensorFault()) {
        commandStatus = "REJECTED";
        return;
    }
    
    targetTemperature = targetTemp;
    holdTimeRequired = holdTime;
    coolTemperature = coolTemp;
    
    transitionTo(MODE_AUTO, STATE_HEATING);
    commandStatus = "EXECUTED";
}

void StateMachine::cmdStop() {
    transitionTo(MODE_IDLE, STATE_IDLE);
    commandStatus = "EXECUTED";
}

void StateMachine::cmdManualMode() {
    if (currentMode == MODE_EMERGENCY || currentState == STATE_FAULT) {
        commandStatus = "REJECTED";
        return;
    }
    transitionTo(MODE_MANUAL, STATE_MANUAL);
    commandStatus = "EXECUTED";
}

void StateMachine::cmdEmergencyStop() {
    transitionTo(MODE_EMERGENCY, STATE_EMERGENCY);
    faultCode = FAULT_EMERGENCY_ACTIVE;
    commandStatus = "EXECUTED";
}

void StateMachine::cmdClearEmergency() {
    if (currentMode == MODE_EMERGENCY) {
        faultCode = FAULT_NONE;
        transitionTo(MODE_IDLE, STATE_IDLE);
        commandStatus = "EXECUTED";
    } else {
        commandStatus = "REJECTED";
    }
}

void StateMachine::cmdReset() {
    if (currentState == STATE_FAULT) {
        if (!hardware.isSensorFault() && hardware.getTemperature() < MAX_SAFE_TEMPERATURE) {
            faultCode = FAULT_NONE;
            transitionTo(MODE_IDLE, STATE_IDLE);
            commandStatus = "EXECUTED";
        } else {
            commandStatus = "REJECTED"; // Still unsafe
        }
    } else {
        transitionTo(MODE_IDLE, STATE_IDLE);
        commandStatus = "EXECUTED";
    }
}

void StateMachine::cmdSetHeater(bool state) {
    if (currentMode != MODE_MANUAL) {
        commandStatus = "REJECTED";
        return;
    }
    
    // Safety is enforced inside hardware.setHeater, but we also check here for logic
    if (state && (hardware.getTemperature() >= MAX_SAFE_TEMPERATURE || hardware.isSensorFault())) {
        commandStatus = "REJECTED";
    } else {
        hardware.setHeater(state);
        commandStatus = "EXECUTED";
    }
}

void StateMachine::cmdSetStirrer(bool state) {
    if (currentMode != MODE_MANUAL) {
        commandStatus = "REJECTED";
        return;
    }
    hardware.setStirrer(state);
    commandStatus = "EXECUTED";
}

void StateMachine::cmdSetCooler(bool state) {
    if (currentMode != MODE_MANUAL) {
        commandStatus = "REJECTED";
        return;
    }
    hardware.setCooler(state);
    commandStatus = "EXECUTED";
}

```

## esp32_controller\StateMachine.h

```h
#ifndef STATEMACHINE_H
#define STATEMACHINE_H

#include <Arduino.h>

enum ProcessMode {
    MODE_IDLE,
    MODE_AUTO,
    MODE_MANUAL,
    MODE_EMERGENCY
};

enum ProcessState {
    STATE_IDLE,
    STATE_HEATING,
    STATE_HOLDING,
    STATE_COOLING,
    STATE_COMPLETE,
    STATE_MANUAL,
    STATE_EMERGENCY,
    STATE_FAULT
};

enum FaultCode {
    FAULT_NONE,
    FAULT_TEMP_SENSOR_ERROR,
    FAULT_OVER_TEMPERATURE,
    FAULT_INVALID_COMMAND,
    FAULT_EMERGENCY_ACTIVE,
    FAULT_PROCESS_TIMEOUT,
    FAULT_SERVER_COMMUNICATION_ERROR,
    FAULT_PZEM_ERROR
};

class StateMachine {
public:
    StateMachine();
    
    void init();
    void update(); // Called every loop to evaluate state and time
    
    // Commands from Server
    void cmdAutoStart(float targetTemp, unsigned long holdTime, float coolTemp);
    void cmdStop();
    void cmdManualMode();
    void cmdEmergencyStop();
    void cmdClearEmergency();
    void cmdReset();
    void cmdSetHeater(bool state);
    void cmdSetStirrer(bool state);
    void cmdSetCooler(bool state);
    
    // Set last command executed
    void setLastCommand(String cmdId, String action, String status);

    // Getters for telemetry
    ProcessMode getMode() const { return currentMode; }
    ProcessState getState() const { return currentState; }
    FaultCode getFaultCode() const { return faultCode; }
    
    float getTargetTemp() const { return targetTemperature; }
    float getCoolTemp() const { return coolTemperature; }
    unsigned long getHoldTimeRequired() const { return holdTimeRequired; }
    unsigned long getHoldTimeElapsed() const { return holdTimeElapsed; }
    
    String getLastCommandId() const { return lastCommandId; }
    String getLastCommand() const { return lastCommand; }
    String getCommandStatus() const { return commandStatus; }
    
    void triggerFault(FaultCode code);
    
private:
    ProcessMode currentMode;
    ProcessState currentState;
    FaultCode faultCode;
    
    float targetTemperature;
    float coolTemperature;
    unsigned long holdTimeRequired;
    
    unsigned long stateStartTime;
    unsigned long holdTimeElapsed; // In seconds
    unsigned long lastUpdateTime;
    
    String lastCommandId;
    String lastCommand;
    String commandStatus;
    
    void transitionTo(ProcessMode newMode, ProcessState newState);
    void evaluateSafety();
    void evaluateAutoSequence();
};

extern StateMachine stateMachine;

#endif // STATEMACHINE_H

```

## esp32_controller\esp32_controller.ino

```ino
#include <Arduino.h>
#include "Config.h"
#include "Hardware.h"
#include "StateMachine.h"
#include "Network.h"

void setup() {
    Serial.begin(115200);
    delay(1000);
    
    Serial.println("Starting ESP32 Pasteurizer Controller...");
    
    // Initialize components
    hardware.init();
    stateMachine.init();
    network.init();
    
    Serial.println("Initialization complete.");
}

void loop() {
    // 1. Read hardware inputs (sensors, PZEM)
    hardware.update();
    
    // 2. Evaluate State Machine and Safety logic
    stateMachine.update();
    
    // 3. Handle Networking (Telemetry POST and Command receive)
    network.update();
}

```

## gobioai-dashboard\.gitignore

```text
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

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

## gobioai-dashboard\README.md

```md
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

## gobioai-dashboard\package-lock.json

```json
{
  "name": "gobioai-dashboard",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "gobioai-dashboard",
      "version": "0.0.0",
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
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.11.1.tgz",
      "integrity": "sha512-RSvbQmHzdKzNsLYa/wHrbc3KN4sYLKAdPZxqiM2HATqv/SBk2/ENSHpvXGaLOMcsAyz0poEGqkmmKYG3OWiJEQ==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.2.2",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.11.1.tgz",
      "integrity": "sha512-vgj7R3y3Wgx24IQaGPA/R6YFXLHVMOZ0uVEyIQPaWs+rd1AzfEMXlAC22FYwO1XkKR6NPsq7mUandH8oIRdZFw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.2.2.tgz",
      "integrity": "sha512-c95qOXkHdydNKhscBTebqEC1CVAZpyqOfVfBzQ1qgzyl3gfeldUjIggDbIZgDKsHLgnsM+igH7TJ/eAasaVuMA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@napi-rs/wasm-runtime": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/@napi-rs/wasm-runtime/-/wasm-runtime-1.1.6.tgz",
      "integrity": "sha512-ZLv/JdUfkvOy9eCnnBaGfiO+XimbjebAeO+MRQqD/B+FR1tnRN0tpKSJHRbE8sFfS6aqsXZ67TQjfwfsxULVbg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@tybys/wasm-util": "^0.10.3"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/Brooooooklyn"
      },
      "peerDependencies": {
        "@emnapi/core": "^1.7.1",
        "@emnapi/runtime": "^1.7.1"
      }
    },
    "node_modules/@oxc-project/types": {
      "version": "0.139.0",
      "resolved": "https://registry.npmjs.org/@oxc-project/types/-/types-0.139.0.tgz",
      "integrity": "sha512-r9gHphtCs+1M7J0pw6Sn/hh/Wpa/iQrOOkrNAlVLF/gHq+/CJmHIWKKUUhdWjcD6CIa8idarspCsASiXCXvFUw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/Boshen"
      }
    },
    "node_modules/@oxlint/binding-android-arm-eabi": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-android-arm-eabi/-/binding-android-arm-eabi-1.73.0.tgz",
      "integrity": "sha512-HZQRN/UMBu+Ut+/9MiAChkbP4qZqrNOWBcNI45vOT40GVhbGR0JgHB87L48D4iAqFQIdVmeQYtV9RF89AjTKkg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-android-arm64": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-android-arm64/-/binding-android-arm64-1.73.0.tgz",
      "integrity": "sha512-Gp+KJRylv2aW7thRpG5p1KTxZq4ZJFbWowrKzufNq9d3ssl3r3JviYV45/+p+7CN1Nv0zDd1e8Ex0b/HUDq4TQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-darwin-arm64": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-darwin-arm64/-/binding-darwin-arm64-1.73.0.tgz",
      "integrity": "sha512-3de96NdtXhxERMjIz7wsp2HYMY6pMQycGxFWac2mFecAx6VeARF/IqFb1QIaqiCRIdfzBwzTed+pCTCoiS+CYA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-darwin-x64": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-darwin-x64/-/binding-darwin-x64-1.73.0.tgz",
      "integrity": "sha512-5zx/uPW32TiaOeVY1dQ/H5iOf0K1HOdFKOJhLqGl4o63+i1fpzoqqu/mKtd7OFgFjNCdhlyTGgjVkQTZm1ELcg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-freebsd-x64": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-freebsd-x64/-/binding-freebsd-x64-1.73.0.tgz",
      "integrity": "sha512-qNe4gKHaGnLuZJ8toUg90JAa0S2vTVvDw+0bRi3q1avXZXDT4u5mMeECf3nD4HYrbdn1O7dXqWut4onY/yx/Xg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-arm-gnueabihf": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-arm-gnueabihf/-/binding-linux-arm-gnueabihf-1.73.0.tgz",
      "integrity": "sha512-cCehYh5hTbfShm/fxTD6wwrGUWIpvX+N5OxmAMhFhDeTGXvw+BeNj889tpxsFQ9ZLatQ6wImuY8tsKLZ+FMz7w==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-arm-musleabihf": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-arm-musleabihf/-/binding-linux-arm-musleabihf-1.73.0.tgz",
      "integrity": "sha512-d5j5GDU/2dMgjVhw7TQT9ITrsIr1Y02KEXKyVGIXUkD+KiaxE9TP65FS2ZdgTBemQvoRL+gSBdbrIm3cQIeacg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-arm64-gnu": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-arm64-gnu/-/binding-linux-arm64-gnu-1.73.0.tgz",
      "integrity": "sha512-Eyf1SrP3+yR1DI3OJgOY2Pvrr9dWP9TK37xPaDYycwTtlGlI45erJAVIfH5/m/xosDt6BupJYEFi47bvbTuuyw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-arm64-musl": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-arm64-musl/-/binding-linux-arm64-musl-1.73.0.tgz",
      "integrity": "sha512-IlT/OJApEDKaMmCooHuncgJZbbCe7T5QIWmTZBEtYscWvzPQuuEinVcid6kwQRVQOUdb7PUCz4jQHnaYXdfJXw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-ppc64-gnu": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-ppc64-gnu/-/binding-linux-ppc64-gnu-1.73.0.tgz",
      "integrity": "sha512-L+JYcb/vdg5fmcH08V6o0YYLU28cTH1SPNulwJdvK9NK49aXSkYy6oNpKBmddArVOXYqNepriDGiZ04G54kh1Q==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-riscv64-gnu": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-riscv64-gnu/-/binding-linux-riscv64-gnu-1.73.0.tgz",
      "integrity": "sha512-Qtk0g3bKV6OwWjIm7R8kQN1uOZRKQt/MODK2a8QfkwhTpXBD53ozx5XLVWLGDQAVyp2otLW4D2wB98XfAfMPGA==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-riscv64-musl": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-riscv64-musl/-/binding-linux-riscv64-musl-1.73.0.tgz",
      "integrity": "sha512-wX0NQKZVxltkAOVmzFcpOaMpdaUvsq1Eqpx9tkAfl71UdkTlSo1R4AdAnGccR1Fm2+TzFgZ22CyyGuZ41RDr/A==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-s390x-gnu": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-s390x-gnu/-/binding-linux-s390x-gnu-1.73.0.tgz",
      "integrity": "sha512-vPe7UGBMWyiLTtnqS4xxgMQFSFGmtQwhwCxuiw6lXygaO6bVt0D8dFVg8Xv05eaiN3ybC0HXXHUAohFMFvqoCQ==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-x64-gnu": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-x64-gnu/-/binding-linux-x64-gnu-1.73.0.tgz",
      "integrity": "sha512-2CwIWr9cemFC/CbRBWZvuk5mffz6ObmfFkfcC/9rTQ7f+icNhYr2kOjf9Rt8lLvugvkdGDOmkoVoFFHh6ClCTw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-linux-x64-musl": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-linux-x64-musl/-/binding-linux-x64-musl-1.73.0.tgz",
      "integrity": "sha512-nDadfJgg7NBBxG0N560wOe7LLX5QiYp6qBaI7viuk5EUORFBktU/NfV0MbTqU3gTqQDCh4VyxKdo5VADxk9w8Q==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-openharmony-arm64": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-openharmony-arm64/-/binding-openharmony-arm64-1.73.0.tgz",
      "integrity": "sha512-wGjJC+NLH9xP+IKGn9RDW94ojJR/wPbg5WCnQjj/oReaOtCQthr8ws1zICe77JFmo4ouUdeTHHZL/ESGiF6Pmw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-win32-arm64-msvc": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-win32-arm64-msvc/-/binding-win32-arm64-msvc-1.73.0.tgz",
      "integrity": "sha512-I7X47GPGljw225YUQ5SbC/rb1Kkdrd0yQf0x+hYxeKS6DpfjMbo9ccQPQ6LNY6BoJQ1sHhgDUGuMn5Vg5gHT6w==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-win32-ia32-msvc": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-win32-ia32-msvc/-/binding-win32-ia32-msvc-1.73.0.tgz",
      "integrity": "sha512-5lWj+3h+74Fm1jYOO9qkJA4xkAlZA099DkXppuXsk7UpnpZLttsefrZU469vChGaG6hcSqrkKXQOvMTZtbjeNg==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@oxlint/binding-win32-x64-msvc": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/@oxlint/binding-win32-x64-msvc/-/binding-win32-x64-msvc-1.73.0.tgz",
      "integrity": "sha512-WaNRvh4f6zY9CvUQk2YoA1O90ieWrIklI84+HXFr9Isjz9CSESrdqo/RtIYt4Dll/cAchqGDMehfaZd0vqEFZw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@reduxjs/toolkit": {
      "version": "2.12.0",
      "resolved": "https://registry.npmjs.org/@reduxjs/toolkit/-/toolkit-2.12.0.tgz",
      "integrity": "sha512-KiT+RzZbp6mQET+Mg+h2c97+9j1sNflUxQkIHI7Yuzf6Peu+OYpmkn6nbHWmLLWj+1ZODUJFwGZ7gx3L9R9EOw==",
      "license": "MIT",
      "dependencies": {
        "@standard-schema/spec": "^1.0.0",
        "@standard-schema/utils": "^0.3.0",
        "immer": "^11.0.0",
        "redux": "^5.0.1",
        "redux-thunk": "^3.1.0",
        "reselect": "^5.1.0"
      },
      "peerDependencies": {
        "react": "^16.9.0 || ^17.0.0 || ^18 || ^19",
        "react-redux": "^7.2.1 || ^8.1.3 || ^9.0.0"
      },
      "peerDependenciesMeta": {
        "react": {
          "optional": true
        },
        "react-redux": {
          "optional": true
        }
      }
    },
    "node_modules/@rolldown/binding-android-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-android-arm64/-/binding-android-arm64-1.1.5.tgz",
      "integrity": "sha512-lZg8fqIv2v7FF237bwMgzGZEJvGL79/s5knJ/i6FmsGF4XXlzccZ4jb+TrFIxtSSxFtIpdsgrPZeMk1I9AFcyQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-arm64/-/binding-darwin-arm64-1.1.5.tgz",
      "integrity": "sha512-51Bnx9pNiMRKSUNtBfySkNJ9vMU9Hh3I1ozDd6gyPPYzaXCfnptUcEZxXGYFn+ul2dtcMUiqGR1Yai2K10uoTw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-x64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-x64/-/binding-darwin-x64-1.1.5.tgz",
      "integrity": "sha512-Tm+gbfC0aHu1tBA/JvKQh32S0K6YgCHkiAF4/W6xX0K0RmNuc94VeK419dJoE65R5aRxmo+noZQSWrAMF6yb6g==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-freebsd-x64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-freebsd-x64/-/binding-freebsd-x64-1.1.5.tgz",
      "integrity": "sha512-JMzDKCCXq93YccG5gz3hvOs1oXRKAf0XYpfOS88e+wZrC8Iugj6j68867vrYZkvpDDpKn/KoKORThmchMpF6TA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm-gnueabihf": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm-gnueabihf/-/binding-linux-arm-gnueabihf-1.1.5.tgz",
      "integrity": "sha512-uML21j2K5TfPGutKxub+M+nLjZIrWjXQ5Grx4lCe/nimTj9B4L63zHpjXLl4y0L3mcm2htEQIb06oCG/szerNw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-gnu/-/binding-linux-arm64-gnu-1.1.5.tgz",
      "integrity": "sha512-navSiuTMogvnQoZoM/v+l3ZWo50/NTwSHSzheABx/RCnmUPaKwq9qSo4Br2OYRs21+Fz8uFqITZM3H4opOB0/Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-musl": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-musl/-/binding-linux-arm64-musl-1.1.5.tgz",
      "integrity": "sha512-lAryqH7IteztmCXQXk0etKj4wBQ7Gx5S6LjKhsgp9zb8I5bsuvU/2llH1hDQcjsFeqIsovMVN339/8pUDDBXxA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-ppc64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-ppc64-gnu/-/binding-linux-ppc64-gnu-1.1.5.tgz",
      "integrity": "sha512-fsK/sNBnxzBlL4O1JNrZakVQxPspqpED5dLtNsZS9oOKmtSpdNIzxH2kkol5HYTWJN47sE20ztMJPxfZ89qGOg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-s390x-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-s390x-gnu/-/binding-linux-s390x-gnu-1.1.5.tgz",
      "integrity": "sha512-gLYb4BIadlfTOYT5gO503n8zQjXflgzpD0FcyKh0Mzx3rqCZKnHoJWV9xe1KXUJ5lx2JfcSHr/mhzS0PC/McAA==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-gnu/-/binding-linux-x64-gnu-1.1.5.tgz",
      "integrity": "sha512-FjcpEKUyJygHgs1o50VYNvkt5+7Le/VEdYt0AkRpkL33MnyQfwr8l5mXwMmfmTbyMPr5vJLC+8/Gd9gXnwU1QQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-musl": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-musl/-/binding-linux-x64-musl-1.1.5.tgz",
      "integrity": "sha512-Me+PfPI2TMeOQk0gYWfLQZtTktrmzbr8cDboqX83XKc7UrgAi55gF+2dUkWdxd19n55Essp2yeca+O9N5rBxHg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-openharmony-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-openharmony-arm64/-/binding-openharmony-arm64-1.1.5.tgz",
      "integrity": "sha512-yc5WrLzXks6zCQfn9Oxr8pORKyl/pF+QjHmW/Qx3qu0oyrrNC+y2JLTU1E2rcWYAmzlnqngWXHQjy51VzW70Vw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-wasm32-wasi": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-wasm32-wasi/-/binding-wasm32-wasi-1.1.5.tgz",
      "integrity": "sha512-VbQGPX2b4r48TAMIM2cjgluIM1HYutm4pcTEJsle7iEP7sB1dFqtPLBVbdLAZCxy1txCcPxf4QFf4v8uvltPqA==",
      "cpu": [
        "wasm32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "1.11.1",
        "@emnapi/runtime": "1.11.1",
        "@napi-rs/wasm-runtime": "^1.1.6"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-arm64-msvc": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-arm64-msvc/-/binding-win32-arm64-msvc-1.1.5.tgz",
      "integrity": "sha512-gHv82k63z4qpV5+Q1y/12KrK0ltWBukVDI8nZcbT7Tt/ZlOIVwppazneq0F93oDxTo3IgAMEDIoQh3E2n6mVsw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-x64-msvc": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-x64-msvc/-/binding-win32-x64-msvc-1.1.5.tgz",
      "integrity": "sha512-tTZuDBPw85tEN5PQi1pnEBzDy0Z49HtScLAbD5t6hyeU92A95pRWaSMw1GZZi/RwgSgUIl0xrSlXIT/9QzvYSA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.1.tgz",
      "integrity": "sha512-2j9bGt5Jh8hj+vPtgzPtl72j0yRxHAyumoo6TNfAjsLB04UtpSvPbPcDcBMxz7n+9CYB0c1GxQFxYRg2jimqGw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@standard-schema/spec": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@standard-schema/spec/-/spec-1.1.0.tgz",
      "integrity": "sha512-l2aFy5jALhniG5HgqrD6jXLi/rUWrKvqN/qJx6yoJsgKhblVd+iqqU4RCXavm/jPityDo5TCvKMnpjKnOriy0w==",
      "license": "MIT"
    },
    "node_modules/@standard-schema/utils": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/@standard-schema/utils/-/utils-0.3.0.tgz",
      "integrity": "sha512-e7Mew686owMaPJVNNLs55PUvgz371nKgwsc4vxE49zsODpJEnxgxRo2y/OKrqueavXgZNMDVj3DdHFlaSAeU8g==",
      "license": "MIT"
    },
    "node_modules/@tailwindcss/node": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/node/-/node-4.3.2.tgz",
      "integrity": "sha512-yWP/sqEcBLaD8JuA6zNwxoYKr75qxTioYwlRwekj5Jr/I5GXnoJfjetH/psLUIv74cYTH2lBUEzBkinthoYcBg==",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/remapping": "^2.3.5",
        "enhanced-resolve": "5.21.6",
        "jiti": "^2.7.0",
        "lightningcss": "1.32.0",
        "magic-string": "^0.30.21",
        "source-map-js": "^1.2.1",
        "tailwindcss": "4.3.2"
      }
    },
    "node_modules/@tailwindcss/oxide": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide/-/oxide-4.3.2.tgz",
      "integrity": "sha512-z8ZgnzX8gdNoWLBLqBPoh/sjnxkwvf9ZuWjnO0l0yIzbLa5/9S+eC5QxGZKRobVHIC3/1BoMWjHblqWjcgFgag==",
      "license": "MIT",
      "engines": {
        "node": ">= 20"
      },
      "optionalDependencies": {
        "@tailwindcss/oxide-android-arm64": "4.3.2",
        "@tailwindcss/oxide-darwin-arm64": "4.3.2",
        "@tailwindcss/oxide-darwin-x64": "4.3.2",
        "@tailwindcss/oxide-freebsd-x64": "4.3.2",
        "@tailwindcss/oxide-linux-arm-gnueabihf": "4.3.2",
        "@tailwindcss/oxide-linux-arm64-gnu": "4.3.2",
        "@tailwindcss/oxide-linux-arm64-musl": "4.3.2",
        "@tailwindcss/oxide-linux-x64-gnu": "4.3.2",
        "@tailwindcss/oxide-linux-x64-musl": "4.3.2",
        "@tailwindcss/oxide-wasm32-wasi": "4.3.2",
        "@tailwindcss/oxide-win32-arm64-msvc": "4.3.2",
        "@tailwindcss/oxide-win32-x64-msvc": "4.3.2"
      }
    },
    "node_modules/@tailwindcss/oxide-android-arm64": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-android-arm64/-/oxide-android-arm64-4.3.2.tgz",
      "integrity": "sha512-WHxqIuHpvZ5VtdX6GTl1Ik/Vp2YuN42Et+0CdeaVd/frQ9jAvGmvR8vLT+jk3e8/Q3x8kECB9+R17pgpp2BulA==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-darwin-arm64": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-arm64/-/oxide-darwin-arm64-4.3.2.tgz",
      "integrity": "sha512-GZypeUY/IDJW3877KeM+O67vbXr3MBnbtEL4aYhNErv/JWZhye2vGSWWG9tB6iiqR2MqRNkY8IOUy4NdSZV26w==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-darwin-x64": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-x64/-/oxide-darwin-x64-4.3.2.tgz",
      "integrity": "sha512-UIIzmefR6KO1sDU7MzRqAxC8iBpft/VhkGjTjnhoS6k7Z3rQ9wEgA1ODSiyH/tcSYssulNm4Ci3hOeK1jH7ccQ==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-freebsd-x64": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-freebsd-x64/-/oxide-freebsd-x64-4.3.2.tgz",
      "integrity": "sha512-GN+uAmcI6DNspnCDwtOAZrTz6oukJnp337qZvxqCGLd3BHBzJpO0ZbTLRvJNdztOeAmTzewewGIMPb0tk2R4WA==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm-gnueabihf": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm-gnueabihf/-/oxide-linux-arm-gnueabihf-4.3.2.tgz",
      "integrity": "sha512-4ABn7qSbdHRwTiDiuWNegCyb5+2FJ4vKIKc3DmKrvAFw7MU1Lm11dIkTPwUaFdTzc7IsOpDbqBrlh0x6y36U/w==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm64-gnu": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-gnu/-/oxide-linux-arm64-gnu-4.3.2.tgz",
      "integrity": "sha512-wDgEIGwoM8w8pufh9LVt1PahDgNdKXrLC2qfAnV3vAmococ9RWbxeAw4pxPttd/TsJfwjyLf90Dg1y9y8I6Emw==",
      "cpu": [
        "arm64"
      ],
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-arm64-musl": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-musl/-/oxide-linux-arm64-musl-4.3.2.tgz",
      "integrity": "sha512-J5Nuk0uZQIiMTJj3LEx4sAA9tMFUoXQZFv1J6An+QGYe53HKRJuFDi0rpq/tuouCZeAbOBY3kQ6g8qeD4TUjtA==",
      "cpu": [
        "arm64"
      ],
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-x64-gnu": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-gnu/-/oxide-linux-x64-gnu-4.3.2.tgz",
      "integrity": "sha512-kqCZpSKOBEJO4mz7OqWoofBZeXTAwaVGPj0ErAj7CojmhKpWVWVOnrt9dE8odoIraZq4oj3ausM37kXi+Tow8w==",
      "cpu": [
        "x64"
      ],
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-linux-x64-musl": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-musl/-/oxide-linux-x64-musl-4.3.2.tgz",
      "integrity": "sha512-cixpqbh2toJDmkuCRI68nXA8ZxNmdK9Y+9v5h3MC3ZQKy/0BO8AWzlkWyRM7JAFSGBlfig4YVTPsK6MVgqz1uw==",
      "cpu": [
        "x64"
      ],
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-wasm32-wasi": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-wasm32-wasi/-/oxide-wasm32-wasi-4.3.2.tgz",
      "integrity": "sha512-4ec2Z/LOmRsAgU23CS4xeJfcJlmRg94A/XrbGRCF1gyU/zdDfRLYDVsS+ynSZCmGNxQ1jQriQOKMQeQxBA3Isw==",
      "bundleDependencies": [
        "@napi-rs/wasm-runtime",
        "@emnapi/core",
        "@emnapi/runtime",
        "@tybys/wasm-util",
        "@emnapi/wasi-threads",
        "tslib"
      ],
      "cpu": [
        "wasm32"
      ],
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "^1.11.1",
        "@emnapi/runtime": "^1.11.1",
        "@emnapi/wasi-threads": "^1.2.2",
        "@napi-rs/wasm-runtime": "^1.1.4",
        "@tybys/wasm-util": "^0.10.2",
        "tslib": "^2.8.1"
      },
      "engines": {
        "node": ">=14.0.0"
      }
    },
    "node_modules/@tailwindcss/oxide-win32-arm64-msvc": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-arm64-msvc/-/oxide-win32-arm64-msvc-4.3.2.tgz",
      "integrity": "sha512-Zyr/M0+XcYZu3bZrUytc7TXvrk0ftWfl8gN2MwekNDzhqhKRUucMPSeOzM0o0wH5AWOU49BsKRrfKxI2atCPMQ==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/oxide-win32-x64-msvc": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-x64-msvc/-/oxide-win32-x64-msvc-4.3.2.tgz",
      "integrity": "sha512-QI9BO7KlNZsp2GuO0jwAAj5jCDABOKXRkCk2XuKTSaNEFSdfzqswYVTtCHBNKHLsqyjFyFkqlDiwkNbTYSssMQ==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 20"
      }
    },
    "node_modules/@tailwindcss/postcss": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/@tailwindcss/postcss/-/postcss-4.3.2.tgz",
      "integrity": "sha512-rjVWYCa7Ngbi5AarT6k8TkxUG3Wl1QKzHdIZVsjZSzf36Jmo2IKZt/NHRAwly8oDkbBOH0YTu+CHuf9jPxMc+g==",
      "license": "MIT",
      "dependencies": {
        "@alloc/quick-lru": "^5.2.0",
        "@tailwindcss/node": "4.3.2",
        "@tailwindcss/oxide": "4.3.2",
        "postcss": "^8.5.15",
        "tailwindcss": "4.3.2"
      }
    },
    "node_modules/@tybys/wasm-util": {
      "version": "0.10.3",
      "resolved": "https://registry.npmjs.org/@tybys/wasm-util/-/wasm-util-0.10.3.tgz",
      "integrity": "sha512-F3fo1MYrRJYL3zER0OUOmkutjr1Vp23m7OsSgp7nq4SP6OqX6C/56XFIPAl5bt3zaBRjmW7SGz3u/6LwFpYcOg==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@types/d3-array": {
      "version": "3.2.2",
      "resolved": "https://registry.npmjs.org/@types/d3-array/-/d3-array-3.2.2.tgz",
      "integrity": "sha512-hOLWVbm7uRza0BYXpIIW5pxfrKe0W+D5lrFiAEYR+pb6w3N2SwSMaJbXdUfSEv+dT4MfHBLtn5js0LAWaO6otw==",
      "license": "MIT"
    },
    "node_modules/@types/d3-color": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/@types/d3-color/-/d3-color-3.1.3.tgz",
      "integrity": "sha512-iO90scth9WAbmgv7ogoq57O9YpKmFBbmoEoCHDB2xMBY0+/KVrqAaCDyCE16dUspeOvIxFFRI+0sEtqDqy2b4A==",
      "license": "MIT"
    },
    "node_modules/@types/d3-ease": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-ease/-/d3-ease-3.0.2.tgz",
      "integrity": "sha512-NcV1JjO5oDzoK26oMzbILE6HW7uVXOHLQvHshBUW4UMdZGfiY6v5BeQwh9a9tCzv+CeefZQHJt5SRgK154RtiA==",
      "license": "MIT"
    },
    "node_modules/@types/d3-interpolate": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-3.0.4.tgz",
      "integrity": "sha512-mgLPETlrpVV1YRJIglr4Ez47g7Yxjl1lj7YKsiMCb27VJH9W8NVM6Bb9d8kkpG/uAQS5AmbA48q2IAolKKo1MA==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-color": "*"
      }
    },
    "node_modules/@types/d3-path": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/@types/d3-path/-/d3-path-3.1.1.tgz",
      "integrity": "sha512-VMZBYyQvbGmWyWVea0EHs/BwLgxc+MKi1zLDCONksozI4YJMcTt8ZEuIR4Sb1MMTE8MMW49v0IwI5+b7RmfWlg==",
      "license": "MIT"
    },
    "node_modules/@types/d3-scale": {
      "version": "4.0.9",
      "resolved": "https://registry.npmjs.org/@types/d3-scale/-/d3-scale-4.0.9.tgz",
      "integrity": "sha512-dLmtwB8zkAeO/juAMfnV+sItKjlsw2lKdZVVy6LRr0cBmegxSABiLEpGVmSJJ8O08i4+sGR6qQtb6WtuwJdvVw==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-time": "*"
      }
    },
    "node_modules/@types/d3-shape": {
      "version": "3.1.8",
      "resolved": "https://registry.npmjs.org/@types/d3-shape/-/d3-shape-3.1.8.tgz",
      "integrity": "sha512-lae0iWfcDeR7qt7rA88BNiqdvPS5pFVPpo5OfjElwNaT2yyekbM0C9vK+yqBqEmHr6lDkRnYNoTBYlAgJa7a4w==",
      "license": "MIT",
      "dependencies": {
        "@types/d3-path": "*"
      }
    },
    "node_modules/@types/d3-time": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/@types/d3-time/-/d3-time-3.0.4.tgz",
      "integrity": "sha512-yuzZug1nkAAaBlBBikKZTgzCeA+k1uy4ZFwWANOfKw5z5LRhV0gNA7gNkKm7HoK+HRN0wX3EkxGk0fpbWhmB7g==",
      "license": "MIT"
    },
    "node_modules/@types/d3-timer": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/@types/d3-timer/-/d3-timer-3.0.2.tgz",
      "integrity": "sha512-Ps3T8E8dZDam6fUyNiMkekK3XUsaUEik+idO9/YjPtfj2qruF8tFBXS7XhtE4iIXBLxhmLjP3SXpLhVf21I9Lw==",
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "19.2.17",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.17.tgz",
      "integrity": "sha512-MXfmqaVPEVgkBT/aY0aGCkRWWtByiYQXo3xdQ8r5RzuFrPiRn8Gar2tQdXSUQ2GKV3bkXckek89V8wQBY2Q/Aw==",
      "devOptional": true,
      "license": "MIT",
      "dependencies": {
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "19.2.3",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-19.2.3.tgz",
      "integrity": "sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^19.2.0"
      }
    },
    "node_modules/@types/use-sync-external-store": {
      "version": "0.0.6",
      "resolved": "https://registry.npmjs.org/@types/use-sync-external-store/-/use-sync-external-store-0.0.6.tgz",
      "integrity": "sha512-zFDAD+tlpf2r4asuHEj0XH6pY6i0g5NeAHPn+15wk3BV6JA69eERFXC1gyGThDkVa1zCyKr5jox1+2LbV/AMLg==",
      "license": "MIT"
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-6.0.3.tgz",
      "integrity": "sha512-vmFvco5/QuC2f9Oj+wTk0+9XeDFkHxSamwZKYc7MxYwKICfvUvlMhqKI0VuICPltGqh1neqBKDvO4kes1ya8vg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rolldown/pluginutils": "^1.0.1"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "peerDependencies": {
        "@rolldown/plugin-babel": "^0.1.7 || ^0.2.0",
        "babel-plugin-react-compiler": "^1.0.0",
        "vite": "^8.0.0"
      },
      "peerDependenciesMeta": {
        "@rolldown/plugin-babel": {
          "optional": true
        },
        "babel-plugin-react-compiler": {
          "optional": true
        }
      }
    },
    "node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/autoprefixer": {
      "version": "10.5.2",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.5.2.tgz",
      "integrity": "sha512-rD5t5DwOjJdmSORcTq64j8MawTC+tbQ+HHqjR4NDumamy/ambn1UJrlKL+KdwujWxMkFjPM3pPHOEA9tl4767Q==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/autoprefixer"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "browserslist": "^4.28.4",
        "caniuse-lite": "^1.0.30001799",
        "fraction.js": "^5.3.4",
        "picocolors": "^1.1.1",
        "postcss-value-parser": "^4.2.0"
      },
      "bin": {
        "autoprefixer": "bin/autoprefixer"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      },
      "peerDependencies": {
        "postcss": "^8.1.0"
      }
    },
    "node_modules/axios": {
      "version": "1.18.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.18.1.tgz",
      "integrity": "sha512-3nTvFlvpn9Zu/RkHUqtc7/+al4UpRW5az71ap5zccp6e8RAYEzhMTecX8Dz1wWDYrPpUoB1HAQEGEAEvUr7S9g==",
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.16.0",
        "form-data": "^4.0.5",
        "https-proxy-agent": "^5.0.1",
        "proxy-from-env": "^2.1.0"
      }
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.10.42",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.42.tgz",
      "integrity": "sha512-c/jurFrDLyui7o1J86yLkRu4LMsTYcBohveus7/I2Hzdn9KIP2bdJPTue/lR1KH46enoPbD77GKeSYNdyPoD3Q==",
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.cjs"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/browserslist": {
      "version": "4.28.5",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.5.tgz",
      "integrity": "sha512-Cu2E6QejHWzuDMTkuwgpABFgDfZrXLQq5V13YOACZx4mFAG4IwGTbTfHPMr4WtxlHoXSM8FIuRwYYCz5XiabaQ==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "baseline-browser-mapping": "^2.10.42",
        "caniuse-lite": "^1.0.30001800",
        "electron-to-chromium": "^1.5.387",
        "node-releases": "^2.0.50",
        "update-browserslist-db": "^1.2.3"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001803",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001803.tgz",
      "integrity": "sha512-g/uHREV2ZpK9qMalCsWaxmA6ol+DX8GYhuf3T40RKoP+oL7vhRJh8LNt73PCjpnR6l14FzfPrB5Yux4PKm2meg==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/clsx": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/clsx/-/clsx-2.1.1.tgz",
      "integrity": "sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/cookie": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-1.1.1.tgz",
      "integrity": "sha512-ei8Aos7ja0weRpFzJnEA9UHJ/7XQmqglbRwnf2ATjcB9Wq874VKH9kfjjirM6UhU2/E5fFYadylyhFldcqSidQ==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "devOptional": true,
      "license": "MIT"
    },
    "node_modules/d3-array": {
      "version": "3.2.4",
      "resolved": "https://registry.npmjs.org/d3-array/-/d3-array-3.2.4.tgz",
      "integrity": "sha512-tdQAmyA18i4J7wprpYq8ClcxZy3SC31QMeByyCFyRt7BVHdREQZ5lpzoe5mFEYZUWe+oq8HBvk9JjpibyEV4Jg==",
      "license": "ISC",
      "dependencies": {
        "internmap": "1 - 2"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-color": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-color/-/d3-color-3.1.0.tgz",
      "integrity": "sha512-zg/chbXyeBtMQ1LbD/WSoW2DpC3I0mpmPdW+ynRTj/x2DAWYrIY7qeZIHidozwV24m4iavr15lNwIwLxRmOxhA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-ease": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-ease/-/d3-ease-3.0.1.tgz",
      "integrity": "sha512-wR/XK3D3XcLIZwpbvQwQ5fK+8Ykds1ip7A2Txe0yxncXSdq1L9skcG7blcedkOX+ZcgxGAmLX1FrRGbADwzi0w==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-format": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/d3-format/-/d3-format-3.1.2.tgz",
      "integrity": "sha512-AJDdYOdnyRDV5b6ArilzCPPwc1ejkHcoyFarqlPqT7zRYjhavcT3uSrqcMvsgh2CgoPbK3RCwyHaVyxYcP2Arg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-interpolate": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-interpolate/-/d3-interpolate-3.0.1.tgz",
      "integrity": "sha512-3bYs1rOD33uo8aqJfKP3JWPAibgw8Zm2+L9vBKEHJ2Rg+viTR7o5Mmv5mZcieN+FRYaAOWX5SJATX6k1PWz72g==",
      "license": "ISC",
      "dependencies": {
        "d3-color": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-path": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-path/-/d3-path-3.1.0.tgz",
      "integrity": "sha512-p3KP5HCf/bvjBSSKuXid6Zqijx7wIfNW+J/maPs+iwR35at5JCbLUT0LzF1cnjbCHWhqzQTIN2Jpe8pRebIEFQ==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-scale": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/d3-scale/-/d3-scale-4.0.2.tgz",
      "integrity": "sha512-GZW464g1SH7ag3Y7hXjf8RoUuAFIqklOAq3MRl4OaWabTFJY9PN/E1YklhXLh+OQ3fM9yS2nOkCoS+WLZ6kvxQ==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2.10.0 - 3",
        "d3-format": "1 - 3",
        "d3-interpolate": "1.2.0 - 3",
        "d3-time": "2.1.1 - 3",
        "d3-time-format": "2 - 4"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-shape": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/d3-shape/-/d3-shape-3.2.0.tgz",
      "integrity": "sha512-SaLBuwGm3MOViRq2ABk3eLoxwZELpH6zhl3FbAoJ7Vm1gofKx6El1Ib5z23NUEhF9AsGl7y+dzLe5Cw2AArGTA==",
      "license": "ISC",
      "dependencies": {
        "d3-path": "^3.1.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/d3-time/-/d3-time-3.1.0.tgz",
      "integrity": "sha512-VqKjzBLejbSMT4IgbmVgDjpkYrNWUYJnbCGo874u7MMKIWsILRX+OpX/gTk8MqjpT1A/c6HY2dCA77ZN0lkQ2Q==",
      "license": "ISC",
      "dependencies": {
        "d3-array": "2 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-time-format": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/d3-time-format/-/d3-time-format-4.1.0.tgz",
      "integrity": "sha512-dJxPBlzC7NugB2PDLwo9Q8JiTR3M3e4/XANkreKSUxF8vvXKqm1Yfq4Q5dl8budlunRVlUUaDUgFt7eA8D6NLg==",
      "license": "ISC",
      "dependencies": {
        "d3-time": "1 - 3"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/d3-timer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/d3-timer/-/d3-timer-3.0.1.tgz",
      "integrity": "sha512-ndfJ/JxxMd3nw31uyKoY2naivF+r29V+Lc0svZxe1JvvIRmi8hUsrMvdOwgS1o6uBHmiz91geQ0ylPP0aj1VUA==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/decimal.js-light": {
      "version": "2.5.1",
      "resolved": "https://registry.npmjs.org/decimal.js-light/-/decimal.js-light-2.5.1.tgz",
      "integrity": "sha512-qIMFpTMZmny+MMIitAB6D7iVPEorVw6YQRWkvarTkT4tBeSLLiHzcwj6q0MmYSFCiVpiqPJTJEYIrpcPzVEIvg==",
      "license": "MIT"
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/detect-libc": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
      "integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
      "license": "Apache-2.0",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.389",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.389.tgz",
      "integrity": "sha512-cEto7aeOqBfU1D+c5py5pE+ooscKE75JifxLBdFUZsqAxRS6y7kebtxAZvICszSl05gPjYHDTjY+lXpyGvpJbg==",
      "license": "ISC"
    },
    "node_modules/enhanced-resolve": {
      "version": "5.21.6",
      "resolved": "https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.21.6.tgz",
      "integrity": "sha512-aNnGCvbJ/RIyWo1IuhNdVjnNF+EjH9wpzpNHt+ci/m9He9LJvUN8wrCcXjp9cWsGNAuvSpVFTx/vraAFQ8qGjQ==",
      "license": "MIT",
      "dependencies": {
        "graceful-fs": "^4.2.4",
        "tapable": "^2.3.3"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.2.tgz",
      "integrity": "sha512-HWcBoN6NileqtSydK2FqHbS/LoDd2pqrnQHLyJzBj4kOp/ky2MWMN694xOfkK8/SnUsW2DH7EfyVlydKCsm1Zw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-toolkit": {
      "version": "1.49.0",
      "resolved": "https://registry.npmjs.org/es-toolkit/-/es-toolkit-1.49.0.tgz",
      "integrity": "sha512-G5iZ6Pc/FNRY/soKZHC+TxGDD83rHUDXxzaWhGCX44vAv/tMs56WMusnm/KMNK+luUPsgA9U28cGr4RDlSzL2g==",
      "license": "MIT",
      "workspaces": [
        "docs",
        "benchmarks"
      ]
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/eventemitter3": {
      "version": "5.0.4",
      "resolved": "https://registry.npmjs.org/eventemitter3/-/eventemitter3-5.0.4.tgz",
      "integrity": "sha512-mlsTRyGaPBjPedk6Bvw+aqbsXDtoAyAzm5MO7JgU+yVRyMQ5O8bD4Kcci7BS85f93veegeCPkL8R4GLClnjLFw==",
      "license": "MIT"
    },
    "node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.16.0",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.16.0.tgz",
      "integrity": "sha512-y5rN/uOsadFT/JfYwhxRS5R7Qce+g3zG97+JrtFZlC9klX/W5hD7iiLzScI4nZqUS7DNUdhPgw4xI8W2LuXlUw==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/form-data": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.6.tgz",
      "integrity": "sha512-vKatAh4SlVfgbv+YtmhiRjhEMJsYpsG1Y2rMQtR+SVSbytsSD1YGzDIcrAJmdFec88u/+VoGmxnl+80gL1tRCQ==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.4",
        "mime-types": "^2.1.35"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fraction.js": {
      "version": "5.3.4",
      "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-5.3.4.tgz",
      "integrity": "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ==",
      "license": "MIT",
      "engines": {
        "node": "*"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/rawify"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/graceful-fs": {
      "version": "4.2.11",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
      "integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
      "license": "ISC"
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz",
      "integrity": "sha512-T2UbfbBEF32wiepXIsMlTW9+dDYC6wMh/t/vYA4tuOMKqWz/n3vr1NFSxQiyP+zk2mXsoMA/i/7qV6LKut1t1A==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/https-proxy-agent": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz",
      "integrity": "sha512-dFcAjpTQFgoLMzC2VwU+C/CbS7uRL0lWmxDITmqm7C+7F0Odmj6s9l6alZc6AELXhrnggM2CeWSXHGOdX2YtwA==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/immer": {
      "version": "11.1.11",
      "resolved": "https://registry.npmjs.org/immer/-/immer-11.1.11.tgz",
      "integrity": "sha512-qzXuyXAkPySAGYkfsAwodDPWT8Zm7/Uo5BNt4BjhMhG5WlWyZZ4wQqnWwdS8kjlQ1Cwu6gjw3A6+0gTQwlyYtw==",
      "license": "MIT",
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/immer"
      }
    },
    "node_modules/internmap": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/internmap/-/internmap-2.0.3.tgz",
      "integrity": "sha512-5Hh7Y1wQbvY5ooGgPbDaL5iYLAPzMTUrjMulskHLH6wnv/A+1q5rgEaiuqEjB+oxGXIVZs1FF+R/KPN3ZSQYYg==",
      "license": "ISC",
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/jiti": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/jiti/-/jiti-2.7.0.tgz",
      "integrity": "sha512-AC/7JofJvZGrrneWNaEnJeOLUx+JlGt7tNa0wZiRPT4MY1wmfKjt2+6O2p2uz2+skll8OZZmJMNqeke7kKbNgQ==",
      "license": "MIT",
      "bin": {
        "jiti": "lib/jiti-cli.mjs"
      }
    },
    "node_modules/lightningcss": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss/-/lightningcss-1.32.0.tgz",
      "integrity": "sha512-NXYBzinNrblfraPGyrbPoD19C1h9lfI/1mzgWYvXUTe414Gz/X1FD2XBZSZM7rRTrMA8JL3OtAaGifrIKhQ5yQ==",
      "license": "MPL-2.0",
      "dependencies": {
        "detect-libc": "^2.0.3"
      },
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      },
      "optionalDependencies": {
        "lightningcss-android-arm64": "1.32.0",
        "lightningcss-darwin-arm64": "1.32.0",
        "lightningcss-darwin-x64": "1.32.0",
        "lightningcss-freebsd-x64": "1.32.0",
        "lightningcss-linux-arm-gnueabihf": "1.32.0",
        "lightningcss-linux-arm64-gnu": "1.32.0",
        "lightningcss-linux-arm64-musl": "1.32.0",
        "lightningcss-linux-x64-gnu": "1.32.0",
        "lightningcss-linux-x64-musl": "1.32.0",
        "lightningcss-win32-arm64-msvc": "1.32.0",
        "lightningcss-win32-x64-msvc": "1.32.0"
      }
    },
    "node_modules/lightningcss-android-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-android-arm64/-/lightningcss-android-arm64-1.32.0.tgz",
      "integrity": "sha512-YK7/ClTt4kAK0vo6w3X+Pnm0D2cf2vPHbhOXdoNti1Ga0al1P4TBZhwjATvjNwLEBCnKvjJc2jQgHXH0NEwlAg==",
      "cpu": [
        "arm64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-arm64/-/lightningcss-darwin-arm64-1.32.0.tgz",
      "integrity": "sha512-RzeG9Ju5bag2Bv1/lwlVJvBE3q6TtXskdZLLCyfg5pt+HLz9BqlICO7LZM7VHNTTn/5PRhHFBSjk5lc4cmscPQ==",
      "cpu": [
        "arm64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-x64/-/lightningcss-darwin-x64-1.32.0.tgz",
      "integrity": "sha512-U+QsBp2m/s2wqpUYT/6wnlagdZbtZdndSmut/NJqlCcMLTWp5muCrID+K5UJ6jqD2BFshejCYXniPDbNh73V8w==",
      "cpu": [
        "x64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-freebsd-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-freebsd-x64/-/lightningcss-freebsd-x64-1.32.0.tgz",
      "integrity": "sha512-JCTigedEksZk3tHTTthnMdVfGf61Fky8Ji2E4YjUTEQX14xiy/lTzXnu1vwiZe3bYe0q+SpsSH/CTeDXK6WHig==",
      "cpu": [
        "x64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm-gnueabihf": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm-gnueabihf/-/lightningcss-linux-arm-gnueabihf-1.32.0.tgz",
      "integrity": "sha512-x6rnnpRa2GL0zQOkt6rts3YDPzduLpWvwAF6EMhXFVZXD4tPrBkEFqzGowzCsIWsPjqSK+tyNEODUBXeeVHSkw==",
      "cpu": [
        "arm"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-gnu/-/lightningcss-linux-arm64-gnu-1.32.0.tgz",
      "integrity": "sha512-0nnMyoyOLRJXfbMOilaSRcLH3Jw5z9HDNGfT/gwCPgaDjnx0i8w7vBzFLFR1f6CMLKF8gVbebmkUN3fa/kQJpQ==",
      "cpu": [
        "arm64"
      ],
      "libc": [
        "glibc"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-musl/-/lightningcss-linux-arm64-musl-1.32.0.tgz",
      "integrity": "sha512-UpQkoenr4UJEzgVIYpI80lDFvRmPVg6oqboNHfoH4CQIfNA+HOrZ7Mo7KZP02dC6LjghPQJeBsvXhJod/wnIBg==",
      "cpu": [
        "arm64"
      ],
      "libc": [
        "musl"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-gnu/-/lightningcss-linux-x64-gnu-1.32.0.tgz",
      "integrity": "sha512-V7Qr52IhZmdKPVr+Vtw8o+WLsQJYCTd8loIfpDaMRWGUZfBOYEJeyJIkqGIDMZPwPx24pUMfwSxxI8phr/MbOA==",
      "cpu": [
        "x64"
      ],
      "libc": [
        "glibc"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-musl/-/lightningcss-linux-x64-musl-1.32.0.tgz",
      "integrity": "sha512-bYcLp+Vb0awsiXg/80uCRezCYHNg1/l3mt0gzHnWV9XP1W5sKa5/TCdGWaR/zBM2PeF/HbsQv/j2URNOiVuxWg==",
      "cpu": [
        "x64"
      ],
      "libc": [
        "musl"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-arm64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-arm64-msvc/-/lightningcss-win32-arm64-msvc-1.32.0.tgz",
      "integrity": "sha512-8SbC8BR40pS6baCM8sbtYDSwEVQd4JlFTOlaD3gWGHfThTcABnNDBda6eTZeqbofalIJhFx0qKzgHJmcPTnGdw==",
      "cpu": [
        "arm64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-x64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-x64-msvc/-/lightningcss-win32-x64-msvc-1.32.0.tgz",
      "integrity": "sha512-Amq9B/SoZYdDi1kFrojnoqPLxYhQ4Wo5XiL8EVJrVsB8ARoC1PWW6VGtT0WKCemjy8aC+louJnjS7U18x3b06Q==",
      "cpu": [
        "x64"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lucide-react": {
      "version": "1.24.0",
      "resolved": "https://registry.npmjs.org/lucide-react/-/lucide-react-1.24.0.tgz",
      "integrity": "sha512-YT6mBD8lGKkg4nM39enlm94/sfJIiW0YKUT60fBy4YK8tai31ylg1VhGNWxkpSKHo9UagfnZqwIff3HTDQwXeA==",
      "license": "ISC",
      "peerDependencies": {
        "react": "^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/magic-string": {
      "version": "0.30.21",
      "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.21.tgz",
      "integrity": "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==",
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.5"
      }
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/nanoid": {
      "version": "3.3.15",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.15.tgz",
      "integrity": "sha512-y7Wygv/7mEOvxTuEQDB8StXdMRBWf1kR/tlhAzBRUFkB2jfcLOAxO/SHmOO2zgz1pVgK29/kyupn059/bCHdjA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/node-releases": {
      "version": "2.0.51",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.51.tgz",
      "integrity": "sha512-wRNIrw4DmVLKQlbgOMdkMx27Wrpzes2hh5Jtbi2bjPd+4wJstWIqP5A+lscnqbm0xxmT5Bpg8Lec5ItEBwx6BQ==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/oxlint": {
      "version": "1.73.0",
      "resolved": "https://registry.npmjs.org/oxlint/-/oxlint-1.73.0.tgz",
      "integrity": "sha512-u91G9TJzU6yqKWNZUYprQB07W7YvntZXaRxQ6CkoytepYhLWUXWsr1M8zUJ34VatNPuUAr3Z8GH+O2A331CluQ==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "oxlint": "bin/oxlint"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/Boshen"
      },
      "optionalDependencies": {
        "@oxlint/binding-android-arm-eabi": "1.73.0",
        "@oxlint/binding-android-arm64": "1.73.0",
        "@oxlint/binding-darwin-arm64": "1.73.0",
        "@oxlint/binding-darwin-x64": "1.73.0",
        "@oxlint/binding-freebsd-x64": "1.73.0",
        "@oxlint/binding-linux-arm-gnueabihf": "1.73.0",
        "@oxlint/binding-linux-arm-musleabihf": "1.73.0",
        "@oxlint/binding-linux-arm64-gnu": "1.73.0",
        "@oxlint/binding-linux-arm64-musl": "1.73.0",
        "@oxlint/binding-linux-ppc64-gnu": "1.73.0",
        "@oxlint/binding-linux-riscv64-gnu": "1.73.0",
        "@oxlint/binding-linux-riscv64-musl": "1.73.0",
        "@oxlint/binding-linux-s390x-gnu": "1.73.0",
        "@oxlint/binding-linux-x64-gnu": "1.73.0",
        "@oxlint/binding-linux-x64-musl": "1.73.0",
        "@oxlint/binding-openharmony-arm64": "1.73.0",
        "@oxlint/binding-win32-arm64-msvc": "1.73.0",
        "@oxlint/binding-win32-ia32-msvc": "1.73.0",
        "@oxlint/binding-win32-x64-msvc": "1.73.0"
      },
      "peerDependencies": {
        "oxlint-tsgolint": ">=0.24.0",
        "vite-plus": "*"
      },
      "peerDependenciesMeta": {
        "oxlint-tsgolint": {
          "optional": true
        },
        "vite-plus": {
          "optional": true
        }
      }
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.5.tgz",
      "integrity": "sha512-RvwwcruNjI1ncT5xRakeyS9Lf8lcItv34KD+aif+VH9kduAyfYBipGh12274xtenIPZ119/R9BdTBa8gAwSh0A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.16",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.16.tgz",
      "integrity": "sha512-vuwillviilfKZsg0VGj5R/YwwcHx4SLsIOI/7K6mQkWx+l5cUHTjj5g0AasTBcyXsbfTgrwsUNmVUb5xVwyPwg==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "nanoid": "^3.3.12",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/postcss-value-parser": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
      "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
      "license": "MIT"
    },
    "node_modules/proxy-from-env": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-2.1.0.tgz",
      "integrity": "sha512-cJ+oHTW1VAEa8cJslgmUZrc+sjRKgAKl3Zyse6+PV38hZe/V6Z14TbCuXcan9F9ghlz4QrFr2c92TNF82UkYHA==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/react": {
      "version": "19.2.7",
      "resolved": "https://registry.npmjs.org/react/-/react-19.2.7.tgz",
      "integrity": "sha512-HNe9WslTbXmFK8o8cmwgAeJFSBvt1bPdHCVKtaaV+WlAN36mpT4hcRpwbf3fY56ar2oIXzsBpOAiIRHAdY0OlQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "19.2.7",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-19.2.7.tgz",
      "integrity": "sha512-t0BRVXvbiE/o20Hfw669rLbMCDWtYZLvmJigy2f0MxsXF+71pxhR3xOkspmsO8h3ZlNzyibAmtCa3l4lYKk6gQ==",
      "license": "MIT",
      "dependencies": {
        "scheduler": "^0.27.0"
      },
      "peerDependencies": {
        "react": "^19.2.7"
      }
    },
    "node_modules/react-is": {
      "version": "19.2.7",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-19.2.7.tgz",
      "integrity": "sha512-kZFnouyVv7eP/Phmrlo9FK+zcAdriZJvzxXHF1Sl1P377WSGe2G/JxVolhTrB/jeV47lKImhNUsijjHAAbcl/A==",
      "license": "MIT",
      "peer": true
    },
    "node_modules/react-redux": {
      "version": "9.3.0",
      "resolved": "https://registry.npmjs.org/react-redux/-/react-redux-9.3.0.tgz",
      "integrity": "sha512-KQopgqFo/p/fgmAs5qz6p5RWaNAzq40WAu7fJIXnQpYxFPbJYtsJPWvGeF2rOBaY/kEuV77AVsX8TsQzKm+A/g==",
      "license": "MIT",
      "dependencies": {
        "@types/use-sync-external-store": "^0.0.6",
        "use-sync-external-store": "^1.4.0"
      },
      "peerDependencies": {
        "@types/react": "^18.2.25 || ^19",
        "react": "^18.0 || ^19",
        "redux": "^5.0.0"
      },
      "peerDependenciesMeta": {
        "@types/react": {
          "optional": true
        },
        "redux": {
          "optional": true
        }
      }
    },
    "node_modules/react-router": {
      "version": "7.18.1",
      "resolved": "https://registry.npmjs.org/react-router/-/react-router-7.18.1.tgz",
      "integrity": "sha512-GDLgg3i3uM0aeJO3Fm+TCS+sDQ7gu12T6x0qdTEzcwqEfleci7JwugVNIF3U//0FWKnJT7ptG+20B2jfDqnZAg==",
      "license": "MIT",
      "dependencies": {
        "cookie": "^1.0.1",
        "set-cookie-parser": "^2.6.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      },
      "peerDependenciesMeta": {
        "react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/react-router-dom": {
      "version": "7.18.1",
      "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-7.18.1.tgz",
      "integrity": "sha512-KaZh+X/6UtEp28x51AUYZDMg9NGoz2ja3dNHa+ta/tk40vCzKhQ/RypCWBMLbmDr6//E24Vv5uPsrqXFozdkAg==",
      "license": "MIT",
      "dependencies": {
        "react-router": "7.18.1"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      }
    },
    "node_modules/recharts": {
      "version": "3.9.2",
      "resolved": "https://registry.npmjs.org/recharts/-/recharts-3.9.2.tgz",
      "integrity": "sha512-G4fy+Pk46RaXgwWMh+Nzhyo/lbFAVqXo9gtetlyehe6Ehge9CsgDuOTwQDD+i1+llaLktNBiNq4bhnGlDRXFtw==",
      "license": "MIT",
      "workspaces": [
        "www"
      ],
      "dependencies": {
        "@reduxjs/toolkit": "^1.9.0 || 2.x.x",
        "clsx": "^2.1.1",
        "decimal.js-light": "^2.5.1",
        "es-toolkit": "^1.39.3",
        "eventemitter3": "^5.0.1",
        "immer": "^11.1.8",
        "react-redux": "8.x.x || 9.x.x",
        "reselect": "5.2.0",
        "tiny-invariant": "^1.3.3",
        "use-sync-external-store": "^1.2.2",
        "victory-vendor": "^37.0.2"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-is": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/redux": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/redux/-/redux-5.0.1.tgz",
      "integrity": "sha512-M9/ELqF6fy8FwmkpnF0S3YKOqMyoWJ4+CS5Efg2ct3oY9daQvd/Pc71FpGZsVsbl3Cpb+IIcjBDUnnyBdQbq4w==",
      "license": "MIT"
    },
    "node_modules/redux-thunk": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/redux-thunk/-/redux-thunk-3.1.0.tgz",
      "integrity": "sha512-NW2r5T6ksUKXCabzhL9z+h206HQw/NJkcLm1GPImRQ8IzfXwRGqjVhKJGauHirT0DAuyy6hjdnMZaRoAcy0Klw==",
      "license": "MIT",
      "peerDependencies": {
        "redux": "^5.0.0"
      }
    },
    "node_modules/reselect": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/reselect/-/reselect-5.2.0.tgz",
      "integrity": "sha512-AgZ3UOZm3YndfrJ4OYjgrT7bmCm/1iqkjvEfH/oYjzh6PD2qw4QuT3jjnXIrpdt4MTpMXclMT3lXbmRY+XRakw==",
      "license": "MIT"
    },
    "node_modules/rolldown": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/rolldown/-/rolldown-1.1.5.tgz",
      "integrity": "sha512-t9z29cJjXf/vxQ8dyhCSpt6H6aSwHTk8cT5I3iy6SMXuFpk5mB6PL6XfC8PCwrPTx93udwKUm9HRteAlTGBLiA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@oxc-project/types": "=0.139.0",
        "@rolldown/pluginutils": "^1.0.0"
      },
      "bin": {
        "rolldown": "bin/cli.mjs"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "optionalDependencies": {
        "@rolldown/binding-android-arm64": "1.1.5",
        "@rolldown/binding-darwin-arm64": "1.1.5",
        "@rolldown/binding-darwin-x64": "1.1.5",
        "@rolldown/binding-freebsd-x64": "1.1.5",
        "@rolldown/binding-linux-arm-gnueabihf": "1.1.5",
        "@rolldown/binding-linux-arm64-gnu": "1.1.5",
        "@rolldown/binding-linux-arm64-musl": "1.1.5",
        "@rolldown/binding-linux-ppc64-gnu": "1.1.5",
        "@rolldown/binding-linux-s390x-gnu": "1.1.5",
        "@rolldown/binding-linux-x64-gnu": "1.1.5",
        "@rolldown/binding-linux-x64-musl": "1.1.5",
        "@rolldown/binding-openharmony-arm64": "1.1.5",
        "@rolldown/binding-wasm32-wasi": "1.1.5",
        "@rolldown/binding-win32-arm64-msvc": "1.1.5",
        "@rolldown/binding-win32-x64-msvc": "1.1.5"
      }
    },
    "node_modules/scheduler": {
      "version": "0.27.0",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.27.0.tgz",
      "integrity": "sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q==",
      "license": "MIT"
    },
    "node_modules/set-cookie-parser": {
      "version": "2.7.2",
      "resolved": "https://registry.npmjs.org/set-cookie-parser/-/set-cookie-parser-2.7.2.tgz",
      "integrity": "sha512-oeM1lpU/UvhTxw+g3cIfxXHyJRc/uidd3yK1P242gzHds0udQBYzs3y8j4gCCW+ZJ7ad0yctld8RYO+bdurlvw==",
      "license": "MIT"
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/tailwindcss": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-4.3.2.tgz",
      "integrity": "sha512-WtctNNSH8A9jlMIqxzuYumOHU5uGZyRv0Q5svQl+oEPy5w84YpBxdb7MdqyiSPQge5jTJ6zFQLq0PFygdccSBA==",
      "license": "MIT"
    },
    "node_modules/tapable": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/tapable/-/tapable-2.3.3.tgz",
      "integrity": "sha512-uxc/zpqFg6x7C8vOE7lh6Lbda8eEL9zmVm/PLeTPBRhh1xCgdWaQ+J1CUieGpIfm2HdtsUpRv+HshiasBMcc6A==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      }
    },
    "node_modules/tiny-invariant": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz",
      "integrity": "sha512-+FbBPE1o9QAYvviau/qC5SE3caw21q3xkvWKBtja5vgqOWIHHJ3ioaq1VPfn/Szqctz2bU/oYeKd9/z5BL+PVg==",
      "license": "MIT"
    },
    "node_modules/tinyglobby": {
      "version": "0.2.17",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz",
      "integrity": "sha512-wXR/dYpcqKmfWpEdZjiKJOwCNFndD0DMnrW/cYjVGttEkBfVgcLFHoNrlj47mjOVic9yyNu65alsgF4NQyTa2g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.4"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "license": "0BSD",
      "optional": true
    },
    "node_modules/update-browserslist-db": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
      "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/use-sync-external-store": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/use-sync-external-store/-/use-sync-external-store-1.6.0.tgz",
      "integrity": "sha512-Pp6GSwGP/NrPIrxVFAIkOQeyw8lFenOHijQWkUTrDvrF4ALqylP2C/KCkeS9dpUM3KvYRQhna5vt7IL95+ZQ9w==",
      "license": "MIT",
      "peerDependencies": {
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/victory-vendor": {
      "version": "37.3.6",
      "resolved": "https://registry.npmjs.org/victory-vendor/-/victory-vendor-37.3.6.tgz",
      "integrity": "sha512-SbPDPdDBYp+5MJHhBCAyI7wKM3d5ivekigc2Dk2s7pgbZ9wIgIBYGVw4zGHBml/qTFbexrofXW6Gu4noGxrOwQ==",
      "license": "MIT AND ISC",
      "dependencies": {
        "@types/d3-array": "^3.0.3",
        "@types/d3-ease": "^3.0.0",
        "@types/d3-interpolate": "^3.0.1",
        "@types/d3-scale": "^4.0.2",
        "@types/d3-shape": "^3.1.0",
        "@types/d3-time": "^3.0.0",
        "@types/d3-timer": "^3.0.0",
        "d3-array": "^3.1.6",
        "d3-ease": "^3.0.1",
        "d3-interpolate": "^3.0.1",
        "d3-scale": "^4.0.2",
        "d3-shape": "^3.1.0",
        "d3-time": "^3.0.0",
        "d3-timer": "^3.0.1"
      }
    },
    "node_modules/vite": {
      "version": "8.1.4",
      "resolved": "https://registry.npmjs.org/vite/-/vite-8.1.4.tgz",
      "integrity": "sha512-bTT9PsdWO+MQMNG9ZXIP/qM9wGh37DFxTV/sPq9cFpHr3w4jkgef032PkAL9jAqhk3Nz8NQw3O8n6/xFkqO4QQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "lightningcss": "^1.32.0",
        "picomatch": "^4.0.5",
        "postcss": "^8.5.16",
        "rolldown": "~1.1.4",
        "tinyglobby": "^0.2.17"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^20.19.0 || >=22.12.0",
        "@vitejs/devtools": "^0.3.0",
        "esbuild": "^0.27.0 || ^0.28.0",
        "jiti": ">=1.21.0",
        "less": "^4.0.0",
        "sass": "^1.70.0",
        "sass-embedded": "^1.70.0",
        "stylus": ">=0.54.8",
        "sugarss": "^5.0.0",
        "terser": "^5.16.0",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "@vitejs/devtools": {
          "optional": true
        },
        "esbuild": {
          "optional": true
        },
        "jiti": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "sass-embedded": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    }
  }
}

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

```jsx
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

```jsx
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

```jsx
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
        const response = await axios.get('https://milk-project-updated-1.onrender.com/device/history');
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

```jsx
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

```jsx
import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Thermometer, Zap, Clock, Power, ShieldCheck, AlertTriangle, Loader2, CheckCircle2, XCircle, Radio } from 'lucide-react';

// ─────────────────────────────────────────────────────────────────────────────
// CONFIG — change MACHINE_ID to match your ESP32's machine_id field
// ─────────────────────────────────────────────────────────────────────────────
const API_BASE = 'http://localhost:8000';
const MACHINE_ID = 'ESP32_Pasteurizer_01';
const POLL_INTERVAL_MS = 2000; // 2 seconds

// ─────────────────────────────────────────────────────────────────────────────
// STATUS BADGE for active command
// ─────────────────────────────────────────────────────────────────────────────
function CommandStatusBadge({ activeCommand }) {
  if (!activeCommand) return null;

  const statusStyles = {
    PENDING:  'bg-yellow-900/40 text-yellow-400 border-yellow-500/50',
    SENT:     'bg-blue-900/40  text-blue-400   border-blue-500/50',
    EXECUTED: 'bg-green-900/40 text-green-400  border-green-500/50',
    REJECTED: 'bg-red-900/40   text-red-400    border-red-500/50',
    FAILED:   'bg-red-900/40   text-red-400    border-red-500/50',
  };
  const statusIcons = {
    PENDING:  <Radio className="w-4 h-4 animate-pulse" />,
    SENT:     <Radio className="w-4 h-4 animate-pulse" />,
    EXECUTED: <CheckCircle2 className="w-4 h-4" />,
    REJECTED: <XCircle className="w-4 h-4" />,
    FAILED:   <XCircle className="w-4 h-4" />,
  };
  const style = statusStyles[activeCommand.status] || statusStyles.PENDING;
  const icon  = statusIcons[activeCommand.status]  || statusIcons.PENDING;

  return (
    <div className={`mt-4 flex items-center justify-between bg-slate-900 p-3 rounded border ${style} text-sm`}>
      <span className="text-slate-400">
        Last Command: <span className="text-white font-bold">{activeCommand.command}</span>
        <span className="text-slate-500 font-mono text-xs ml-2">({activeCommand.command_id})</span>
      </span>
      <span className={`flex items-center gap-1 font-bold uppercase tracking-widest ${style.split(' ')[1]}`}>
        {icon} {activeCommand.status}
      </span>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// MAIN COMPONENT
// ─────────────────────────────────────────────────────────────────────────────
export default function LiveDashboard() {
  const [sensorData, setSensorData]   = useState(null);
  const [error, setError]             = useState(false);
  const [isSending, setIsSending]     = useState(false); // Prevents double-click

  // Track the ID of the last command WE sent so we can highlight its status
  const lastSentCommandIdRef = useRef(null);

  // ── 1. HTTP Polling for live data ─────────────────────────────────────────
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${API_BASE}/device/live`);
        setSensorData(response.data);
        setError(false);

        // Auto-clear isSending once the command is in a terminal state
        const ac = response.data?.active_command;
        if (
          ac &&
          ac.command_id === lastSentCommandIdRef.current &&
          ['EXECUTED', 'REJECTED', 'FAILED'].includes(ac.status)
        ) {
          setIsSending(false);
        }
      } catch (err) {
        console.error('Error fetching live data:', err);
        setError(true);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, POLL_INTERVAL_MS);
    return () => clearInterval(interval);
  }, []);

  // ── 2. Send a command to the backend ──────────────────────────────────────
  const triggerCommand = async (commandName, parameters = {}) => {
    if (isSending) return;
    setIsSending(true);
    lastSentCommandIdRef.current = null;

    try {
      const response = await axios.post(
        `${API_BASE}/device/${MACHINE_ID}/commands`,
        { command: commandName, parameters }
      );
      lastSentCommandIdRef.current = response.data.command_id;
      console.log(`✅ Command queued: ${response.data.command_id} (${commandName}) — status: ${response.data.status}`);
      // isSending will be cleared when the polling loop sees EXECUTED/REJECTED/FAILED
    } catch (err) {
      console.error('Failed to send command:', err);
      setIsSending(false);
    }
  };

  // ── Helpers ───────────────────────────────────────────────────────────────
  const formatTime = (seconds) => {
    if (seconds === undefined || seconds === null) return '00:00';
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  // ── Loading / Error states ────────────────────────────────────────────────
  if (error) return (
    <div className="p-8 text-xl font-bold text-red-500 flex items-center justify-center h-full bg-slate-900">
      ⚠️ Cannot connect to backend at <code className="ml-2 text-red-400">{API_BASE}</code>.
      <br />Make sure <code>uvicorn main:app</code> is running.
    </div>
  );
  if (!sensorData || Object.keys(sensorData).length === 0) {
    return (
      <div className="flex items-center justify-center h-screen bg-slate-900 text-slate-300">
        <div className="text-center">
          <Loader2 className="w-12 h-12 animate-spin mx-auto mb-4 text-blue-500" />
          <h2 className="text-2xl font-bold">🔌 SCADA System Initializing</h2>
          <p className="mt-2 text-slate-400">Waiting for telemetry from <span className="font-mono text-blue-400">{MACHINE_ID}</span>…</p>
          <p className="mt-1 text-xs text-slate-600">Backend: {API_BASE}</p>
        </div>
      </div>
    );
  }

  const isOnline = sensorData.online;
  const isHolding = sensorData.process_state === 'HOLDING';
  const pipelineStates = ['START', 'HEATING', 'HOLDING', 'COOLING', 'COMPLETE'];
  const activeCommand = sensorData.active_command;

  return (
    <div className="min-h-screen bg-slate-900 p-6 font-sans text-slate-200">
      <div className="max-w-7xl mx-auto flex flex-col gap-6">

        {/* ── Top Bar ── */}
        <div className="flex justify-between items-center bg-slate-800 p-6 rounded-lg border-2 border-slate-700 shadow-lg">
          <div className="flex items-center gap-4">
            <h1 className="text-3xl font-black text-slate-100 tracking-wider">MILK PASTEURIZATION SCADA</h1>
            <span className="bg-slate-900 px-3 py-1 rounded text-sm text-blue-400 font-mono tracking-wider border border-slate-700">
              {sensorData.machine_id}
            </span>
          </div>
          <div className="flex items-center gap-3">
            <span className="font-bold text-slate-400 uppercase text-sm tracking-widest">Status</span>
            <div className={`flex items-center gap-2 px-4 py-2 rounded-full font-bold ${isOnline ? 'bg-green-900/40 text-green-400 border border-green-500/50' : 'bg-red-900/40 text-red-400 border border-red-500/50'}`}>
              <div className={`w-3 h-3 rounded-full ${isOnline ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`}></div>
              {isOnline ? 'ONLINE' : 'OFFLINE'}
            </div>
          </div>
        </div>

        {/* ── Mode & Pipeline ── */}
        <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg flex flex-col gap-6">
          <div className="flex justify-between items-center">
            <div className="flex gap-4">
              <div className="bg-slate-900 p-4 rounded border border-slate-700 min-w-[150px]">
                <div className="text-slate-500 text-xs font-bold uppercase tracking-wider mb-1">Control Mode</div>
                <div className="text-xl font-bold text-blue-400">{sensorData.mode || 'UNKNOWN'}</div>
              </div>
              <div className="bg-slate-900 p-4 rounded border border-slate-700 min-w-[150px]">
                <div className="text-slate-500 text-xs font-bold uppercase tracking-wider mb-1">Process State</div>
                <div className="text-xl font-bold text-emerald-400">{sensorData.process_state || 'IDLE'}</div>
              </div>
            </div>
          </div>

          <div className="flex items-center w-full bg-slate-900 p-4 rounded border border-slate-700 overflow-x-auto">
            {pipelineStates.map((state, index) => {
              const isActive = sensorData.process_state === state;
              const isPast = pipelineStates.indexOf(sensorData.process_state) > index;
              return (
                <div key={state} className="flex-1 flex items-center min-w-[120px]">
                  <div className={`flex-1 text-center py-2 rounded font-bold text-sm tracking-wider whitespace-nowrap
                    ${isActive ? 'bg-blue-600 text-white shadow-[0_0_15px_rgba(37,99,235,0.5)]' :
                      isPast ? 'text-slate-400' : 'text-slate-600'}`}>
                    [ {state} ]
                  </div>
                  {index < pipelineStates.length - 1 && (
                    <div className="w-8 flex justify-center">
                      <span className={isPast ? 'text-blue-500' : 'text-slate-700'}>→</span>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* ── Main Dashboard Grid ── */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Column 1: Temperature & Timers */}
          <div className="lg:col-span-1 flex flex-col gap-6">
            <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg relative overflow-hidden h-full flex flex-col justify-center text-center group">
              <Thermometer className="absolute -top-4 -left-4 w-32 h-32 text-slate-700/30 group-hover:text-blue-500/10 transition-colors" />
              <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-2 z-10">Temperature</h3>
              <div className="text-7xl font-black text-white z-10">
                {(sensorData.temperature || 0).toFixed(1)}<span className="text-3xl text-slate-500">°C</span>
              </div>

              <div className="grid grid-cols-2 gap-4 mt-8 z-10">
                <div className="bg-slate-900 p-3 rounded border border-slate-700">
                  <div className="text-xs text-slate-500 uppercase font-bold">Target</div>
                  <div className="text-lg font-bold text-blue-400">{sensorData.target_temperature || 0}°C</div>
                </div>
                <div className="bg-slate-900 p-3 rounded border border-slate-700">
                  <div className="text-xs text-slate-500 uppercase font-bold">Diff</div>
                  <div className="text-lg font-bold text-amber-400">
                    {Math.abs((sensorData.temperature || 0) - (sensorData.target_temperature || 0)).toFixed(1)}°C
                  </div>
                </div>
              </div>
            </div>

            {/* Conditional Holding Timer */}
            {isHolding && (
              <div className="bg-slate-800 p-6 rounded-lg border-2 border-emerald-500/50 shadow-[0_0_20px_rgba(16,185,129,0.1)] text-center animate-pulse">
                <Clock className="w-8 h-8 text-emerald-500 mx-auto mb-2" />
                <h3 className="text-slate-300 font-bold uppercase tracking-widest mb-2">Holding Timer</h3>
                <div className="flex justify-center items-center gap-4 text-3xl font-mono font-bold text-emerald-400">
                  <span>{formatTime(sensorData.holding_elapsed_sec)}</span>
                  <span className="text-slate-600">/</span>
                  <span>{formatTime(sensorData.holding_time_sec)}</span>
                </div>
                <div className="mt-2 text-sm text-emerald-600 font-bold">
                  REMAINING: {formatTime(sensorData.holding_remaining_sec)}
                </div>
              </div>
            )}
          </div>

          {/* Column 2: Equipment Relays */}
          <div className="lg:col-span-2 flex flex-col gap-6">
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
              {[
                { name: 'HEATER',  state: sensorData.heater  },
                { name: 'STIRRER', state: sensorData.stirrer },
                { name: 'COOLER',  state: sensorData.cooler  }
              ].map(equip => (
                <div key={equip.name} className={`bg-slate-800 p-6 rounded-lg border ${equip.state ? 'border-green-500/50' : 'border-slate-700'} shadow-lg flex flex-col items-center justify-center transition-all`}>
                  <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4">{equip.name}</h3>
                  <div className={`w-16 h-16 rounded-full flex items-center justify-center mb-4 transition-colors ${equip.state ? 'bg-green-500 shadow-[0_0_20px_rgba(34,197,94,0.4)]' : 'bg-slate-700'}`}>
                    <Power className={`w-8 h-8 ${equip.state ? 'text-white' : 'text-slate-900'}`} />
                  </div>
                  <div className={`text-2xl font-black ${equip.state ? 'text-green-400' : 'text-slate-600'}`}>
                    {equip.state ? 'ON' : 'OFF'}
                  </div>
                </div>
              ))}
            </div>

            {/* Electrical Telemetry */}
            <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
              <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
                <Zap className="w-5 h-5 text-yellow-500" />
                Electrical Telemetry
              </h3>
              <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                {[
                  { label: 'VOLTAGE', val: (sensorData.voltage      || 0).toFixed(1),  unit: 'V'   },
                  { label: 'CURRENT', val: (sensorData.current      || 0).toFixed(2),  unit: 'A'   },
                  { label: 'POWER',   val: (sensorData.power        || 0).toFixed(1),  unit: 'W'   },
                  { label: 'ENERGY',  val: (sensorData.energy       || 0).toFixed(3),  unit: 'kWh' },
                  { label: 'FREQ',    val: (sensorData.frequency    || 0).toFixed(1),  unit: 'Hz'  },
                  { label: 'PF',      val: (sensorData.power_factor || 0).toFixed(2),  unit: ''    }
                ].map(metric => (
                  <div key={metric.label} className="bg-slate-900 p-3 rounded border border-slate-800 text-center">
                    <div className="text-[10px] text-slate-500 font-bold uppercase tracking-widest mb-1">{metric.label}</div>
                    <div className="text-lg font-mono font-bold text-slate-200">
                      {metric.val} <span className="text-xs text-slate-500">{metric.unit}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* ── Bottom: Control Panel & Alarms ── */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          <div className="lg:col-span-3 bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
            <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-blue-500" />
              Command Center
            </h3>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <button
                id="btn-auto-start"
                onClick={() => triggerCommand('AUTO_START', { target_temperature: 72.0, hold_time: 15, cool_temperature: 35.0 })}
                disabled={isSending}
                className="w-full bg-green-700 hover:bg-green-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Auto Start
              </button>
              <button
                id="btn-manual"
                onClick={() => triggerCommand('MANUAL_MODE')}
                disabled={isSending}
                className="w-full bg-blue-700 hover:bg-blue-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Manual
              </button>
              <button
                id="btn-stop"
                onClick={() => triggerCommand('STOP')}
                disabled={isSending}
                className="w-full bg-amber-700 hover:bg-amber-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors"
              >
                Stop
              </button>
              <button
                id="btn-emergency-stop"
                onClick={() => triggerCommand('EMERGENCY_STOP')}
                disabled={isSending}
                className="w-full bg-red-700 hover:bg-red-600 disabled:bg-slate-700 disabled:cursor-not-allowed text-white py-4 rounded font-bold uppercase tracking-wider transition-colors flex items-center justify-center gap-2"
              >
                <AlertTriangle className="w-5 h-5" /> E-STOP
              </button>
            </div>

            {/* Live Command Status (driven by backend state) */}
            <CommandStatusBadge activeCommand={activeCommand} />
          </div>

          {/* Fault / Alarm Panel */}
          <div className="lg:col-span-1 bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-lg">
            <h3 className="text-slate-400 font-bold uppercase tracking-widest mb-4 flex items-center gap-2">
              <AlertTriangle className={`w-5 h-5 ${sensorData.fault ? 'text-red-500 animate-pulse' : 'text-slate-500'}`} />
              Active Alarms
            </h3>
            <div className={`h-full min-h-[80px] rounded flex items-center justify-center border p-4 ${sensorData.fault ? 'bg-red-900/30 border-red-500 text-red-500' : 'bg-slate-900 border-slate-700 text-slate-500'}`}>
              {sensorData.fault ? (
                <div className="text-center font-bold">
                  <div className="text-xl uppercase">FAULT DETECTED</div>
                  <div className="text-sm font-mono mt-1">{sensorData.fault_code || 'UNKNOWN ERROR'}</div>
                </div>
              ) : (
                <div className="font-bold uppercase tracking-wider text-sm text-center">No active alarms</div>
              )}
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

```

## machine_learning\__init__.py

```py

```

## machine_learning\feature_engineering.py

```py
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

```py
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

```py
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

```py
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

## routers\__init__.py

```py
# Init file for routers package

```

## routers\commands.py

```py
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

```

## routers\device.py

```py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import schemas
import models
from database import get_db
from services.industrial_logic import calculate_heater_decision, check_industrial_safety_override

router = APIRouter(
    prefix="/device",
    tags=["IoT Device Endpoints"]
)

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
            "action": pending_command.command,   # e.g. "AUTO_START", "STOP", "EMERGENCY_STOP"
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

```

## routers\prediction.py

```py
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

## services\__init__.py

```py
# init

```

## services\industrial_logic.py

```py
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

## services\websocket_manager.py

```py
from fastapi import WebSocket
from typing import Dict, List

class ConnectionManager:
    def __init__(self):
        # Maps a specific machine_id to its active ESP32 WebSocket
        self.active_machines: Dict[str, WebSocket] = {}
        # Holds all connected React dashboards listening for live updates
        self.dashboard_clients: List[WebSocket] = []

    # --- ESP32 MACHINE CONNECTIONS ---
    async def connect_machine(self, machine_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_machines[machine_id] = websocket
        print(f"[WebSocket] ESP32 Machine {machine_id} connected.")

    def disconnect_machine(self, machine_id: str):
        if machine_id in self.active_machines:
            del self.active_machines[machine_id]
            print(f"[WebSocket] ESP32 Machine {machine_id} disconnected.")

    async def send_to_machine(self, machine_id: str, message: dict) -> bool:
        """Sends a JSON command strictly to the targeted ESP32."""
        if machine_id in self.active_machines:
            websocket = self.active_machines[machine_id]
            try:
                await websocket.send_json(message)
                return True
            except Exception:
                self.disconnect_machine(machine_id)
                return False
        return False

    # --- DASHBOARD CONNECTIONS ---
    async def connect_dashboard(self, websocket: WebSocket):
        await websocket.accept()
        self.dashboard_clients.append(websocket)
        print("[WebSocket] React Dashboard client connected.")

    def disconnect_dashboard(self, websocket: WebSocket):
        if websocket in self.dashboard_clients:
            self.dashboard_clients.remove(websocket)
            print("[WebSocket] React Dashboard client disconnected.")

    async def broadcast_machine_state(self, state: dict):
        """Pushes live machine state to all connected React dashboards without page refresh."""
        disconnected_clients = []
        for client in self.dashboard_clients:
            try:
                await client.send_json(state)
            except Exception:
                disconnected_clients.append(client)
        
        # Clean up dead connections so the server doesn't crash
        for client in disconnected_clients:
            self.disconnect_dashboard(client)

# Create a single global instance to import across your routers
manager = ConnectionManager()

```
