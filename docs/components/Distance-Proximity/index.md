---
id: IO500
name: Distance & Proximity Sensors
title: Distance & Proximity Sensors
category: IO
tags:
  - sensor
  - distance
  - proximity
  - ultrasonic
  - laser
  - tof
short: "Distance measurement • Proximity"
use: "ranging, obstacle detection"
no_label: true
---

# Distance & Proximity Sensors - IO500

Sensors for measuring distance to objects or detecting proximity. Includes ultrasonic rangefinders and Time-of-Flight (ToF) laser sensors.

## Components in This Family

{{ children() }}

## Comparison

| Component | Technology | Range | Accuracy | Interface | Best For |
|-----------|-----------|-------|----------|-----------|----------|
| [IO501](IO501.md) | Ultrasonic | 2cm - 4m | ±3mm | Digital (pulse) | General ranging, obstacle avoidance |
| [IO502](IO502.md) | Laser ToF | 3cm - 2m | ±3% | I2C | Precise indoor measurement, gesture detection |

## Selection Guide

**For general distance measurement:**
- Use IO501 (HC-SR04) - ultrasonic
- Cheap, simple, good for most projects
- Works outdoors in all lighting
- 2cm to 4m range

**For precise indoor measurement:**
- Use IO502 (VL53L0X) - laser ToF
- Higher accuracy (±3%)
- Faster measurement (<30ms)
- Smaller beam angle (more precise)
- Not affected by surface color/texture

**For outdoor use:**
- Use IO501 (ultrasonic)
- Laser affected by sunlight
- Ultrasonic works in all conditions

**For long range (>4m):**
- Neither sensor good for >4m
- Consider: VL53L1X (4m), ultrasonic modules with longer range

## Key Concepts

**Ultrasonic ranging:**
- Sends 40 kHz sound pulse
- Measures echo return time
- Distance = (time × speed_of_sound) / 2
- Affected by temperature (speed of sound changes)

**Time-of-Flight (ToF) laser:**
- Sends infrared light pulse
- Measures time for reflection
- Very fast (<30ms)
- Narrow beam (precise targeting)

**Beam angle:**
- **Ultrasonic:** ~15° cone (wider, less precise)
- **Laser ToF:** ~25° FoV (narrower, more precise)

## Gotchas

**Ultrasonic sensors:**
- Soft materials (foam, fabric) absorb sound (poor echo)
- Angled surfaces deflect sound away (no echo)
- Small objects may not reflect enough sound
- Temperature affects speed of sound (calibration needed)

**Laser ToF sensors:**
- Sunlight interferes (outdoor use limited)
- Dark surfaces absorb more light (reduced range)
- Transparent surfaces (glass) invisible to sensor
- More expensive than ultrasonic

## Typical Applications

**Ultrasonic (IO501):**
- Robot obstacle avoidance
- Parking sensors
- Water tank level monitoring
- People counting (door entry)
- Drone altitude hold

**Laser ToF (IO502):**
- Gesture recognition
- Indoor navigation
- Precise bin level monitoring
- Hand sanitizer dispenser (proximity trigger)
- VR/AR tracking
