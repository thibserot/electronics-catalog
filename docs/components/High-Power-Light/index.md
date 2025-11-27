---
id: AC900
name: High-Power Light
category: AC
tags:
  - family
  - led
  - laser
  - high-power
  - lighting
  - illumination
short: "High-Power LEDs & Lasers"
use: "Illumination • Indicators • Pointing"
---

# High-Power LEDs & Lasers - AC900

High-power light sources for illumination, bright indicators, and laser modules. These components require proper current regulation (constant-current drivers for LEDs) or voltage regulation (for laser modules) and often generate significant heat. Use heatsinks for continuous operation.

## Comparison

| Component | Type | Power | Output | Driver Required | Best For |
|-----------|------|-------|--------|-----------------|----------|
| [AC901](AC901.md) (XPG3 LED) | High-power LED | 7W | 777 lm | Constant current | Flashlights, spotlights, bright indicators |
| [AC902](AC902.md) (Laser Diode) | Laser module | 5mW | 650nm red | Voltage regulated | Alignment, pointing, distance sensing |
| [AC903](AC903.md) (KY-008) | Laser module | <5mW | 650nm red | Built-in driver | Quick laser projects, line generation |

## Selection Guide

**[AC901](AC901.md) (XPG3 7W LED):** Brightest option for illumination, requires proper heatsinking and constant-current driver

**[AC902](AC902.md) (Laser Diode Module):** Bare laser diode, needs external driver circuit, more control over current

**[AC903](AC903.md) (KY-008 Laser Module):** Ready-to-use laser module with built-in driver, simplest to wire

## Common Applications

**Bright flashlights/spotlights:** AC901 with proper heatsink and driver

**Laser alignment/leveling:** AC902 or AC903 for straight line projection

**Distance sensing:** AC902 + photodiode for TOF or triangulation

**Laser engraving (low power):** AC902 with modulation control

**Line/cross generators:** AC903 with line/cross lens attachment

## Safety Warnings

**LEDs:**

- High-power LEDs get HOT - always use heatsinks for continuous operation
- Never drive directly from GPIO - use constant-current LED driver
- Protect eyes from direct viewing at close range

**Lasers:**

- Class 2 lasers (<5mW) are generally safe but avoid direct eye exposure
- Never point at people, animals, aircraft, or reflective surfaces
- Use proper enclosures and safety interlocks for higher-power applications
- Check local regulations for laser use and classification

---

## Components in This Family

{{ children() }}
