---
id: IO300
name: Rotary Encoders & Joysticks
title: Rotary Encoders & Joysticks
category: IO
tags:
  - input
  - rotary-encoder
  - joystick
  - user-interface
short: "Rotary input • Joystick XY"
use: "user interface control"
---

# Rotary Encoders & Joysticks - IO300

Rotary encoders and analog joysticks for user input and control interfaces. Encoders provide incremental rotation sensing with optional push buttons, while joysticks offer 2-axis analog positioning.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Features | Interface | Best For |
|-----------|------|----------|-----------|----------|
| [IO301](IO301.md) | Rotary Encoder | 20 steps/rev, push button | 2x GPIO + 1x button | Volume control, menu navigation |
| [IO302](IO302.md) | Rotary Encoder Module | Clickable, pull-ups included | 3x GPIO (CLK/DT/SW) | Breadboard projects |
| [IO303](IO303.md) | Joystick Module | 2-axis analog + button | 2x ADC + 1x GPIO | Game controllers, robot control |

## Selection Guide

**For menu navigation:**
- Use IO301 or IO302 (rotary encoder)
- Provides incremental steps with detents
- Optional push button for "select"

**For volume/brightness control:**
- Use rotary encoder (IO301/IO302)
- Smooth incremental adjustment
- Better UX than buttons

**For XY positioning:**
- Use IO303 (joystick)
- Analog 2-axis control
- Self-centering spring return

**For game controllers:**
- Use IO303 (joystick)
- Familiar game controller interface
- Center push button for "fire"

## Key Concepts

**Rotary Encoder Operation:**
- Quadrature output (A/B channels)
- Detects direction by phase relationship
- Steps determined by physical detents
- No absolute position (incremental only)

**Joystick Operation:**
- Two potentiometers (X and Y axis)
- Center position ~2.5V (mid-point)
- Push moves toward 0V or 3.3V
- Returns to center when released

## Gotchas

**Rotary Encoders:**
- Require interrupt-based reading for reliability
- Debouncing needed for clean edges
- Fast rotation can skip steps if polling too slow
- CLK/DT pins must be read together for direction

**Joysticks:**
- Center position varies (not exactly 512 on 10-bit ADC)
- Dead zone recommended around center
- Needs calibration for min/max values
- Pressing button slightly moves analog position
