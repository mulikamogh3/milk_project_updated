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
