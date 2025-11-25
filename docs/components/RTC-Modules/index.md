---
id: OT200
name: RTC Modules
category: OT
tags:
  - family
  - rtc
  - real-time-clock
  - timekeeping
  - battery-backup
short: "RTC Modules • Timekeeping"
use: "Date/time • Battery backup"
---

# RTC Modules - OT200

Real-time clock (RTC) modules for keeping accurate time and date even when the main power is off. Both modules use a 32.768 kHz crystal and CR2032 coin cell backup, providing years of battery life. Choose based on interface preference (3-wire vs I2C) and features needed (RAM size, square wave output).

## Comparison

| Component | Interface | Voltage | RAM | SQW Output | Backup Current | Best For |
|-----------|-----------|---------|-----|------------|----------------|----------|
| [OT201](OT201.md) (DS1302) | 3-wire serial | 2.0-5.5V | 31 bytes | No | <1 µW | Simple interface, wide voltage range |
| [OT202](OT202.md) (DS1307) | I2C (0x68) | 4.5-5.5V | 56 bytes NVRAM | Yes (1Hz-32kHz) | <500 nA | I2C bus sharing, timer interrupts |

## Selection Guide

**Choose [OT201](OT201.md) (DS1302) when:**

- Want simple 3-wire interface (RST, I/O, CLK) without I2C complexity
- Need wide voltage range (2.0-5.5V for battery-only operation)
- Prefer dedicated pins (no bus sharing needed)
- Don't need square wave output

**Choose [OT202](OT202.md) (DS1307) when:**

- Already using I2C bus (can share SDA/SCL with other devices)
- Need square wave output for timer interrupts (1Hz tick, etc.)
- Want more battery-backed RAM (56 vs 31 bytes)
- Standard I2C ecosystem compatibility preferred

## Common Applications

- **Data loggers**: Timestamp sensor readings with battery-backed timekeeping
- **Alarm clocks**: Use SQW output (DS1307) for 1Hz interrupt to update display
- **Scheduled tasks**: Wake microcontroller at specific times (irrigation, lighting control)
- **Event timestamping**: Log when sensors trigger (security, environmental monitoring)

---

## Components in This Family

{{ children() }}
