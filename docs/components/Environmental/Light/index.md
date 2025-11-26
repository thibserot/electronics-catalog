---
id: ENV300
name: Light Sensors
category: ENV
tags:
  - family
  - light-sensor
  - lux
  - photoresistor
  - i2c
short: "Light Sensors • Digital & Analog"
use: "Lux measurement • Dark/bright"
---

# Light Sensors - ENV300

Light sensors for measuring illuminance (lux) or detecting brightness levels. Choose between digital I2C sensors (accurate lux values) or analog photoresistors (simple dark/bright thresholds). All measure visible light, some compensate for IR to approximate human eye response.

## Comparison

| Component | Type | Range | Interface | Power | Best For |
|-----------|------|-------|-----------|-------|----------|
| [ENV301](ENV301.md) (TSL2561) | Digital | 0.1-40k lux | I2C (0x29/39/49) | 0.6 mA | Budget digital, general use |
| [ENV302](ENV302.md) (TSL2591) | Digital | 188µ-88k lux | I2C (0x29) | Higher | Extreme range, high sensitivity |
| [ENV303](ENV303.md) (BH1750) | Digital | 1-65k lux | I2C (0x23/5C) | 0.12 mA | Low power, simple output |
| [ENV304](ENV304.md) (Photoresistor) | Analog | Qualitative | ADC (voltage divider) | Passive | Cheapest, threshold detection |
| [ENV305](ENV305.md) (LDR 5528) | Analog | 10-20kΩ light | ADC (voltage divider) | Passive | Simple ambient light sensing |

## Selection Guide

**[ENV301](ENV301.md) (TSL2561):** General-purpose digital sensor, good price/performance balance

**[ENV302](ENV302.md) (TSL2591):** Best dynamic range (600M:1), extreme low-light and bright-light capability

**[ENV303](ENV303.md) (BH1750):** Simplest code, lowest power (0.12 mA), direct lux output

**[ENV304](ENV304.md) (Photoresistor):** Cheapest option, analog only, good for "dark/bright" thresholds

**[ENV305](ENV305.md) (LDR 5528):** GL5528 CdS photoresistor, classic voltage divider design

## Common Applications

**Auto-brightness displays:** Adjust screen/LED brightness based on ambient light (any digital sensor)

**Outdoor weather stations:** Measure daylight intensity (ENV302 for wide range)

**Smart lighting:** Turn lights on when dark (ENV304 cheapest, digital for precise control)

**Solar trackers:** Maximize panel orientation (digital sensors for accuracy)

**Camera auto-exposure:** Measure scene brightness (ENV302 for best dynamic range)

---

## Components in This Family

{{ children() }}
