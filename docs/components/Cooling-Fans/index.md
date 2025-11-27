---
id: AC600
name: Cooling Fans
category: AC
tags:
  - family
  - fan
  - cooling
  - airflow
  - thermal
short: "Cooling Fans • 12V & 5V"
use: "Thermal management • Airflow"
---

# Cooling Fans - AC600

Small 25mm brushless DC cooling fans for active thermal management. Use these to cool voltage regulators, MOSFETs, enclosures, or any component that needs airflow. Available in 12V and 5V versions - choose based on your power supply. Control via MOSFET or relay module for PWM speed control.

## Comparison

| Component | Voltage | Current | Power | Speed | Airflow | Best For |
|-----------|---------|---------|-------|-------|---------|----------|
| [AC601](AC601.md) (12V Fan) | 12V | 60mA | 0.72W | 10k RPM | 2.1 CFM | High airflow, 12V projects |
| [AC602](AC602.md) (5V Fan) | 5V | ~100mA | 0.5W | ~8k RPM | ~1.5 CFM | Low voltage, USB power |

## Selection Guide

**[AC601](AC601.md) (12V Fan):** Higher speed and airflow, suitable for 12V power supply systems

**[AC602](AC602.md) (5V Fan):** Lower voltage, USB-compatible, easier integration with 5V logic

## Common Applications

**Voltage regulator cooling:** Attach fan to heatsink when using high-power buck/boost converters

**Enclosure ventilation:** Mount fan in case to exhaust hot air from electronics

**MOSFET cooling:** Cool high-current switching circuits (motor drivers, relay boards)

**3D printer hot-end cooling:** Layer cooling and hot-end thermal management

**Temperature-controlled cooling:** Use with temperature sensor and PWM for automatic fan speed control

## Wiring Notes

**Never connect fans directly to ESP32 GPIO!** Use a MOSFET driver circuit:

1. **Power:** Connect fan +V to appropriate voltage (5V or 12V)
2. **Switching:** Connect fan GND through N-channel MOSFET drain-source
3. **Control:** ESP32 GPIO → 100Ω → MOSFET gate (with 10kΩ pull-down)
4. **Protection:** Add flyback diode (1N4148/1N5819) across fan terminals
5. **Common ground:** Connect ESP32 GND to power supply GND

**PWM Speed Control:** Use ESP32 LEDC (25kHz typical) on MOSFET gate for variable speed

---

## Components in This Family

{{ children() }}
