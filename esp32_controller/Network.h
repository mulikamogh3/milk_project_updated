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
