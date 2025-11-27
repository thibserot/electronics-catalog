---
id: ENV400
name: Moisture & Water Sensors
category: ENV
tags:
  - sensor
  - moisture
  - water
  - soil
  - rain
  - irrigation
  - environmental
  - esp32-compatible
  - arduino-compatible
no_label: true
---

# Moisture & Water Sensors - ENV400

Sensors for detecting water presence, soil moisture levels, and rainfall. Essential for irrigation automation, leak detection, and water level monitoring.

## Comparison

| Component | Type | Output | Sensitivity | Best For |
|-----------|------|--------|-------------|----------|
| [ENV401](ENV401.md) | Soil moisture | Analog voltage | Adjustable | Plant watering, garden automation |
| [ENV402](ENV402.md) | Water level | Analog/Digital | Variable depth | Tank level, leak detection |
| [ENV403](ENV403.md) | Rain detection | Analog/Digital | Rainfall intensity | Weather station, sprinkler control |

## Selection Guide

**[ENV401 - Soil Moisture Sensor](ENV401.md):** Measures moisture content in soil using capacitive or resistive sensing. Perfect for automated plant watering systems. Analog output proportional to moisture level.

**[ENV402 - Water Level Sensor](ENV402.md):** Detects presence and depth of water using exposed traces. Good for tank level monitoring, leak detection, and flood sensors. Both analog (level) and digital (threshold) outputs.

**[ENV403 - Rain Sensor](ENV403.md):** Detects rainfall on sensing board. Triggers when raindrops hit surface. Useful for automatic sprinkler shutoff, weather stations, and window closing automation.

## Common Applications

**Smart irrigation:** Use ENV401 (soil moisture) to water plants only when soil is dry.

**Rain-aware sprinklers:** Use ENV403 (rain sensor) to disable sprinklers during rainfall.

**Water tank monitoring:** Use ENV402 (water level) to track tank fill level.

**Leak detection:** Use ENV402 (water level) to detect basement/pipe leaks.

**Weather station:** Combine ENV403 (rain) with ENV102 (BME280) for complete weather data.

## Sensor Types

**Resistive sensors:**
- Two probes measure resistance through soil/water
- Cheaper but probe corrosion issues
- Direct contact with liquid

**Capacitive sensors:**
- Measures dielectric constant (no exposed metal)
- More durable, less corrosion
- Can sense through plastic barrier
- More expensive

**Water level (exposed traces):**
- Multiple parallel traces
- Analog output based on submersion depth
- Cheap but corrodes over time

## Power Considerations

**Avoid constant power:**
- Sensors degrade faster with constant DC voltage
- Electrolysis corrodes probes
- Use switched power (turn on only when reading)

**Example switching:**
```cpp
// Power sensor only during measurement
digitalWrite(SENSOR_POWER_PIN, HIGH);  // Power ON
delay(100);  // Let sensor stabilize
int reading = analogRead(SENSOR_PIN);
digitalWrite(SENSOR_POWER_PIN, LOW);   // Power OFF
```

## Interface Types

**Analog output:**
- Voltage varies with moisture/water level
- Read with ADC (0-3.3V or 0-5V)
- More information (gradual changes)

**Digital output:**
- ON/OFF threshold detection
- Adjustable via potentiometer
- Simpler to use (GPIO read)

Most modules provide BOTH outputs.

## Calibration

**Soil moisture calibration:**
1. **Dry:** Read sensor in completely dry soil
2. **Wet:** Read sensor in water-saturated soil
3. Map readings to 0-100% moisture range

**Water level calibration:**
1. Measure voltage at each depth increment
2. Create lookup table or linear equation
3. Account for sensor orientation

---

## Components in This Family

{{ children() }}
