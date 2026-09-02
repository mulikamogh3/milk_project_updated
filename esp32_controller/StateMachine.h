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
