---
id: IO400
name: Motion & Orientation Sensors
title: Motion & Orientation Sensors
category: IO
tags:
  - sensor
  - motion
  - orientation
  - accelerometer
  - gyroscope
  - magnetometer
short: "IMU • Tilt • Motion detect"
use: "orientation tracking, motion detection"
---

# Motion & Orientation Sensors - IO400

Sensors for detecting motion, orientation, tilt, and rotation. Includes IMUs (gyro+accel), standalone accelerometers, magnetometers, tilt switches, vibration sensors, and PIR motion detectors.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Axes | Interface | Best For |
|-----------|------|------|-----------|----------|
| [IO401](IO401.md) | Gyro + Accel | 6-axis | I2C | Orientation tracking, drones, balancing |
| [IO402](IO402.md) | Accelerometer | 3-axis | I2C/SPI | Tilt, vibration, impact detection |
| [IO403](IO403.md) | Magnetometer | 3-axis | I2C | Digital compass, heading detection |
| [IO404](IO404.md) | Tilt Switch | 1-axis | Digital | Simple tilt ON/OFF detection |
| [IO405](IO405.md) | Vibration Sensor | Digital | Digital | Vibration/knock/shock detection |
| [IO406](IO406.md) | PIR Motion | Passive IR | Digital | Human presence detection (3-7m range) |

## Selection Guide

**For drone/gimbal stabilization:**
- Use IO401 (MPU6050) - gyro + accel
- 6-axis IMU for orientation tracking
- DMP for sensor fusion

**For tilt/inclination measurement:**
- Use IO402 (ADXL345) - accelerometer only
- Cheaper than full IMU if no rotation needed
- Or use IO404 for simple ON/OFF tilt

**For compass/heading:**
- Use IO403 (HMC5883L) - magnetometer
- Digital compass for navigation
- Combine with IMU for 9-axis fusion

**For simple tilt detection:**
- Use IO404 (ball tilt switch)
- No code needed (mechanical switch)
- Binary ON/OFF output

**For vibration/knock detection:**
- Use IO405 (SW-420)
- Detects vibration, tapping, shaking
- Adjustable sensitivity

**For human presence:**
- Use IO406 (PIR sensor)
- Detects body heat motion
- 3-7 meter range, wide angle

## Key Concepts

**Accelerometer:**
- Measures linear acceleration (g-force)
- Can detect tilt via gravity vector
- Cannot detect rotation rate

**Gyroscope:**
- Measures angular velocity (rotation speed)
- Cannot detect absolute orientation (drifts)
- Needs integration to get angle

**IMU (Inertial Measurement Unit):**
- Combines gyro + accel (6-axis)
- Sometimes adds magnetometer (9-axis)
- Sensor fusion for accurate orientation

**Magnetometer:**
- Detects Earth's magnetic field
- Digital compass functionality
- Affected by metal/magnets nearby

**PIR (Passive Infrared):**
- Detects infrared radiation (body heat)
- No active emission (passive)
- Fresnel lens focuses IR onto sensor

## Coordinate Systems

**MPU6050 / ADXL345 orientation:**
```
      Y
      ^
      |
      +----> X
     /
    Z (into board)

Accelerometer at rest:
- X = 0g, Y = 0g, Z = +1g (horizontal, Z up)
- X = +1g, Y = 0g, Z = 0g (tilted right)
```

## Gotchas

**IMU sensors:**
- Gyro drifts over time (needs recalibration)
- Accelerometer noisy during movement
- I2C address conflicts if using multiple sensors
- Temperature affects readings (calibration needed)

**Magnetometer:**
- Metal nearby distorts readings
- Hard-iron and soft-iron calibration required
- USB cables and motors cause interference
- Not useful indoors (building steel distorts field)

**PIR sensors:**
- False triggers from sunlight, pets, fans
- Blind spot directly in front (needs lateral motion)
- Fresnel lens affects detection pattern
- Warm-up time needed (~60 seconds)

**Tilt/vibration switches:**
- Mechanical (wear out over time)
- Orientation dependent (mount carefully)
- Debouncing required
