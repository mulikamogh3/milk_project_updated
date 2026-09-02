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
