---
id: IO600
name: Audio Input Microphones
title: Audio Input Microphones
category: IO
tags:
  - audio
  - microphone
  - sound
  - voice
  - i2s
  - analog
short: "Audio capture • Sound level"
use: "voice input, sound detection"
---

# Audio Input Microphones - IO600

Microphone modules for audio capture and sound level detection. Includes analog electret microphones with amplifiers and digital I2S MEMS microphones.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Output | Interface | Quality | Best For |
|-----------|------|--------|-----------|---------|----------|
| [IO601](IO601.md) | Electret + Amp | Analog | ADC | Basic | Sound level, clap detection, VU meter |
| [IO602](IO602.md) | MEMS I2S | Digital | I2S | High | Voice recording, speech recognition |

## Selection Guide

**For simple sound detection:**
- Use IO601 (MAX4466) - analog
- Cheap, simple ADC reading
- Good for sound level, clap detection
- No audio recording needed

**For voice recording/recognition:**
- Use IO602 (INMP441) - I2S MEMS
- Digital audio stream
- Better quality, no ADC noise
- Required for speech-to-text

**For music/high quality:**
- Use IO602 (I2S MEMS)
- Wider frequency response
- Lower noise floor
- Better SNR (signal-to-noise ratio)

## Key Concepts

**Electret microphone:**
- Analog voltage output
- Requires amplification (very weak signal)
- Simple circuit, cheap
- Limited frequency response

**MEMS (Micro-Electro-Mechanical Systems):**
- Tiny silicon microphone
- Digital I2S output
- Better specs, more expensive
- Standard for smartphones

**I2S (Inter-IC Sound):**
- Serial audio protocol
- Transmits digital audio data
- Used for DACs, ADCs, microphones
- Synchronous (clock + data)

**Gain:**
- Amplification factor for microphone signal
- Too low = weak signal, noise dominates
- Too high = clipping, distortion
- Adjustable via potentiometer or software

## Gotchas

**Analog microphones (IO601):**
- ADC noise affects quality
- Requires calibration for absolute levels
- Gain adjustment critical
- AC coupled (DC offset ~1.65V)

**I2S microphones (IO602):**
- More complex code (I2S driver)
- Not all MCUs have I2S hardware
- Clock timing critical
- Higher cost

## Typical Applications

**Analog (IO601):**
- Sound level meter (dB meter)
- Clap-activated lights
- VU meter / audio visualizer
- Noise monitoring
- Simple voice activation (threshold)

**I2S Digital (IO602):**
- Voice recording
- Speech recognition (Google Assistant, Alexa)
- Intercom systems
- Baby monitor
- High-quality audio sampling
