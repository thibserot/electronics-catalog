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

### GPIO Expansion (74HC595)

Use shift registers when your microcontroller runs out of GPIO pins. Common projects:
- **LED matrices**: Control 8×8 = 64 LEDs with just 5-6 microcontroller pins (using cascaded shift registers + multiplexing)
- **7-segment displays**: Drive multiple digits using only 3 control pins
- **Relay banks**: Control 8-16 relays for home automation
- **Cascading**: Connect Q7' output of one IC to DS input of next for unlimited expansion

### Timing & Oscillation (LMC555)

Use timers for standalone timing circuits or signal generation:
- **Astable mode (oscillator)**: LED blinker, clock generator, PWM dimming, tone generation
- **Monostable mode (one-shot)**: Timed delays, switch debouncing, pulse stretching
- **Low-power advantage**: CMOS version draws 50× less current than bipolar 555 (ideal for battery projects)

## Typical Wiring Patterns

### 74HC595 Basic Connection

```
74HC595    Microcontroller
--------   ---------------
DS     --> GPIO (MOSI/Data)
SHCP   --> GPIO (SCK/Clock)
STCP   --> GPIO (Latch)
VCC    --> 3.3V or 5V
GND    --> GND
MR     --> VCC (or GPIO for reset)
OE     --> GND (or GPIO for enable)
Q0-Q7  --> LEDs/outputs (with current-limiting resistors)
```

**Cascading:** Connect Q7' of first IC to DS of second IC. Share SHCP, STCP, MR, OE across all ICs.

### LMC555 Astable (LED Blinker)

```
VCC ----+---- R1 ----+---- THR (6) / TRIG (2)
        |            |       |
        |            R2      C1
        |            |       |
   RESET(4)    DISCH(7)     GND
        |
   0.01µF (CTRL filter)
        |
       GND

OUT (3) --> LED + resistor --> GND
```

**Note:** No microcontroller needed—timer runs autonomously with external R/C values.

## Projects Using This Family

- **LED matrices** (OT101): Control 64+ LEDs with cascaded shift registers
- **Digital clocks** (OT101 + OT102): Shift registers for display, 555 for time base
- **Relay control panels** (OT101): Expand 8-16 relay outputs from 3 GPIO pins
- **Pulse generators** (OT102): Generate precise pulses for stepper motors, servos
- **Battery-powered blinkers** (OT102): Low-power CMOS timer for long battery life

{{ children() }}
