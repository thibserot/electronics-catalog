# Electronics Catalog Migration Plan

## Overview
Incremental migration to new family-based organization. Work one family at a time for review.

**Status Legend:**
- ⬜ Not Started
- 🔄 In Progress
- ✅ Completed
- ⏸️ Paused/Blocked

---

## Phase 1: Simple Single-Component Migrations (Warmup)

Good for testing the process with minimal risk.

### 1.1 IO201: Touch Sensor ⬜
**Complexity**: ⭐ Easy
**What**: Rename IO001 → IO201 (no family structure)
**Steps**:
1. Move `docs/components/IO001.md` to `docs/components/IO201.md`
2. Update front-matter: `id: IO201`
3. Regenerate: `make registry_stickers`
4. Review sticker output

**Files affected**: 1 file

---

### 1.2 RF101: RFID Reader ⬜
**Complexity**: ⭐ Easy
**What**: Rename RF001 → RF101 (no family, RC522=MFRC522 same module)
**Steps**:
1. Move `docs/components/RF001.md` to `docs/components/RF101.md`
2. Update front-matter: `id: RF101`
3. Update content to mention RC522 is same module
4. Regenerate: `make registry_stickers`
5. Review sticker output

**Files affected**: 1 file

---

## Phase 2: Small New Families (2-3 components)

Test creating family structures with comparison tables.

### 2.1 ENV2xx: Air Quality & Gas Sensors ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components with family structure
**Steps**:
1. Create folder: `docs/components/Environmental/Air-Quality/`
2. Create `index.md` (ENV200) with comparison table
3. Create `ENV201.md` (MH-Z19C CO2 Sensor)
4. Create `ENV202.md` (MQ-2 Gas Sensor)
5. Regenerate: `make registry_stickers`
6. Review all 3 stickers + comparison table

**Files affected**: 3 new files (1 index + 2 components)

---

### 2.2 OT1xx: Logic ICs ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components with family structure
**Steps**:
1. Create folder: `docs/components/Other/Logic-ICs/`
2. Create `index.md` (OT100) with comparison table
3. Create `OT101.md` (74HC595 Shift Register - 2pcs)
4. Create `OT102.md` (LMC555CN Timer IC - 20pcs)
5. Regenerate: `make registry_stickers`
6. Review all 3 stickers + comparison table

**Files affected**: 3 new files

---

### 2.3 OT2xx: RTC Modules ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components with family structure
**Steps**:
1. Create folder: `docs/components/Other/RTC-Modules/`
2. Create `index.md` (OT200) with comparison table
3. Create `OT201.md` (DS1302 RTC - SPI)
4. Create `OT202.md` (DS1307 RTC - I2C)
5. Regenerate: `make registry_stickers`
6. Review all 3 stickers + comparison table

**Files affected**: 3 new files

---

## Phase 3: Medium Families (4-5 components with renames)

Mix of existing and new components.

### 3.1 ENV1xx: Temperature & Humidity Sensors ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 5 components (2 renames + 3 new) with family structure
**Steps**:
1. Create folder: `docs/components/Environmental/Temperature-Humidity/`
2. Create `index.md` (ENV100) with comparison table
3. Move & rename: `TS001.md` → `ENV101.md` (update id, category)
4. Move & rename: `ENV001.md` → `ENV102.md` (update id)
5. Create `ENV103.md` (DHT11)
6. Create `ENV104.md` (GY-SHT45 - 2pcs)
7. Create `ENV105.md` (Thermistor)
8. Regenerate: `make registry_stickers`
9. Review all 6 stickers + comparison table

**Files affected**: 6 files (1 index + 2 renames + 3 new)

---

### 3.2 ENV3xx: Light Sensors ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 4 components (1 rename + 3 new) with family structure
**Steps**:
1. Create folder: `docs/components/Environmental/Light/`
2. Create `index.md` (ENV300) with comparison table
3. Move & rename: `ENV002.md` → `ENV301.md` (update id)
4. Create `ENV302.md` (TSL2591 - 2pcs)
5. Create `ENV303.md` (GY-2561 TSL2561 - 2pcs)
6. Create `ENV304.md` (Photoresistor - 2pcs)
7. Regenerate: `make registry_stickers`
8. Review all 5 stickers + comparison table

