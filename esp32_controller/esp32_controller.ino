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
