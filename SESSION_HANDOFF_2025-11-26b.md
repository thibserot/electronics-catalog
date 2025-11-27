# Session Handoff - Electronics Catalog Migration
**Date:** 2025-11-26 (Session 2)
**Project:** Electronics Catalog Family Migration
**Current Phase:** Phase 3 - Continued Progress

## Project Overview

Git-versioned electronics catalog built with MkDocs Material. Migrating individual components into family-based organization with QR sticker generation for physical component storage.

**Repository:** `/home/thibanir/Project/electronics-catalog/`
**Branch:** `main` (fully synced with origin)

## Current Status

### ✅ Completed Families (15 families, 53+ components)

1. **SW201** - Touch Sensors (1 component)
   - SW201: TTP223 Touch Sensor

2. **RF101** - RFID Readers (1 component)
   - RF101: MFRC522 RFID Reader

3. **ENV2xx** - Air Quality & Gas Sensors (5 components)
   - ENV200: Family anchor
   - ENV201-ENV205: MQ-series gas sensors
   - Location: `docs/components/Environmental/Air-Quality/`

4. **OT1xx** - Logic ICs (3 components)
   - OT100: Family anchor
   - OT101: 74HC595 Shift Register
   - OT102: LMC555 Timer
   - Location: `docs/components/Logic-ICs/`

5. **OT2xx** - RTC Modules (3 components)
   - OT200: Family anchor
   - OT201: DS1302 RTC (3-wire)
   - OT202: DS1307 RTC (I2C)
   - Location: `docs/components/RTC-Modules/`

6. **AC5xx** - Servos (4 components)
   - AC500: Family anchor
   - AC501: SG92R (metal gear, 2.5 kg·cm)
   - AC502: SG90 180° (plastic gear, 1.8 kg·cm)
   - AC503: SG90-360° (continuous rotation)
   - Location: `docs/components/Servos/`

7. **ENV3xx** - Light Sensors (5 components)
   - ENV300: Family anchor
   - ENV301: TSL2561 (0.1-40k lux, I2C)
   - ENV302: TSL2591 (188µ-88k lux, extreme range)
   - ENV303: BH1750 (1-65k lux, low power)
   - ENV304: Photoresistor (migrated from ENV002, analog)
   - Location: `docs/components/Environmental/Light/`

8. **PS3xx** - LDO Regulators (3 components)
   - PS300: Family anchor
   - PS301: MCP1700 (3.3V, 1.6µA Iq, TO-92)
   - PS302: HT7333 (3.3V, 3.5µA Iq, SOT-89, 12V max)
   - Location: `docs/components/LDO/`

9. **PS1xx** - DC-DC Converters (4 components)
   - PS100: Family anchor
   - PS101: TPS63020 Buck-Boost (1.8-5.5V → 3.3V, 2A)
   - PS102: 5V Buck Converter (5-30V → 5V, 3A)
   - PS103: Boost Converter (3.7V → 5-12V, 0.3-1A)
   - Location: `docs/components/DC-DC-Converters/`
   - Note: Moved from PS0xx range to free up PS0xx

10. **PA004** - Schottky Diodes (1 component)
    - PA004: 8-value diode kit (1N4148, 1N4007, 1N5819, etc.)
    - Recovered from accidental PS101 overwrite
    - Location: `docs/components/PA004.md`

11. **PS2xx** - Battery Charging (3 components)
    - PS200: Family anchor
    - PS201: TP4056 USB charger (5V, 1A, can work with solar)
    - PS202: CN3065 Solar charger (4.4-6V panel, 500mA)
    - Location: `docs/components/Battery Charging/`

12. **MC1xx** - ESP32 Boards (8 components)
    - MC100: Family anchor with key boards comparison
    - MC101: ESP32-C3 SuperMini (RISC-V, compact)
    - MC102: ESP32-S3 SuperMini (dual Xtensa, high performance)
    - MC103: ESP32 CAM OV5640 (5MP camera)
    - MC104: ESP32 WROOM-32D DevKit (standard dev board)
    - MC105-107: Additional ESP32 variants
    - Location: `docs/components/esp32/`

13. **AC2xx** - Transistors (11 components)
    - AC200: Family anchor
    - AC201-210: BJT components (BC337, BC327, 2N2222, 2N2907, 2N3904, 2N3906, S8050, S8550, A1015, C1815)
    - Location: `docs/components/Bipolar Junction Transistor/`
    - Note: Stickers kept unchanged (no reprinting needed)

