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
