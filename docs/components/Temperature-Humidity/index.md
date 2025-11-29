---
id: ENV100
name: Temperature & Humidity Sensors
category: ENV
tags:
  - sensor
  - temperature
  - humidity
  - environmental
  - esp32-compatible
  - arduino-compatible
short: "Temp & humidity • I2C/1-Wire"
use: "environmental monitoring"
---

# Temperature & Humidity Sensors - ENV100

Sensors for measuring ambient temperature and/or relative humidity. Essential for weather stations, environmental monitoring, greenhouse automation, and HVAC control.

## Comparison

| Component | Type | Temp Range | RH Range | Accuracy | Interface | Response Time | Best For |
|-----------|------|------------|----------|----------|-----------|---------------|----------|
| [ENV101](ENV101.md) | Temp only | -55 to 125°C | - | ±0.5°C | 1-Wire | ~750ms | Multiple sensors, waterproof |
| [ENV102](ENV102.md) | Temp+RH+Press | -40 to 85°C | 0-100% | ±1°C, ±3% RH | I2C/SPI | <1s | Weather stations, altitude |
| [ENV103](ENV103.md) | Temp+RH | 0 to 50°C | 20-90% | ±2°C, ±5% RH | 1-Wire | ~2s | Basic projects, low cost |
| [ENV104](ENV104.md) | Temp+RH | -40 to 125°C | 0-100% | ±0.1°C, ±1% RH | I2C | <1s | High precision, lab use |
| [ENV105](ENV105.md) | Temp only | -50 to 150°C | - | ~1-2°C | Analog | Instant | Simple circuits, wide range |

## Selection Guide

**[ENV101 - DS18B20](ENV101.md):** Digital 1-Wire temperature sensor. Best for multiple sensors on one bus (e.g., multi-zone monitoring). Available in waterproof probe form. Temperature only, no humidity.

**[ENV102 - BME280/BMP280](ENV102.md):** All-in-one I2C sensor with temperature, humidity, AND barometric pressure. Perfect for weather stations and altitude measurement. Industry standard for environmental sensing.

**[ENV103 - DHT11](ENV103.md):** Budget-friendly temp + humidity sensor. Good enough for basic projects but slow (1 reading/second) and less accurate. Easy to use for beginners.

**[ENV104 - GY-SHT45](ENV104.md):** High-precision I2C sensor with ±0.1°C temperature and ±1% RH accuracy. Use when precision matters (lab, greenhouse, incubator). Most expensive option.

**[ENV105 - Thermistor](ENV105.md):** Simple analog temperature sensor (NTC resistor). Cheapest option, requires calibration. Good for basic temperature sensing when humidity not needed.

## Common Applications

**Weather station:** Use ENV102 (BME280) for complete environmental data including pressure for weather prediction.

**Multi-zone temperature monitoring:** Use ENV101 (DS18B20) on 1-Wire bus to monitor multiple rooms/zones with single GPIO pin.

**Greenhouse automation:** Use ENV104 (SHT45) for precise humidity control to prevent mold/disease.

**Basic room monitoring:** Use ENV103 (DHT11) or ENV105 (thermistor) for cost-effective temperature tracking.

**Outdoor waterproof:** Use ENV101 (DS18B20) in waterproof stainless steel probe for pond/soil temperature.

## Interface Comparison

**1-Wire (ENV101, ENV103):**
- Single data wire (+ power + ground)
- Multiple sensors on one bus
- Slower but simpler wiring

**I2C (ENV102, ENV104):**
- Two wires (SDA + SCL, + power + ground)
- Faster communication
- Can share bus with other I2C devices
- Standard protocol, well-supported

**Analog (ENV105):**
- Single analog pin
- Requires ADC and calibration
- Simplest circuit, no protocol
- Most basic but functional

## Accuracy vs Cost

```
High Precision                    Low Cost
    |                                |
ENV104 -----> ENV102 -----> ENV101 -----> ENV103 -----> ENV105
(SHT45)      (BME280)     (DS18B20)      (DHT11)     (Thermistor)
```

Choose based on your precision requirements and budget.

---

## Components in This Family

{{ children() }}
