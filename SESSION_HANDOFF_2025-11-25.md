# Session Handoff - Electronics Catalog Migration
**Date:** 2025-11-25
**Project:** Electronics Catalog Family Migration
**Current Phase:** Phase 3 - In Progress

## Project Overview

This is a Git-versioned electronics catalog built with MkDocs Material. We're migrating individual components into family-based organization with QR sticker generation for physical component storage.

**Repository:** `/home/thibanir/Project/electronics-catalog/`
**Branch:** `main` (18+ commits ahead of origin)

## Current Status

### ✅ Completed Families (7 families, 18 components)

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

7. **ENV3xx** - Light Sensors (4 components) ← **Just completed!**
   - ENV300: Family anchor
   - ENV301: TSL2561 (0.1-40k lux, I2C)
   - ENV302: TSL2591 (188µ-88k lux, extreme range)
   - ENV303: BH1750 (1-65k lux, low power)
   - ENV304: Photoresistor (migrated from ENV002, analog)
   - Location: `docs/components/Environmental/Light/`

### 📦 Migration Sheets

Custom sticker sheets generated with `--output-prefix migration --pad-sheets`:
- **migration_001.png** through **migration_004.png** (4 sheets, 15 stickers)
- All sheets padded to exactly 4 stickers for zero-waste thermal printing

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
short: "Light sensor"         # Sticker line 1 (concise!)
use: "0.1-40k lux • I2C"      # Sticker line 2 (specs/interface)
---
```

### Sticker Guidelines
- **Line 1 (short):** Generic type (e.g., "Light sensor", "Servo", "RTC")
- **Line 2 (use):** Key specs + interface (e.g., "0.1-40k lux • I2C", "180° • 1.8 kg·cm")
- Keep both lines concise - space is limited on 384px stickers
- Industry abbreviations OK when space-constrained (e.g., "9g" for weight on servo stickers)

### Markdown Rendering Rules
**CRITICAL:** Always add blank line before bullet lists, especially after bold headers:

```markdown
**Good:**
**Important:**

- Bullet point here

