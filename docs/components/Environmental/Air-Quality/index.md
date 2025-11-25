---
id: ENV200
name: Air Quality & Gas Sensors
category: ENV
tags: [family, sensor, air-quality, gas]
sticker_line1: "Air Quality & Gas Sensors"
sticker_line2: "Family anchor"
---

# Air Quality & Gas Sensors

Sensors for detecting CO2 concentration, combustible gases, smoke, and other airborne pollutants.

## Comparison

| Component | Detects | Range | Interface | Accuracy | Preheat | Best For |
|-----------|---------|-------|-----------|----------|---------|----------|
| [ENV201](ENV201.md) (MH-Z19C) | CO2 only | 400-5000ppm | UART, PWM | ±(50ppm+5%) | 3 min | Indoor air quality, HVAC control |
| [ENV202](ENV202.md) (MQ-2) | LPG, smoke, methane, propane, H2, CO | 200-10000ppm | Analog, Digital | Requires calibration | 24-48 hrs | Gas leak detection, fire alarm |

## Selection Guide

**Choose [ENV201](ENV201.md) (MH-Z19C) when:**

- Monitoring indoor CO2 levels (ventilation control, HVAC)
- Need accurate, quantitative CO2 measurements
- Quick startup time required (3 min preheat)
- Digital interface preferred (UART communication)

**Choose [ENV202](ENV202.md) (MQ-2) when:**

- Detecting combustible gas leaks (LPG, methane, propane)
- Building fire/smoke alarm systems
- Simple analog threshold detection sufficient
- Don't need precise ppm readings (qualitative detection)

## Projects Using This Family

- Smart ventilation (ENV201: auto-open windows when CO2 >1000ppm)
- Kitchen gas leak alarm (ENV202: LPG detection)
- Indoor air quality monitor (ENV201: log CO2 + temp/humidity)
- RV/camper safety (ENV201: CO2, ENV202: propane detection)

---

{{ children() }}
