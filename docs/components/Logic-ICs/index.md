---
id: OT100
name: Logic ICs
category: OT
tags:
  - family
  - logic-ic
  - shift-register
  - timer
  - digital
short: "Logic ICs • Shift register • Timer"
use: "GPIO expansion • Timing circuits"
---

# Logic ICs - OT100

General-purpose digital logic integrated circuits for expanding GPIO pins, generating timing signals, and building digital control circuits without microcontrollers.

## Comparison

| Component | Type | Function | Supply Voltage | Key Feature | Best For |
|-----------|------|----------|----------------|-------------|----------|
| [OT101](OT101.md) (74HC595) | Shift Register | Serial-to-parallel (8 outputs) | 2.0-6.0V | Cascadable, 3-pin control | GPIO expansion, LED control |
| [OT102](OT102.md) (LMC555) | Timer | Monostable/Astable | 1.5-12V | Low power CMOS, pin-compatible with NE555 | Timing circuits, PWM, oscillators |

## Selection Guide

**Choose OT101 (74HC595 Shift Register) when:**

- Need to expand GPIO pins (control 8+ outputs with only 3 microcontroller pins)
- Driving multiple LEDs, 7-segment displays, or LED matrices
- Want to cascade for 16, 24, 32+ outputs (virtually unlimited expansion)
- Need synchronized output updates (all pins latch simultaneously)

**Choose OT102 (LMC555 Timer) when:**

- Need timing delays or oscillating waveforms without microcontroller code
- Generating PWM signals, clock pulses, or pulse trains
- Low-power battery applications (CMOS draws ~100 µA vs ~5 mA for bipolar 555)
- Simple standalone circuits (LED blinker, buzzer, switch debouncer)
- Drop-in replacement for classic NE555/LM555 (pin-compatible)

## Common Applications

**GPIO Expansion (74HC595):**

- LED matrices: Control 8×8 = 64 LEDs with just 5-6 pins (cascaded shift registers + multiplexing)
- 7-segment displays: Drive multiple digits using only 3 control pins
- Relay banks: Control 8-16 relays for home automation

**Timing & Oscillation (LMC555):**

- Astable mode: LED blinker, clock generator, PWM dimming, tone generation
- Monostable mode: Timed delays, switch debouncing, pulse stretching
- Low-power advantage: CMOS draws 50× less current than bipolar 555 (ideal for battery projects)

---

## Components in This Family

{{ children() }}