**Bad (won't render):**
**Important:**
- Bullet point here
```

### Family Index Structure
```markdown
# Family Name - CCXX00

Brief intro paragraph

## Comparison
| Component | Key Spec | Interface | Best For |
|-----------|----------|-----------|----------|
| [CC101](CC101.md) | ... | ... | ... |

## Selection Guide
**[CC101](CC101.md):** One-line recommendation

**[CC102](CC102.md):** One-line recommendation

## Common Applications
**Use case 1:** Brief description (recommended component)

**Use case 2:** Brief description (recommended component)

---

## Components in This Family

{{ children() }}
```

**Important:** Don't repeat detailed wiring/specs from component pages. Family page is for comparison only.

### Sticker Path Depth
- **Root level** (e.g., `docs/components/SW201.md`): `../stickers/SW201.png`
- **2-level deep** (e.g., `docs/components/Logic-ICs/OT101.md`): `../stickers/OT101.png`
- **3-level deep** (e.g., `docs/components/Environmental/Light/ENV301.md`): `../../stickers/ENV301.png`

### AliExpress Links
- ✅ Use actual product links: `https://www.aliexpress.com/item/1005006811956625.html`
- ❌ Don't use search pages: `https://www.aliexpress.com/w/wholesale-tsl2561`

### Platform Tags
- Use simple tags: `esp32-compatible`, `arduino-compatible`
- Avoid overly technical tags (e.g., "astable", "monostable" removed - not DIYer-friendly)
- Remove weight tags like "9g" (not useful for search, but OK in text/stickers)

## Folder Structure

```
docs/components/
├── Servos/
│   ├── index.md (AC500)
│   ├── AC501.md
│   ├── AC502.md
│   └── AC503.md
├── Logic-ICs/
│   ├── index.md (OT100)
│   ├── OT101.md
│   └── OT102.md
├── RTC-Modules/
│   ├── index.md (OT200)
│   ├── OT201.md
│   └── OT202.md
├── Environmental/
│   ├── Air-Quality/
│   │   ├── index.md (ENV200)
│   │   └── ENV201-205.md
│   └── Light/
│       ├── index.md (ENV300)
│       └── ENV301-304.md
└── stickers/
    ├── *.png (individual stickers)
    ├── sheet_*.png (regular sheets)
    ├── migration_*.png (custom migration sheets)
    ├── id_registry.yaml
    └── id_registry_simple.yaml
```

**Note:** No "Other" folder - families at root level (e.g., `Logic-ICs/`, `RTC-Modules/`)

## Key Commands

```bash
# Generate stickers for specific family
python scripts/build_labels.py --family ENV3xx

# Generate custom migration sheets (padded to multiples of 4)
python scripts/build_labels.py --output-prefix migration --pad-sheets \
  --ids SW201,RF101,ENV201,ENV202,ENV203,ENV204,ENV205,OT101,OT102,OT201,OT202,AC501,AC502,AC503,ENV301,ENV302,ENV303,ENV304

# Preview site
make serve

# Build everything (registry + stickers)
make registry_stickers

# Commit with pre-commit hook (auto-runs make registry_stickers)
git add -A && git commit -m "message"
```

## Lessons Learned

### Issues Fixed in ENV3xx
1. **Libraries list rendering:** Needed blank line before bullets
2. **Circuit explanation rendering:** Needed blank line before bullets
3. **Sticker verbosity:** Simplified line 1 to generic type only
4. **AliExpress links:** Multiple old links broken, updated to current products

### Common Mistakes to Avoid
- ❌ Forgetting blank lines before lists
- ❌ Repeating component details in family index
- ❌ Using "Other" folder (use root-level folders instead)
- ❌ Wrong sticker path depth for nested folders
- ❌ Using search URLs instead of product links
- ❌ Adding technical tags that DIYers won't search for
- ❌ Making sticker text too verbose

## Next Steps

### Remaining Families to Migrate

Check `MIGRATION_PLAN.md` for full list. Some high-priority families:

**Phase 3 - Medium Priority:**
- **PS1xx:** LDO Regulators (PS001 AMS1117, PS002 HT7333, PS003 XC6206)
- **PS2xx:** DC-DC Converters (PS201 XL6009, PS202 LM2596, PS203 MP1584)
- **MC1xx:** ESP32 Boards (MC001 ESP32-DevKitC, etc.)
- **AC3xx:** DC Motors & Drivers (AC301 L298N, AC302 DRV8833)

**Phase 4 - Nice to Have:**
- **TS1xx:** Temperature Sensors (TS001 DS18B20, TS002 DHT22, etc.)
- **IO1xx:** I/O Expanders (IO001 PCF8574, etc.)

### Workflow for Next Family

1. **Check next available IDs:**
   ```bash
   cat docs/components/stickers/id_registry_simple.yaml
   ```

2. **Read existing component files** (if migrating) to understand current state

3. **Create family structure:**
   - Family anchor (CCXX00): `index.md` with comparison table
   - Individual components (CCXX01, CCXX02, etc.)
   - Apply all formatting rules (blank lines, concise stickers, etc.)

4. **Generate stickers:**
   ```bash
   python scripts/build_labels.py --family CCXX
   ```

5. **Update migration sheets** (if user wants to print):
   ```bash
   python scripts/build_labels.py --output-prefix migration --pad-sheets --ids <full-list>
   ```

6. **Commit with descriptive message**

### Target for Full Sheets
- Current: 18 components = 4 sheets (with 2 reserved placeholders on sheet 4)
- Need 2 more components to fill sheet 4 completely
- Or continue to next family for another full sheet

## Important Files

- **MIGRATION_PLAN.md:** Full migration roadmap
- **CLAUDE.md:** Project architecture and conventions
- **SESSION_HANDOFF.md:** Original session context (older)
- **SESSION_HANDOFF_2025-11-25.md:** This file (current session)
- **scripts/build_labels.py:** Sticker generation script
- **docs/components/stickers/id_registry_simple.yaml:** Quick ID reference

## Git Status

```
Branch: main
Status: 18 commits ahead of origin/main
Last commit: "Fix ENV3xx documentation issues"
Pre-commit hook: Active (auto-runs make registry_stickers)
```

## Questions to Ask User

When starting the next session:

1. "Should we continue with the next family migration? If so, which family would you like to tackle next?"
2. "Do you want to fill the current migration sheet (need 2 more components) or start a fresh sheet with a new family?"
3. "Any feedback on the ENV3xx family we just completed?"

## Context Prompt for New Session

Copy-paste this to start a new session:

---

I'm continuing the electronics catalog migration project. We're organizing individual components into family-based structure with QR stickers.

**Current Status:**
- ✅ Completed 7 families: SW201, RF101, ENV2xx (5), OT1xx (2), OT2xx (2), AC5xx (3), ENV3xx (4)
- 📦 Total: 18 components across 4 migration sheets (padded for thermal printer)
- 🎯 Latest: ENV3xx Light Sensors family just completed with all fixes applied

**Important Context:**
- Read `SESSION_HANDOFF_2025-11-25.md` for full details on patterns, conventions, and lessons learned
- Key rules: blank lines before lists, concise stickers, no "Other" folder, proper sticker paths
- Branch is 18 commits ahead of origin (unpushed)

**Ready to continue!** What family should we migrate next?

---