**Files affected**: 5 files (1 index + 1 rename + 3 new)

---

### 3.3 AC5xx: Servos ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 3 components (1 rename + 2 new) with family structure
**Steps**:
1. Create folder: `docs/components/Actuators/Servos/`
2. Create `index.md` (AC500) with comparison table
3. Move & rename: `AC009.md` → `AC501.md` (update id)
4. Create `AC502.md` (SG90 180°)
5. Create `AC503.md` (SG90 360°)
6. Regenerate: `make registry_stickers`
7. Review all 4 stickers + comparison table

**Files affected**: 4 files (1 index + 1 rename + 2 new)

---

### 3.4 AC6xx: Cooling Fans (Same family, 2 drawers) ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 2 components (1 rename + 1 new) with family structure
**Steps**:
1. Create folder: `docs/components/Actuators/Cooling-Fans/`
2. Create `index.md` (AC600) with comparison table (12V vs 5V)
3. Move & rename: `AC010.md` → `AC601.md` (update id)
4. Create `AC602.md` (25mm Fan 5V - 5pcs)
5. Regenerate: `make registry_stickers`
6. Review all 3 stickers + comparison table

**Files affected**: 3 files (1 index + 1 rename + 1 new)

---

## Phase 4: Large Families (6+ components)

### 4.1 AC8xx: Audio Output (Speakers/Buzzers) ⬜
**Complexity**: ⭐⭐⭐⭐ Complex
**What**: 5 components (4 renames + 1 new) with family structure
**Steps**:
1. Create folder: `docs/components/Actuators/Audio-Output/`
2. Create `index.md` (AC800) with comparison table
3. Move & rename: `AC002.md` → `AC801.md`
4. Move & rename: `AC003.md` → `AC802.md`
5. Move & rename: `AC004.md` → `AC803.md`
6. Move & rename: `OT001.md` → `AC804.md`
7. Create `AC805.md` (Active Buzzer - 2-3pcs)
8. Regenerate: `make registry_stickers`
9. Review all 6 stickers + comparison table

**Files affected**: 6 files (1 index + 4 renames + 1 new)

---

### 4.2 IO4xx: Motion & Orientation Sensors ⬜
**Complexity**: ⭐⭐⭐⭐ Complex
**What**: 6 new components with family structure
**Steps**:
1. Create folder: `docs/components/Input-Output/Motion-Orientation/`
2. Create `index.md` (IO400) with comparison table
3. Create `IO401.md` (MPU6500 - 5pcs)
4. Create `IO402.md` (GY-521 MPU6050)
5. Create `IO403.md` (Vibration Sensor)
6. Create `IO404.md` (Tilt Sensor Module)
7. Create `IO405.md` (Tilt Ball Switch)
8. Create `IO406.md` (HC-SR501 PIR - 2pcs)
9. Regenerate: `make registry_stickers`
10. Review all 7 stickers + comparison table

**Files affected**: 7 files (1 index + 6 new)

---

### 4.3 IO7xx: Displays ⬜
**Complexity**: ⭐⭐⭐⭐ Complex
**What**: 4 new components with family structure
**Steps**:
1. Create folder: `docs/components/Input-Output/Displays/`
2. Create `index.md` (IO700) with comparison table
3. Create `IO701.md` (LCD1602 Module)
4. Create `IO702.md` (MAX7219 LED Matrix)
5. Create `IO703.md` (1-Digit 7-Segment)
6. Create `IO704.md` (4-Digit 7-Segment)
7. Regenerate: `make registry_stickers`
8. Review all 5 stickers + comparison table

**Files affected**: 5 files (1 index + 4 new)

---

## Phase 5: Expanding Existing Families

### 5.1 AC2xx: Transistors (Add to existing) ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: Add 1 new component to existing family (AC211)
**Steps**:
1. Update `docs/components/Bipolar Junction Transistor/index.md` comparison table
2. Create `AC211.md` (4N35 Optocoupler)
3. Update AC203 quantity notes (add 10x from kits)
4. Update AC207 quantity notes (add 5x from kits)
5. Regenerate: `make registry_stickers`
6. Review AC211 sticker + updated comparison table

