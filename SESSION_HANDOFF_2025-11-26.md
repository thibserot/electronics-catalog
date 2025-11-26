# Session Handoff - Electronics Catalog Migration
**Date:** 2025-11-26
**Project:** Electronics Catalog Family Migration
**Current Phase:** Phase 3 - Continued Progress

## Project Overview

Git-versioned electronics catalog built with MkDocs Material. Migrating individual components into family-based organization with QR sticker generation for physical component storage.

**Repository:** `/home/thibanir/Project/electronics-catalog/`
**Branch:** `main` (fully synced with origin)

## Current Status

### ✅ Completed Families (14 families, 45+ components)

1. **SW201** - Touch Sensors (1 component)
   - SW201: TTP223 Touch Sensor

2. **RF101** - RFID Readers (1 component)
   - RF101: MFRC522 RFID Reader

3. **ENV2xx** - Air Quality & Gas Sensors (5 components)
   - ENV201-ENV205: MQ-series gas sensors
   - Location: `docs/components/Environmental/Air-Quality/`

4. **OT1xx** - Logic ICs (2 components)
   - OT100: Family anchor
   - OT101: 74HC595 Shift Register
   - OT102: LMC555 Timer
   - Location: `docs/components/Logic-ICs/`

5. **OT2xx** - RTC Modules (2 components)
   - OT200: Family anchor
   - OT201: DS1302 RTC (3-wire)
   - OT202: DS1307 RTC (I2C)
   - Location: `docs/components/RTC-Modules/`

6. **AC5xx** - Servos (3 components)
   - AC500: Family anchor
   - AC501: SG92R (metal gear, 2.5 kg·cm)
   - AC502: SG90 180° (plastic gear, 1.8 kg·cm)
   - AC503: SG90-360° (continuous rotation)
   - Location: `docs/components/Servos/`

7. **ENV3xx** - Light Sensors (4 components) ← **First unpublished stickers**
   - ENV300: Family anchor
   - ENV301: TSL2561 (0.1-40k lux, I2C)
   - ENV302: TSL2591 (188µ-88k lux, extreme range)
   - ENV303: BH1750 (1-65k lux, low power)
   - ENV304: Photoresistor (migrated from ENV002, analog)
   - Location: `docs/components/Environmental/Light/`

8. **PS3xx** - LDO Regulators (2 components)
   - PS300: Family anchor
   - PS301: MCP1700 (3.3V, 1.6µA Iq, TO-92)
   - PS302: HT7333 (3.3V, 3.5µA Iq, SOT-89, 12V max)
   - Location: `docs/components/LDO/`

9. **PS1xx** - DC-DC Converters (3 components)
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

11. **PS2xx** - Battery Charging (2 components)
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

13. **AC2xx** - Transistors (10 components)
    - AC200: Family anchor
    - AC201-210: BJT components (BC337, BC327, 2N2222, 2N2907, 2N3904, 2N3906, S8050, S8550, A1015, C1815)
    - Location: `docs/components/Bipolar Junction Transistor/`
    - Note: Stickers kept unchanged (no reprinting needed)

14. **IO1xx** - Magnetic Sensors (2 components) ← **Latest migration**
    - IO100: Family anchor
    - IO101: GPS-14A Reed Switch (passive, no power)
    - IO102: A3144E Hall Effect (solid-state, bounce-free)
    - Location: `docs/components/Magnetic Sensors/`

## 🖨️ Unpublished Stickers (Need Printing)

Since ENV3xx Light Sensors, **21 components** need stickers printed:

### Sticker Generation Command

```bash
python scripts/build_labels.py --ids ENV301,ENV302,ENV303,ENV304,PS301,PS302,PS101,PS102,PS103,PA004,PS201,PS202,MC101,MC102,MC103,MC104,MC105,MC106,MC107,IO101,IO102
```

**Breakdown:**
- ENV3xx: ENV301, ENV302, ENV303, ENV304 (4 stickers)
- PS3xx: PS301, PS302 (2 stickers)
- PS1xx: PS101, PS102, PS103 (3 stickers)
- PA004: PA004 (1 sticker)
- PS2xx: PS201, PS202 (2 stickers)
- MC1xx: MC101-107 (7 stickers)
- IO1xx: IO101, IO102 (2 stickers)

**Total: 21 stickers**

Note: Family anchors (ENV300, PS300, PS100, PS200, MC100, IO100) don't get stickers - they're index pages only.

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

### High Priority (Have Components, Need Migration)

**None remaining!** All existing families with components have been migrated.

### Future Expansion Opportunities

1. **Temperature Sensors (TS)** - Only 1 component currently (TS002 next)
2. **RF Communications** - 3 components, could organize into families
3. **Connectors (CN)** - 4 components
4. **Switches & Buttons (SW)** - 8 components
5. **Additional PS ranges** - PS0xx now available for future use

## Session History (2025-11-26)

### Commits Made (7 total)
1. `e9e0c82` - Add PS3xx: LDO Regulators family
2. `757319c` - Move DC-DC converters from PS0xx to PS1xx range
3. `2d5fa7d` - Fix PS1xx migration issues and recover PA004 Schottky diodes
4. `e5c1ec5` - Add PS2xx Battery Charging and MC1xx ESP32 families
5. `055698f` - Fix PS2xx and MC1xx documentation issues
6. `3ea21dd` - Add AC2xx: Transistors family migration
7. `d3521f0` - Add IO1xx: Magnetic Sensors family migration

All commits pushed to origin/main successfully.

### Key Fixes Applied
- Recovered PA004 Schottky diodes from accidental PS101 overwrite
- Fixed PS101/PS102 markdown rendering issues
- Updated PS201 to mention solar compatibility
- Fixed PS202 AliExpress link
- Fixed IO101/IO102 ID typos in headers
- Standardized tags across all families

## Workflow for Next Session

1. **Check unpublished stickers count** - Currently 21 components
2. **Pick next family** - Consider creating new families (TS, RF, SW, CN)
3. **Generate stickers** - Use command above after reaching desired count
4. **Optional: Create migration sheets** - For thermal printer with `--pad-sheets`

### Migration Sheet Command (if needed)
```bash
python scripts/build_labels.py --output-prefix migration --pad-sheets \
  --ids ENV301,ENV302,ENV303,ENV304,PS301,PS302,PS101,PS102,PS103,PA004,PS201,PS202,MC101,MC102,MC103,MC104,MC105,MC106,MC107,IO101,IO102
```

## Important Files

- **SESSION_HANDOFF_2025-11-25.md**: Previous session notes
- **SESSION_HANDOFF_2025-11-26.md**: This file (current session)
- **MIGRATION_PLAN.md**: Original migration roadmap
- **CLAUDE.md**: Project architecture and conventions
- **scripts/build_labels.py**: Sticker generation script
- **docs/components/stickers/id_registry_simple.yaml**: Quick ID reference

## Git Status

```
Branch: main
Status: Synced with origin/main
Last commit: "Add IO1xx: Magnetic Sensors family migration" (d3521f0)
Pre-commit hook: Active (auto-runs make registry_stickers)
```

## Questions for Next Session

1. Should we create new families (Temperature, RF, Switches) or continue organizing existing components?
2. How many stickers do you want to accumulate before printing? (Currently 21)
3. Any specific components or families you want to prioritize?

## Preview

**Local server:** http://127.0.0.1:8000
**GitHub Pages:** https://thibserot.github.io/electronics-catalog/

---

**Ready to continue!** All families with existing components have been successfully migrated to the new structure with comparison tables, selection guides, and common applications. The catalog is well-organized and ready for expansion.