14. **IO1xx** - Magnetic Sensors (3 components)
    - IO100: Family anchor
    - IO101: GPS-14A Reed Switch (passive, no power)
    - IO102: A3144E Hall Effect (solid-state, bounce-free)
    - Location: `docs/components/Magnetic Sensors/`

15. **SW1xx** - Physical Switches & Buttons (8 components) ← **Latest migration**
    - SW100: Family anchor
    - SW101: MX mechanical switches (3-pin, keyboard prototyping)
    - SW102: Tact switch kit (25 types, SMD+DIP)
    - SW103: Mini toggle switch (SPDT, ON-ON/ON-OFF-ON)
    - SW104: Momentary pushbutton (12mm panel, pre-wired)
    - SW105: LED pushbutton (16mm panel, illuminated)
    - SW106: Mini rocker switch (SPST, pre-wired)
    - SW107: Mini rocker switch (SPST, 10×15mm)
    - Location: `docs/components/Switches & Buttons/`

## 🖨️ Sticker Status

**All stickers have been printed!** 🎉

No unpublished stickers currently. The next migration will accumulate new stickers for the next print batch.

## Key Patterns & Conventions

### Front-Matter Format
```yaml
---
id: ENV301                    # Component ID (CCNNN format)
name: TSL2561                 # Short name for navigation
title: TSL2561 (Light Sensor) # Optional page title override
category: ENV                 # 2-letter category code
tags:
  - light-sensor              # Lowercase, hyphenated
  - i2c
  - esp32-compatible          # Platform compatibility
  - arduino-compatible
short: "Light sensor"         # Sticker line 1 (concise, generic type)
use: "0.1-40k lux • I2C"     # Sticker line 2 (specs/interface)
---
```

### Family Index Structure
```markdown
# Family Name - CCXX00

Brief intro paragraph explaining the family and selection criteria.

## Comparison

| Component | Key Spec | Interface | Best For |
|-----------|----------|-----------|----------|
| [CC101](CC101.md) | ... | ... | ... |

## Selection Guide

**[CC101](CC101.md):** One-line recommendation with specific use case.

**[CC102](CC102.md):** One-line recommendation with specific use case.

## Common Applications

**Use case 1:** Brief description with recommended component.

**Use case 2:** Brief description with recommended component.

---

## Components in This Family

{{ children() }}
```

### Important Rules

1. **Blank lines before lists**: ALWAYS add blank line after headers before bullet lists
2. **Sticker format**:
   - `short`: Generic type (e.g., "Light sensor", "LDO regulator")
   - `use`: Key specs and interface (e.g., "0.1-40k lux • I2C")
3. **Tags**: Use lowercase with hyphens, include `esp32-compatible` and `arduino-compatible`
4. **AliExpress links**: Use actual product URLs, not search pages
5. **No "Other" folder**: Use descriptive folder names at root level
6. **Sticker paths**: Adjust depth based on folder nesting:
   - Root level: `../stickers/ID.png`
   - 2-level: `../stickers/ID.png`
   - 3-level: `../../stickers/ID.png`

## CPU Architecture Notes (ESP32)

**RISC-V** (ESP32-C3, C6):
- Open-source architecture, no licensing fees
- Generally lower power consumption
- Single-core on C3 (160MHz)
- Different toolchain from Xtensa

**Xtensa** (ESP32, ESP32-S2, ESP32-S3):
- Proprietary architecture by Cadence/Tensilica
- Dual-core available (240MHz)
- More mature ecosystem
- Better library support

**Why it matters:**
- Code compatibility: Xtensa boards easier to port between
- Power: RISC-V more efficient for battery projects
- Performance: Dual-core Xtensa better for multitasking

## Remaining Families to Migrate

### Unmigrated Components at Root Level

**Actuators (AC)** - 9 unmigrated components:
- AC001-008, AC010 (fans, motors, relays, MOSFET boards, etc.)
- Could create AC0xx or AC1xx families for different actuator types

**Connectors (CN)** - 4 unmigrated components:
- CN001-004
- Could create CN1xx family if components are similar enough

**Passive Components (PA)** - 3 unmigrated components:
- PA001-003 (plus PA004 already migrated)
- Resistors, capacitors, potentiometers, trim pots

**Other/Misc (OT)** - 2 unmigrated components:
- OT001-002 (plus OT1xx and OT2xx families already created)

