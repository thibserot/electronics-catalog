---
id: AC500
name: Servos
category: AC
tags:
  - family
  - servo
  - micro-servo
  - position-control
  - continuous-rotation
short: "Servos • 9g micro"
use: "Position • Continuous rotation"
---

# Servos - AC500

9g micro servos for position control and continuous rotation. All use standard hobby servo PWM interface (50 Hz, 3-wire connector). Choose based on whether you need position control (0-180°) or continuous rotation, and required torque/durability.

## Comparison

| Component | Model | Type | Torque @ 4.8V | Speed/Range | Gear Material | Best For |
|-----------|-------|------|---------------|-------------|---------------|----------|
| [AC501](AC501.md) (SG92R) | Position | Micro servo | 2.5 kg·cm | 0-180° | Carbon fiber | Durability, higher torque |
| [AC502](AC502.md) (SG90) | Position | Micro servo | 1.8 kg·cm | 0-180° | Plastic | Learning, prototyping, low cost |
| [AC503](AC503.md) (SG90-360) | Continuous | Micro servo | 1.3 kg·cm | 110-130 RPM | Plastic/POM | Wheels, motors, bidirectional |

## Selection Guide

**Choose [AC501](AC501.md) (SG92R) when:**

- Need reliable position control with durability (carbon fiber gears)
- Want highest torque (2.5 kg·cm) for 9g servo
- Building mechanisms that will be used repeatedly
- Budget allows for slightly higher cost (~2× SG90 price)

**Choose [AC502](AC502.md) (SG90-180°) when:**

- Learning servo basics or quick prototyping
- Need position control (0-180°) for light-duty tasks
- Cost-sensitive project (cheapest option)
- Acceptable to replace if gears strip (plastic gears less durable)

**Choose [AC503](AC503.md) (SG90-360°) when:**

- Need continuous rotation, not position control
- Building wheeled robots or motorized mechanisms
- Want bidirectional variable-speed motor with simple PWM control
- Don't need precise speed regulation (speed varies with load)

## Common Applications

**Position Control (AC501, AC502):**

- **Robot arms/grippers**: Control joint angles precisely
- **Camera gimbals**: Pan/tilt mechanisms
- **Control surfaces**: RC planes (ailerons, rudder, elevator)
- **Mechanical linkages**: Flaps, doors, switches

**Continuous Rotation (AC503):**

- **Wheeled robots**: Differential drive with 2 servos
- **Conveyor belts**: Small-scale material transport
- **Rotating platforms**: Turrets, lazy susans
- **Bidirectional pumps**: Peristaltic or similar

---

## Components in This Family

{{ children() }}
