---
id: RF300
name: Infrared
title: Infrared Communication
category: RF
tags:
  - infrared
  - ir
  - remote-control
  - wireless
short: "IR TX/RX • Remote control"
use: "remote control, IR communication"
no_label: true
---

# Infrared Communication - RF300

Infrared (IR) transmitter and receiver modules for wireless communication and remote control applications. Uses modulated 38 kHz infrared light for reliable short-range communication.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Function | Range | Best For |
|-----------|------|----------|-------|----------|
| [RF301](RF301.md) | Receiver | Decode IR signals | ~10m | Receive remote control commands |
| [RF302](RF302.md) | Transmitter | Send IR signals | ~10m | Control TVs, ACs, build remotes |

## Selection Guide

**For receiving remote control:**
- Use RF301 (IR Receiver)
- Decode TV/AC remote signals
- Learn and replay commands
- Universal remote projects

**For sending remote control:**
- Use RF302 (IR LED Transmitter)
- Control appliances
- Build custom remotes
- Automate TV/AC control

**Typical project:**
- Receiver (RF301) + Transmitter (RF302) together
- Learn codes from existing remote
- Replay codes to control devices

## Key Concepts

**Infrared light:**
- 940nm wavelength (invisible to eye)
- Not radio frequency (RF)
- Line-of-sight required
- Blocked by walls

**38 kHz modulation:**
- IR signal modulated at 38 kHz carrier
- Filters out ambient IR (sunlight, lamps)
- Standard for consumer remotes
- Receiver demodulates automatically

**IR protocols:**
- NEC (most common)
- Sony SIRC
- RC5/RC6 (Philips)
- Samsung
- Many manufacturer-specific

**Address + Command:**
- Each button sends unique code
- Address identifies device type (TV, AC, etc.)
- Command identifies button (power, vol+, etc.)

## How It Works

**Transmitter:**
1. MCU generates protocol-encoded signal
2. Modulates at 38 kHz carrier
3. IR LED pulses on/off rapidly
4. Invisible light beam transmitted

**Receiver:**
1. IR photodiode detects light
2. 38 kHz filter removes ambient IR
3. Demodulator extracts original signal
4. Clean digital output to MCU

## Gotchas

**IR Receivers:**
- Direct sunlight can overwhelm sensor
- Short range (~10m max)
- Line-of-sight required
- Protocol must match (use IR library to decode)

**IR Transmitters:**
- LED must be aimed at device
- Narrow beam angle (~20-30°)
- Distance limited (~10m)
- Multiple LEDs can increase range

## Typical Applications

**Universal remote:** Control TV, AC, stereo from one device.

**Home automation:** Automate appliances with IR control.

**IR repeater:** Extend range of remote controls.

**Learning remote:** Record and replay commands.

**IR communication:** Simple point-to-point data transfer.

**Proximity sensing:** Detect obstacles using IR reflection.
