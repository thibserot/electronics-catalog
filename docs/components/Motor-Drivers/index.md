---
id: AC100
name: Motor Drivers
category: AC
tags:
  - motor-driver
  - h-bridge
  - actuator
  - esp32-compatible
  - arduino-compatible
no_label: true
---

# Motor Drivers - AC100

Motor driver modules and ICs for controlling DC motors, providing H-bridge circuits for bidirectional control and current amplification.

## Comparison

| Component | Type | Channels | Current/Ch | Voltage Range | Interface | Best For |
|-----------|------|----------|-----------|---------------|-----------|----------|
| [AC101](AC101.md) | Module | 2 | 1.2A | 2.7-5.5V | PWM | Small motors, compact design |
| [AC102](AC102.md) | IC | 2 | 600mA | 4.5-36V | Logic | Breadboard projects, higher voltage |

## Selection Guide

**[AC101 - TB6612 Module](AC101.md):** Compact dual motor driver module with built-in MOSFETs. Best for small DC motors (gear motors, coreless motors). More efficient than L293D. Includes enable pins for PWM speed control.

**[AC102 - L293D IC](AC102.md):** Classic H-bridge IC in DIP-16 package. Easy to use on breadboards. Supports higher voltages (up to 36V). Good for learning and prototyping. Higher voltage drop (~2V) compared to TB6612.

## Common Applications

**Small robot platforms:** Use AC101 (TB6612) for efficiency and compact size with gear motors or small DC motors.

**Breadboard prototyping:** Use AC102 (L293D) for ease of wiring and testing.

**Higher voltage motors (12V+):** Use AC102 (L293D) if motors need more than 5.5V.

## Wiring Notes

Both drivers require:

- **Motor power supply** (separate from logic power)
- **PWM signals** for speed control
- **Direction control** pins
- **Enable pins** (can be tied high for always-on)

**Current limiting:** Always check motor stall current doesn't exceed driver rating.

**Heat dissipation:** Add heatsinks if running at high currents for extended periods.

---

## Components in This Family

{{ children() }}
