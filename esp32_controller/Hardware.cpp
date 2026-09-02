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
