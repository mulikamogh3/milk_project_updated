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