**Files affected**: 2 files (1 update + 1 new)

---

### 5.2 PS2xx: Battery Charging (Add to existing) ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: Add 3 new components to existing family
**Steps**:
1. Update `docs/components/Battery Charging/index.md` comparison table
2. Create `PS203.md` (LiPo 250mAh - 2pcs)
3. Create `PS204.md` (LiPo 350mAh - 2pcs)
4. Create `PS205.md` (RC Battery Charger)
5. Regenerate: `make registry_stickers`
6. Review 3 new stickers + updated comparison table

**Files affected**: 4 files (1 update + 3 new)

---

## Phase 6: Remaining Families

### 6.1 ENV4xx: Moisture & Water Sensors ⬜
**Complexity**: ⭐⭐ Medium
**What**: 3 new components (bulky box)
**Files affected**: 4 files

---

### 6.2 IO3xx: Rotary Encoders & Joysticks ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 3 components (1 rename + 2 new)
**Files affected**: 4 files

---

### 6.3 IO5xx: Distance & Proximity ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components
**Files affected**: 3 files

---

### 6.4 IO6xx: Audio Input (Microphones) ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components
**Files affected**: 3 files

---

### 6.5 AC1xx: Motor Drivers ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components
**Files affected**: 3 files

---

### 6.6 AC4xx: Small Motors ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components
**Files affected**: 3 files

---

### 6.7 AC9xx: High-Power LEDs & Lasers ⬜
**Complexity**: ⭐⭐ Medium
**What**: 3 new components
**Files affected**: 4 files

---

### 6.8 RF2xx: Wireless/Ethernet ⬜
**Complexity**: ⭐⭐⭐ Medium
**What**: 2 components (1 rename + 1 new)
**Files affected**: 3 files

---

### 6.9 RF3xx: Infrared ⬜
**Complexity**: ⭐⭐ Medium
**What**: 2 new components
**Files affected**: 3 files

---

## Phase 7: Single Components (No families)

### 7.1 Single Component Migrations ⬜
**Complexity**: ⭐ Easy
**What**: Create remaining single components at root
**Components**:
- AC301 (IRLZ44N MOSFET)
- AC011 (Solenoid Valve)
- AC012 (Water Pressure Sensor)
- AC1201 (F5 LEDs - no sticker)
- PA004 (RXEF030 Fuses)
- SW008 (Key Lock Switch - rename from OT002)
- SW009 (Membrane Switch)

**Files affected**: 7 files

---

## Phase 8: Final Cleanup & Verification

### 8.1 Update existing families with comparison tables ⬜
**What**: Add/improve comparison tables for existing families
**Families**:
- IO100 (Magnetic Sensors)
- PS000 (DC-DC Converters)
- PS300 (LDO)
- MC100 (ESP32)

---

### 8.2 Full regeneration and testing ⬜
**Steps**:
1. Run `make registry_stickers`
2. Verify all ~140-145 stickers generated
3. Check registry YAML files
4. Test site build: `make serve`
5. Review navigation and links

---

### 8.3 Physical organization ⬜
**Steps**:
1. Print all new stickers
2. Label drawers with family names
3. Move components to new drawers
4. Take photos for documentation

---

### 8.4 Git commit and deploy ⬜
**Steps**:
1. Review all changes: `git status`, `git diff`
2. Commit: `git commit -m "Reorganize catalog into family-based drawer system"`
3. Deploy: `make publish`

---

## Progress Summary

**Total Phases**: 8
**Total Tasks**: ~35
**Completed**: 0
**In Progress**: 0
**Remaining**: 35

**Estimated Total Files**: ~100-120 new/modified files

---

## Recommended Starting Point

**Start with Phase 1.1 (IO201)** - simplest possible migration to test the workflow.

After completing Phase 1.1, we can:
1. Review the generated sticker
2. Verify the process works
3. Adjust if needed
4. Move to Phase 1.2 or Phase 2.1

---

## Notes

- Each phase can be done in a separate session
- Review content before moving to next phase
- Can pause and adjust plan as needed
- Token limit: Start fresh session when needed
