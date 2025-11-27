---
id: AC800
name: Audio Output
category: AC
tags:
  - family
  - audio
  - speaker
  - buzzer
  - amplifier
  - sound
short: "Audio Output • Speakers & Buzzers"
use: "Sound generation • Alerts"
---

# Audio Output - AC800

Components for generating sound, from simple beeps and alerts to amplified audio playback. Choose between speakers (need amplifier), buzzers (self-contained or passive), piezo elements (vibration/sound), or amplifier modules for connecting speakers.

## Comparison

| Component | Type | Power | Interface | Volume | Best For |
|-----------|------|-------|-----------|--------|----------|
| [AC801](AC801.md) (Speaker) | 8Ω 0.5W | Requires amp | Analog audio | Medium | Music/voice with LM386/PAM8302 |
| [AC802](AC802.md) (Piezo) | Passive disc | Direct/amp | Voltage flex | Quiet | Vibration sensing or click/beep |
| [AC803](AC803.md) (Passive Buzzer) | Magnetic/piezo | PWM required | Square wave | Medium | Tones, melodies, alarms |
| [AC804](AC804.md) (LM386 Amp) | Amplifier module | 5-12V | Analog audio | Medium | Drive speakers from DAC/audio |
| [AC805](AC805.md) (Active Buzzer) | Self-oscillating | Direct DC | 3-5V DC | Loud | Simple beep, fixed frequency |

## Selection Guide

**[AC801](AC801.md) (Speaker):** Best for music, voice, or audio playback - requires amplifier module (use with AC804)

**[AC802](AC802.md) (Piezo Elements):** Dual-purpose: vibration/knock sensor OR very quiet buzzer

**[AC803](AC803.md) (Passive Buzzer):** Generate tones and melodies with PWM control

**[AC804](AC804.md) (LM386 Amplifier):** Drive speakers from ESP32 DAC or audio sources

**[AC805](AC805.md) (Active Buzzer):** Simplest option - just apply DC voltage for instant beep

## Common Applications

**Alert/notification sounds:** AC805 (active buzzer) for simple beeps, AC803 (passive) for custom tones

**Music/audio playback:** AC801 (speaker) + AC804 (LM386 amp) + ESP32 DAC

**Knock/vibration detection:** AC802 (piezo element) as sensor

**User interface feedback:** AC803 (passive buzzer) with PWM for button clicks, menu navigation

**Voice output:** AC801 (speaker) + AC804 (amplifier) + audio library (e.g., ESP8266Audio)

---

## Components in This Family

{{ children() }}