**RF Communications** - 2 unmigrated components:
- RF002: WiFi antenna (2.4 GHz, passive)
- RF003: USR-ES1 W5500 (SPI Ethernet module)
- RF101 already in its own family
- Note: RF002/003 are quite different, may not warrant family yet

**Environmental (ENV)** - 1 unmigrated component:
- ENV001 (plus ENV2xx and ENV3xx families already created)

**I/O (IO)** - 1 unmigrated component:
- IO003 (plus IO1xx family already created)

**Temperature Sensors (TS)** - 1 component:
- TS001: DS18B20
- Need TS002+ before creating family

### Available ID Ranges

- **PS0xx range** - Now available for future power supply families (freed up during PS1xx migration)

## Session History (2025-11-26, Session 2)

### Commit Made

1. `49bd793` - Add SW1xx: Physical Switches & Buttons family

All commits pushed to origin/main successfully.

### Key Changes

- Migrated SW001-007 → SW101-107 into new "Switches & Buttons" folder
- Created comprehensive SW100 anchor with comparison table
- Standardized all tags and sticker metadata
- Fixed markdown rendering issues (blank lines)
- Generated 8 new stickers (SW100-107)
- Updated registry files

## Workflow for Next Session

1. **Identify next family** - Check remaining unmigrated components
2. **Create family structure** - Folder, anchor page, migrate components
3. **Standardize components** - Tags, sticker metadata, blank lines
4. **Generate stickers** - `make registry_stickers`
5. **Commit and push** - Follow commit message pattern

### Registry and Sticker Generation

```bash
# Generate registry and stickers (also runs automatically on commit via pre-commit hook)
make registry_stickers

# Or run steps individually:
python scripts/generate_id_registry.py
python scripts/build_registry_page.py
python scripts/build_labels.py

# Preview local site
make serve
```

### Sticker Generation for Specific IDs

```bash
# Generate stickers for specific components only
python scripts/build_labels.py --ids ID1,ID2,ID3

# Example for thermal printer sheets with padding
python scripts/build_labels.py --output-prefix migration --pad-sheets --ids ID1,ID2,ID3
```

## Important Files

- **SESSION_HANDOFF_2025-11-25.md**: First session notes from previous context
- **SESSION_HANDOFF_2025-11-26.md**: Second session notes (previous session)
- **SESSION_HANDOFF_2025-11-26b.md**: This file (current session)
- **MIGRATION_PLAN.md**: Original migration roadmap
- **CLAUDE.md**: Project architecture and conventions
- **scripts/build_labels.py**: Sticker generation script
- **docs/components/stickers/id_registry_simple.yaml**: Quick ID reference

## Git Status

```
Branch: main
Status: Synced with origin/main
Last commit: "Add SW1xx: Physical Switches & Buttons family" (49bd793)
Pre-commit hook: Active (auto-runs make registry_stickers)
```

## Next Available IDs (from registry)

- **TS**: TS002 (only 1 component, no families yet)
- **ENV**: ENV002 (root), ENV203 (ENV2xx), ENV305 (ENV3xx)
- **PS**: PS001 (root), PS104 (PS1xx), PS203 (PS2xx), PS303 (PS3xx)
- **MC**: MC001 (root), MC108 (MC1xx)
- **RF**: RF001 (root), no families beyond RF101
- **IO**: IO001 (root), IO103 (IO1xx)
- **AC**: AC009 (root), AC211 (AC2xx), AC504 (AC5xx)
- **CN**: CN005 (4 components, no families)
- **PA**: PA005 (4 components, no families)
- **OT**: OT003 (root), OT103 (OT1xx), OT203 (OT2xx)
- **SW**: SW001 (root), SW108 (SW1xx)

## Component Statistics

- **Total components**: 53+ across 15 families
- **Total families**: 15 (with anchors)
- **Largest category**: AC (Actuators) - 24 components
- **Smallest categories**: TS, SW201, RF101, PA004 - 1 component each
- **Most organized category**: SW (9 components, 1 family created)
- **Stickers printed**: All current stickers (85 total)

## Questions for Next Session

1. Continue creating new families from unmigrated components?
2. Which category to tackle next? (CN, RF, AC0xx, or others?)
3. Any specific components to prioritize?

## Preview

**Local server:** http://127.0.0.1:8000
**GitHub Pages:** https://thibserot.github.io/electronics-catalog/

---

**Ready to continue!** All existing families with multiple components have been successfully migrated. The catalog is well-organized and all stickers have been printed. Ready to continue organizing remaining components into new families as inventory grows.
