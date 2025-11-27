---
id: AC400
name: Small Motors
category: AC
tags:
  - motor
  - dc-motor
  - actuator
  - esp32-compatible
  - arduino-compatible
no_label: true
---

# Small Motors (Drone/Toy) - AC400

Tiny DC motors for drones, RC vehicles, and robotics projects. Includes coreless motors for high-speed applications and gear motors for high-torque low-speed use.

## Comparison

| Component | Type | Voltage | Speed | Torque | Shaft | Best For |
|-----------|------|---------|-------|--------|-------|----------|
| [AC401](AC401.md) | Coreless | 3.7-4.2V | High (30,000+ RPM) | Low | 0.8mm | Quadcopters, fast props |
| [AC402](AC402.md) | Gear motor | 3-6V | Low (60 RPM) | High | 3mm D-shaft | Robots, wheels, precise control |

## Selection Guide

**[AC401 - 716 Coreless Motor](AC401.md):** Ultra-light, high-speed brushed coreless motor. Perfect for micro quadcopters and RC planes. Comes with propeller. Very high RPM but low torque.

**[AC402 - N20 Gear Motor](AC402.md):** Compact metal gearbox motor with 60 RPM output. Great for robot wheels, linear actuators, and precise positioning. Higher torque, lower speed.

## Common Applications

**Micro drones/quadcopters:** Use AC401 (716 coreless) for lightweight, high-speed propeller drive.

**Robot wheels:** Use AC402 (N20 gear motor) for controlled movement and sufficient torque.

**Linear actuators:** Use AC402 (N20 gear motor) with lead screw for precise positioning.

**Fast props (fans, toys):** Use AC401 (716 coreless) for maximum RPM.

## Motor Selection Tips

**Coreless motors (AC401):**

- Very lightweight
- High speed, low torque
- Shorter lifespan (brushes wear)
- Best with propellers or light loads

**Gear motors (AC402):**

- Higher torque at low speed
- Heavier (metal gearbox)
- More durable
- Best for wheels, actuators, precise control

## Driver Requirements

Both motors require:

- **Motor driver** (TB6612, L293D, or H-bridge)
- **PWM speed control**
- **Direction control** for reversing
- **Flyback diode protection** if not using integrated driver module

**Never drive motors directly from GPIO pins** - use a motor driver module.

---

## Components in This Family

{{ children() }}
