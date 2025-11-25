# Session Handoff: Electronics Catalog Migration

## Current Status

### Completed
✅ **Reorganization plan finalized** (`REORGANIZATION_PLAN.md`)
- 18 families with 2+ components (with comparison tables)
- ~20 single components at root (no family structure)
- Total: ~140-145 component types
- ESP32 structure: MC101-104 individual drawers, MC105-107 in shared "Other" drawer

✅ **Migration plan created** (`MIGRATION_PLAN.md`)
- 8 phases organized by complexity
- 35+ tasks broken down step-by-step
- Progress tracking with checkboxes

✅ **Sticker generator updated** (`scripts/build_labels.py`)
- Added `--family` flag for family-specific generation
- Added `--ids` flag for specific component IDs
- Original behavior preserved (no flags = generate all)

### Decisions Made

**Migration Approach: OPTION A (Clean Migration)**
- Standardize front-matter structure as we go
- Fix section headings and formatting
- Update/clean existing content
- Add missing sections (don't need to fill everything)
- Each family is "done" when we finish it

**Workflow Per Family:**
1. Create/move files with harmonized content
2. Run: `python scripts/build_labels.py --family ENV1xx`
3. Review: Generated stickers for that family only
4. Print: Those specific stickers
5. Physically organize: Label drawer and add components
6. Commit: Git commit for that family
7. Move to next family

---

## Updated Sticker Generator Usage

```bash
# Generate stickers for one family
python scripts/build_labels.py --family ENV1xx
# Output: Generates ENV100, ENV101, ENV102, ..., ENV199 (if they exist)

# Generate stickers for specific IDs
python scripts/build_labels.py --ids ENV101,ENV102,ENV103
# Output: Generates only those 3 stickers

# Generate all stickers (original behavior)
python scripts/build_labels.py
# Output: Generates all ~140-145 stickers

# After generation, check output
ls docs/components/stickers/ENV*.png
```

**Family format examples:**
- `ENV1xx` matches ENV100-ENV199 (Temperature & Humidity)
- `ENV2xx` matches ENV200-ENV299 (Air Quality)
- `AC2xx` matches AC200-AC299 (Transistors)
- `IO4xx` matches IO400-IO499 (Motion sensors)

---

## Content Harmonization Guidelines

### Front-Matter Structure (Required)

Every component page must have:

```yaml
---
id: ENV101                      # Component ID (required)
name: DS18B20                   # Display name (required)
category: ENV                   # Category code (required)
tags: [temperature, sensor, waterproof, 1-wire, esp32-safe]  # Searchable tags (required)
sticker_line1: "Temp sensor • ±0.5°C • Waterproof"  # What it is + key specs (required)
sticker_line2: "Outdoor temp sensing"                # Primary use case (required)
# Optional fields:
title: DS18B20                  # Override page title (defaults to name)
qr_url: https://...             # Override QR URL
no_label: false                 # Set true to skip sticker generation
---
```

**Sticker Field Guidelines:**

`sticker_line1` - **What it is + key differentiator**
- Start with what it IS in plain language
- Add 1-2 key specs that differentiate it from similar components
- Example: "Temp sensor • ±0.5°C • Waterproof" (DS18B20)
- Example: "Capacitive touch switch" (TTP223)
- Example: "CO2 sensor • NDIR • 0-5000ppm" (MH-Z19C)
- Keep under ~35 characters

`sticker_line2` - **Best use case or key compatibility**
- When would you grab THIS one over alternatives?
- OR what platform is it compatible with?
- Example: "Outdoor temp sensing" (DS18B20)
- Example: "Toggle/Momentary • ESP32-safe" (TTP223)
- Example: "High-precision HVAC control" (SHT45)
- Keep under ~35 characters

**Tag Strategy (DIYer-focused):**

Tags should help answer: "I want to measure/control X with Y platform - what do I have?"

1. **Function tags** - What it does in plain language (FIRST)
   - Examples: `temperature`, `humidity`, `pressure`, `motion`, `distance`
   - Examples: `button`, `switch`, `motor-driver`, `relay`, `display`, `wireless`
   - Examples: `power-supply`, `voltage-regulator`

2. **Component type tags** - What kind of thing it is
   - Examples: `sensor`, `actuator`, `module`, `breakout`, `ic`, `discrete`

3. **Characteristic tags** - Key properties that help selection
   - Examples: `capacitive`, `mechanical`, `optical`
   - Examples: `waterproof`, `outdoor`, `high-precision`, `low-power`
   - Examples: `toggle`, `momentary`, `latching`

4. **Compatibility tags** - Platform support (what can I use this with?)
   - `esp32-compatible` (works with ESP32 - may need 5V pin for power, but GPIO-safe)
   - `arduino-compatible` (works with Arduino 5V system)
   - Most components get BOTH tags if they work with both platforms

5. **Interface tags** - Only if relevant for discovery
   - Examples: `i2c`, `spi`, `uart`, `1-wire`, `analog`, `pwm`
   - Skip generic ones: `digital`, `gpio`, `input`, `output`

**Don't use:** Generic/obvious tags (`digital`, `input`, `output`, `3v3`, `5v`)

**Keep tags lowercase, use hyphens for multi-word** (`touch-sensor`, `high-precision`)

**Tag order:** Function → Type → Characteristics → Compatibility → Interface

### Page Content Structure (Standardized)

**Tone Guidelines:**
- ✅ Be concise and factual
- ✅ State specs directly from datasheet
- ✅ Call out ambiguity explicitly if details are missing
- ✅ Link to datasheet/component page for full details
- ❌ Don't say "most...", "typically...", "usually..." - be specific or say you don't know
- ❌ Don't improvise or guess specs
- ❌ Don't write dissertations - save user time

```markdown
---
[front-matter here]
---

# Component Name

One sentence: what it is and what it measures/does.

## Key Specifications

- **Operating Voltage**: 3.0V - 5.5V
- **Temperature Range**: -55°C to +125°C
- **Accuracy**: ±0.5°C (-10°C to +85°C)
- **Interface**: 1-Wire (single data line)
- **Package**: TO-92 / Waterproof probe available

## Pinout

| Pin | Name | Description |
|-----|------|-------------|
| 1   | GND  | Ground |
| 2   | DQ   | Data line (1-Wire) |
| 3   | VCC  | Power (3.0-5.5V) |

**Notes:**
- Requires 4.7kΩ pull-up resistor on DQ line
- Can be powered in parasite mode (VCC connected to GND)

## Wiring

### Basic Connection (ESP32)

```
DS18B20    ESP32
--------   ------
VCC    --> 3.3V
GND    --> GND
DQ     --> GPIO 4 (with 4.7kΩ pull-up to 3.3V)
```

**Multiple sensors:** Can connect multiple DS18B20 on same bus (each has unique 64-bit ROM code)

## Usage Notes

### When to Use

**Use this component when:**
- Outdoor/waterproof temperature measurement needed
- Multiple sensors on single bus (unique ROM addressing)

**Don't use when:**
- Need <0.1°C accuracy (use ENV104 SHT45 instead)
- Need fast updates (<750ms conversion time)

### Common Issues
- Requires 4.7kΩ pull-up resistor on DQ line (internal pull-ups insufficient)
- Cable length >30m requires lower pull-up resistance (calculate per datasheet)
- Waterproof probe pinout differs from TO-92 package - verify before wiring

## Code Examples

### Arduino/ESP32

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  Serial.printf("Temperature: %.2f°C\n", tempC);
  delay(1000);
}
```

## Links

- [Datasheet (Maxim DS18B20)](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf)
- [Purchase: Waterproof probe](https://www.aliexpress.com/item/...)
- [Library: DallasTemperature](https://github.com/milesburton/Arduino-Temperature-Control-Library)
- [Arduino example](https://randomnerdtutorials.com/esp32-ds18b20-temperature-arduino-ide/)

**Note**: Related/alternative components are listed in the [ENV1xx family index](../Environmental/Temperature-Humidity/).
```

### Section Guidelines

**Required Sections:**
- Title + brief description (1 sentence)
- Key Specifications (bullet list from datasheet)
- Pinout (if applicable)
- Links (datasheet + purchase link minimum)

**Optional Sections (add only if you have specific info):**
- Wiring diagram (if non-standard)
- When to Use (specific use cases only)
- Common Issues (known problems with solutions)
- Code example (if simple/common pattern)

**Do NOT include:**
- "Related Components" section (put in family index instead)
- Vague generalizations ("most people...", "typically...")
- Information you're guessing at

**Keep Names Concise:**
- Component names must fit on sticker (max ~20-25 chars)
- Abbreviate when needed: "Temp/Humidity Sensor" not "Temperature and Humidity Sensor"
- Use standard abbreviations: "I2C", "SPI", "UART", "ADC", "DAC"

**Markdown Formatting Quirks (MkDocs Material):**
- **Nested lists require 4 spaces**, not 2 spaces
  - ❌ Wrong: `- Item\n  - Subitem` (2 spaces)
  - ✅ Correct: `- Item\n    - Subitem` (4 spaces)
- **Bold text before list needs blank line**
  - ❌ Wrong: `**Use when:**\n- Item 1` (list doesn't render)
  - ✅ Correct: `**Use when:**\n\n- Item 1` (blank line separates)
- **Numbered lists need blank line after header**
  - ❌ Wrong: `### Sensitivity\nMQ-2 is most sensitive to:\n1. Propane` (doesn't render)
  - ✅ Correct: `### Sensitivity\n\nMQ-2 is most sensitive to:\n\n1. Propane` (blank lines)
- **Code blocks** use triple backticks with optional language: ` ```cpp ` or ` ```python `
- **Tables** require proper alignment with pipes and dashes (see Pinout examples)
- **Sources sections need blank line before list**
  - ❌ Wrong: `**Sources:**\n- [Link](url)` (doesn't render)
  - ✅ Correct: `**Sources:**\n\n- [Link](url)` (blank line)

**Nested Component Paths:**
- Components in nested folders must use **relative paths** for sticker images
- **Wrong:** `![QR sticker](stickers/ENV201.png)` (looks in current folder)
- **Correct:** `![QR sticker](../../stickers/ENV201.png)` (goes up to docs/components/)
- Path calculation: `docs/components/Environmental/Air-Quality/ENV201.md` → `../../stickers/ENV201.png`

**Platform Compatibility Tags:**

Tag components based on which platforms they work with:

- `esp32-compatible` - Works with ESP32 (may need 5V pin for power, but GPIO-safe)
- `arduino-compatible` - Works with Arduino (5V system)

**Tagging rules:**

Tag `esp32-compatible` if:
- Runs on 3.3V (use ESP32 3.3V pin), OR
- Runs on 5V with 3.3V-safe GPIO (use ESP32 5V pin for power), OR
- Requires adapters (voltage divider, level shifter) that are documented

Tag `arduino-compatible` if:
- Works with 5V power and logic

**Most components get BOTH tags** (wide compatibility)

**Document special requirements in component page:**
- "Requires 5V power (connect to ESP32 5V pin)"
- "Use voltage divider for ESP32 ADC (5V analog output)"
- "GPIO-safe (3.3V logic levels)"

**Search behavior:**
- User searches `esp32-compatible` → Finds everything that works with ESP32
- User searches `arduino-compatible` → Finds everything that works with Arduino
- Complexity lives in documentation, not tags

### Family Index Pages

Each family `index.md` should have:

**IMPORTANT: Avoid duplication!**
- Don't repeat wiring details (those belong in component pages)
- Don't repeat technical notes (those belong in component pages)
- Focus on comparison and selection guidance only

**Make comparison table links clickable:**
- Component names in table should link to component pages
- Example: `| [ENV201](ENV201.md) (MH-Z19C) |` (clickable link)

```markdown
---
id: ENV100
name: Temperature & Humidity Sensors
category: ENV
tags: [family, sensor, temperature, humidity]
no_label: false  # Generate sticker for family anchor
---

# Temperature & Humidity Sensors

Sensors for measuring ambient temperature and/or relative humidity in various environments.

## Comparison

| Component | Type | Temp Range | RH Range | Accuracy (T/RH) | Interface | Best For |
|-----------|------|------------|----------|-----------------|-----------|----------|
| ENV101 (DS18B20) | Temp only | -55 to 125°C | - | ±0.5°C / - | 1-Wire | Waterproof, multiple sensors |
| ENV102 (BME280) | Temp+RH+Press | -40 to 85°C | 0-100% | ±1°C / ±3% | I2C/SPI | Weather stations |
| ENV103 (DHT11) | Temp+RH | 0 to 50°C | 20-90% | ±2°C / ±5% | Digital | Quick prototypes |
| ENV104 (SHT45) | Temp+RH | -40 to 125°C | 0-100% | ±0.1°C / ±1% | I2C | High precision |
| ENV105 (Thermistor) | Temp only | Varies | - | ~1°C / - | Analog | Simple/cheap |

## Selection Guide

**Choose ENV101 (DS18B20) when:**
- Need waterproof sensor
- Want multiple sensors on same bus (1-Wire addressing)
- Accuracy: ±0.5°C sufficient

**Choose ENV102 (BME280) when:**
- Need temperature + humidity + pressure (3-in-1)
- Low power consumption required (I2C sleep modes)
- Accuracy: ±1°C / ±3% RH sufficient

**Choose ENV103 (DHT11) when:**
- Learning/prototyping only
- Accuracy: ±2°C / ±5% RH acceptable
- Slowest option (1 Hz update rate)

**Choose ENV104 (SHT45) when:**
- High precision required (±0.1°C / ±1% RH)
- HVAC control or data logging
- Budget allows (most expensive)

**Choose ENV105 (Thermistor) when:**
- Need analog temperature input
- Calibration acceptable
- Lowest cost option

## Common Wiring

**3-pin sensors** (ENV101, ENV103):
- VCC, GND, Data line
- Check voltage: 3.3V or 5V (see individual component pages)

**I2C sensors** (ENV102, ENV104):
- VCC, GND, SDA, SCL
- Require 4.7kΩ pull-ups on SDA/SCL (check if onboard)

**Analog sensors** (ENV105):
- VCC, GND, Analog output
- Connect to ADC pin (ESP32: GPIO 32-39)

## Projects Using This Family

- Weather station (ENV102 for outdoor, ENV104 for indoor precision)
- Aquarium/terrarium monitoring (ENV101 waterproof probes)
- Smart home HVAC control (ENV104 for accuracy)
- Greenhouse automation (ENV102 or ENV104)

{{ children() }}
```

---

## Recommended Starting Point

**Phase 1.1: IO201 (Touch Sensor)**
- Simplest task: Single component rename
- Tests the workflow end-to-end
- Low risk, quick validation

**After IO201, move to:**
- Phase 2.1: ENV2xx (Air Quality) - Small new family
- Phase 3.1: ENV1xx (Temp/Humidity) - Medium family with renames

---

## Git Commit Strategy

Commit after each family is complete:

```bash
# After completing ENV2xx family
git add docs/components/Environmental/Air-Quality/
git add docs/components/stickers/ENV2*.png
git commit -m "Add ENV2xx: Air Quality & Gas Sensors family

- ENV200: Family anchor with comparison table
- ENV201: MH-Z19C CO2 Sensor (NDIR infrared)
- ENV202: MQ-2 Gas Sensor (smoke/LPG/CO)

Generated stickers for ENV200-202"

# After completing a rename
git add docs/components/IO201.md
git rm docs/components/IO001.md  # if renaming
git add docs/components/stickers/IO201.png
git commit -m "Rename IO001 → IO201: TTP223 Touch Sensor

Standardized front-matter and content structure"
```

---

## Known Issues / Considerations

### ESP32 Structure
- MC101-MC104: Each in own drawer (4 drawers)
- MC105-MC107: Share "ESP32 - Other" drawer (1 drawer)
- Keep nested folder structure: `esp32/Other/MC105.md`, etc.
- Total: 5 physical drawers for ESP32 family

### Registry Generation
- After each family, run `python scripts/generate_id_registry.py` to update registry
- Or run full `make registry_stickers` to regenerate everything

### Sticker Printing
- Print family stickers as you go (don't wait until end)
- Test print ENV2xx first to verify label size/readability
- Adjust `PRESET` in `build_labels.py` if needed ("compact" vs "large")

---

## Next Session Prompt

Use this prompt to start the next session:

```
I'm continuing the electronics catalog migration. We've completed:

1. ✅ Reorganization plan (REORGANIZATION_PLAN.md)
2. ✅ Migration plan with 8 phases (MIGRATION_PLAN.md)
3. ✅ Updated build_labels.py to support --family and --ids flags
4. ✅ Decided on Option A (clean migration - harmonize content as we go)

SESSION_HANDOFF.md contains:
- Content harmonization guidelines (front-matter structure, page sections, tags)
- Family index page template with comparison tables
- Workflow per family
- Git commit strategy

CURRENT TASK: Start migrations with Phase 1.1 (IO201 - Touch Sensor)

This is a simple rename (IO001 → IO201) with content harmonization:
1. Move docs/components/IO001.md → docs/components/IO201.md
2. Update front-matter: id, standardize tags
3. Clean up content sections (Specs, Pinout, Wiring, Links)
4. Keep name concise for sticker
5. Run: python scripts/build_labels.py --ids IO201
6. Review generated sticker
7. Git commit

Please help me complete Phase 1.1, showing me:
- The updated front-matter
- Content structure outline (what sections to include)
- Generated sticker preview (after running build_labels.py)

After Phase 1.1, we'll review and decide on next phase.
```

---

## Quick Reference Commands

```bash
# Generate stickers for one family
python scripts/build_labels.py --family ENV1xx

# Generate stickers for specific IDs
python scripts/build_labels.py --ids ENV101,ENV102

# Generate all stickers
python scripts/build_labels.py

# Update registry
python scripts/generate_id_registry.py

# Full regeneration (registry + stickers + registry page)
make registry_stickers

# Preview site locally
make serve

# Deploy to GitHub Pages
make publish
```

---

## Files Created/Modified This Session

**New Files:**
- `REORGANIZATION_PLAN.md` - Complete component mapping and reorganization plan
- `MIGRATION_PLAN.md` - 8-phase migration plan with task breakdown
- `SESSION_HANDOFF.md` - This file (handoff for next session)

**Modified Files:**
- `scripts/build_labels.py` - Added --family and --ids arguments for incremental generation

**Status:**
- Ready to start Phase 1.1 (IO201) in next session
- All planning complete
- Tools ready for incremental migration

---

**Recommended: Start fresh session now to reset token count and begin Phase 1.1!**
