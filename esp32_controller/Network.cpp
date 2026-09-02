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
