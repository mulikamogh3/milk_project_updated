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
