---
id: IO700
name: Displays
title: Displays
category: IO
tags:
  - display
  - oled
  - lcd
  - seven-segment
  - i2c
short: "Visual output • Text & graphics"
use: "information display, user interface"
no_label: true
---

# Displays - IO700

Display modules for showing text, numbers, and graphics. Includes OLED displays, LCD character displays, and 7-segment numeric displays.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Resolution | Size | Interface | Best For |
|-----------|------|------------|------|-----------|----------|
| [IO701](IO701.md) | OLED Graphic | 128x64 | 0.96" | I2C | Small projects, graphics |
| [IO702](IO702.md) | OLED Graphic | 128x64 | 1.3" | I2C | Larger display, easier reading |
| [IO703](IO703.md) | LCD Character | 16x2 chars | 80x36mm | I2C | Text messages, menus |
| [IO704](IO704.md) | 7-Segment LED | 4 digits | 30x14mm | 2-wire | Numbers, clock, counter |

## Selection Guide

**For graphics/icons:**
- Use IO701 or IO702 (OLED)
- Pixel-addressable
- Draw shapes, images, graphs

**For simple text display:**
- Use IO703 (LCD 16x2)
- Larger characters
- Lower power
- Backlight adjustable

**For numbers only (clock, counter):**
- Use IO704 (7-segment)
- Very bright
- Easy to read from distance
- Simple interface

**For low power:**
- OLED (IO701/IO702) - only lit pixels use power
- Turn off when idle

**For outdoor/bright light:**
- 7-segment LED (IO704) - brightest
- LCD struggles in direct sun
- OLED better than LCD outdoors

## Key Concepts

**OLED (Organic LED):**
- Each pixel emits light
- No backlight needed
- High contrast, deep blacks
- Limited lifespan (~10,000 hours)

**LCD (Liquid Crystal Display):**
- Requires backlight
- Reflective display (readable without power)
- Character-based (fixed font)
- Very long lifespan

**I2C interface:**
- 2-wire connection (SDA/SCL)
- Multiple displays on same bus
- Slower than SPI
- Address conflicts possible

**7-Segment:**
- 7 LED segments per digit
- Can show 0-9, A-F, some letters
- Bright, easy to read
- Limited character set

## Gotchas

**OLED displays:**
- Burn-in if static image displayed constantly
- Limited lifespan (use timers to turn off)
- Small screens hard to read (0.96" tiny!)
- Clones vary in quality (SSD1306 vs SH1106 controllers)

**LCD displays:**
- Backlight always on (higher power)
- Contrast adjustment needed (pot on back)
- Cold temperatures slow response
- Limited to character set (can't draw graphics)

**7-Segment:**
- Only numbers and limited letters
- Requires more GPIO pins (or use driver IC)
- Very bright (high current)

## Typical Applications

**OLED (IO701/IO702):**
- Sensor dashboards
- Weather stations
- Menu systems
- Logo display
- Graphs/charts

**LCD (IO703):**
- Status messages
- Temperature displays
- Configuration menus
- Name tags
- Simple UI

**7-Segment (IO704):**
- Clocks
- Counters
- Timers
- Score displays
- Temperature (numeric)
