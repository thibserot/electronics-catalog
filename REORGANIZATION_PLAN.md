# Electronics Catalog Reorganization Plan

## Overview

This plan reorganizes the entire catalog to align **physical drawer organization** with **logical family structure**.

**Key principles**:
- **Families only when 2+ component types share logical grouping** (even if different drawers)
- **Single component type = No family structure** (e.g., IO201 at root, no IO2xx family)
- **One sticker per component TYPE** (quantity noted in page content, not front-matter)
- **Family index pages** provide comparison tables to help choose the right component
- **Stickers on drawer fronts** for single-component drawers (no ziplock bags inside)

## Sticker & ID Philosophy

- **One ID per component type**: ENV401 represents all 6 soil moisture sensors
- **No quantity in front-matter**: Track quantities in page content if needed
- **Component names must be concise**: Fit on sticker labels

---

## Complete Component Mapping

### ENV - Environmental Sensors

#### ENV1xx: Temperature & Humidity Sensors (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Environmental/Temperature-Humidity/`
**Family**: YES (5 types - comparison needed)
**Status**: ⏸️ PENDING - TS001 still at root, ENV001 still at root

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| ENV100 | - | Temp & Humidity Sensors | NEW | Family anchor (index.md) with comparison table |
| ENV101 | TS001 | DS18B20 | RENAME | 1-Wire digital temp sensor |
| ENV102 | ENV001 | BME280/BMP280 | RENAME | I2C temp/humidity/pressure |
| ENV103 | - | DHT11 | NEW | From starter kit |
| ENV104 | - | GY-SHT45 | NEW | High-precision I2C (2pcs) |
| ENV105 | - | Thermistor | NEW | Analog temp sensor |

---

#### ENV2xx: Air Quality & Gas Sensors (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Environmental/Air-Quality/`
**Family**: YES (5 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| ENV200 | - | Air Quality & Gas Sensors | NEW | Family anchor (index.md) with comparison table |
| ENV201 | - | MH-Z19C CO2 Sensor | NEW | NDIR infrared CO2 sensor |
| ENV202 | - | MQ-2 Gas Sensor | NEW | Smoke/LPG/CO gas sensor |

---

#### ENV3xx: Light Sensors (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Environmental/Light/`
**Family**: YES (6 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated (includes ENV305 restored 2025-11-27)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| ENV300 | - | Light Sensors | NEW | Family anchor (index.md) with comparison table |
| ENV301 | ENV002 | LDR 5528 | RENAME | Photoresistor (analog) |
| ENV302 | - | TSL2591 | NEW | High dynamic range I2C (2pcs) |
| ENV303 | - | GY-2561 TSL2561 | NEW | Luminosity I2C (2pcs) |
| ENV304 | - | Photoresistor | NEW | Generic LDR from fun kit (2pcs) |

---

#### ENV4xx: Moisture & Water Sensors (Bulky Box) - NOT YET CREATED
**Physical**: Bulky box
**Folder**: `docs/components/Environmental/Moisture-Water/`
**Family**: YES (3 types)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| ENV400 | - | Moisture & Water Sensors | NEW | Family anchor (index.md) with comparison table |
| ENV401 | - | Soil Moisture Sensor | NEW | Capacitive/resistive (6pcs: 5 from new + 1 from old pack) |
| ENV402 | - | Water Level Sensor | NEW | From starter kit |
| ENV403 | - | Rain Sensor | NEW | From old pack |

---

### IO - Input/Output

#### IO1xx: Magnetic Sensors (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/Magnetic Sensors/` (keep existing)
**Family**: YES (3 components + anchor - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO100 | IO100 | Magnetic Sensors | KEEP | Family anchor with comparison table |
| IO101 | IO101 | GPS-14A | KEEP | Hall effect switch |
| IO102 | IO102 | A3144E | KEEP | Hall effect switch |

---

#### SW201: Touch Sensor (1 Drawer) - ✅ COMPLETED (moved from IO to SW)
**Physical**: Small drawer (existing touch drawer)
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)
**Status**: ✅ COMPLETED - Created as SW201 instead of IO201

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO201 | IO001 | TTP223 Touch Sensor | RENAME | Capacitive touch module |

---

#### IO3xx: Rotary Encoders & Joysticks (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer (existing rotary encoder drawer)
**Folder**: `docs/components/Input-Output/Rotary-Joystick/`
**Family**: YES (3 types)
**Status**: ⏸️ PENDING - IO003 still at root

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO300 | - | Rotary Encoders & Joysticks | NEW | Family anchor (index.md) with comparison table |
| IO301 | IO003 | KY-040 Rotary Encoder | RENAME | With push button |
| IO302 | - | Rotary Encoder Module | NEW | From starter kit (different from KY-040) |
| IO303 | - | Joystick Module | NEW | 2-axis analog joystick |

---

#### IO4xx: Motion & Orientation Sensors (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Input-Output/Motion-Orientation/`
**Family**: YES (6 types)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO400 | - | Motion & Orientation Sensors | NEW | Family anchor (index.md) with comparison table |
| IO401 | - | MPU6500 6-Axis | NEW | I2C gyro/accel (5pcs) |
| IO402 | - | GY-521 MPU6050 6-Axis | NEW | I2C gyro/accel from starter kit |
| IO403 | - | Vibration Sensor Module | NEW | From old pack |
| IO404 | - | Tilt Sensor Module | NEW | Mercury/ball tilt sensor |
| IO405 | - | Tilt Ball Switch | NEW | From starter kit |
| IO406 | - | HC-SR501 PIR Motion | NEW | Passive infrared (2pcs) |

---

#### IO5xx: Distance & Proximity Sensors (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Input-Output/Distance-Proximity/`
**Family**: YES (2 types)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO500 | - | Distance & Proximity Sensors | NEW | Family anchor (index.md) with comparison table |
| IO501 | - | HC-SR04 Ultrasonic | NEW | 2cm-400cm range (2pcs) |
| IO502 | - | FC-123 IR Tracking Sensor | NEW | Infrared obstacle detection |

---

#### IO6xx: Audio Input (Microphones) (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Input-Output/Audio-Input/`
**Family**: YES (2 types)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO600 | - | Audio Input (Microphones) | NEW | Family anchor (index.md) with comparison table |
| IO601 | - | INMP441 I2S Mic | NEW | Digital I2S MEMS (5pcs) |
| IO602 | - | Sound Sensor Module | NEW | Analog output (2pcs) |

---

#### IO7xx: Displays (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Input-Output/Displays/`
**Family**: YES (4 types)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| IO700 | - | Displays | NEW | Family anchor (index.md) with comparison table |
| IO701 | - | LCD1602 Module | NEW | 16x2 char I2C/parallel |
| IO702 | - | MAX7219 LED Matrix | NEW | 8x8 LED matrix SPI |
| IO703 | - | 1-Digit 7-Segment | NEW | Common cathode/anode |
| IO704 | - | 4-Digit 7-Segment | NEW | Common cathode/anode |

---

### AC - Actuators

#### AC0xx: Individual Actuators (Keep existing, not in families) - ✅ COMPLETED
**Physical**: Various individual drawers
**Folder**: `docs/components/` (root level, keep existing)
**Family**: NO (each is unique/high quantity)
**Status**: ✅ COMPLETED - All standalone components kept as is + AC011 created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC001 | AC001 | AOD4184 MOSFET | KEEP | Dedicated drawer (30+ pcs) |
| AC005 | AC005 | Electromagnetic Lock | KEEP | |
| AC006 | AC006 | WS2812B Addressable LED | KEEP | |
| AC007 | AC007 | Ultrasonic Nebulizer Driver | KEEP | |
| AC008 | AC008 | 1-Channel Relay Module | KEEP | |

---

#### AC1xx: Motor Drivers (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Motor-Drivers/`
**Family**: YES (3 components + anchor)
**Status**: ✅ COMPLETED - Created 2025-11-27

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC100 | - | Motor Drivers | NEW | Family anchor (index.md) with comparison table |
| AC101 | - | TB6612 Dual Motor Driver | NEW | 1A per channel module (2pcs) |
| AC102 | - | L293D Motor Driver IC | NEW | DIP-16 IC from starter kit |

---

#### AC2xx: Transistors (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing transistor drawer)
**Folder**: `docs/components/Bipolar Junction Transistor/` (keep existing folder)
**Family**: YES (11 BJT types + optocoupler - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC200 | AC200 | Transistors | KEEP | Family anchor with comparison table |
| AC201 | AC201 | BC337 (NPN) | KEEP | |
| AC202 | AC202 | BC327 (PNP) | KEEP | |
| AC203 | AC203 | 2N2222 (NPN) | KEEP | Add 10x from kits |
| AC204 | AC204 | 2N2907 (PNP) | KEEP | |
| AC205 | AC205 | 2N3904 (NPN) | KEEP | |
| AC206 | AC206 | 2N3906 (PNP) | KEEP | |
| AC207 | AC207 | S8050 (NPN) | KEEP | Add 5x from starter kit |
| AC208 | AC208 | S8550 (PNP) | KEEP | |
| AC209 | AC209 | A1015 (PNP) | KEEP | |
| AC210 | AC210 | C1815 (NPN) | KEEP | |
| AC211 | - | 4N35 Optocoupler | NEW | From fun kit |

---

#### AC301: Power MOSFET (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (next to AC2xx or separate?)
**Folder**: `docs/components/` (root level)
**Family**: NO (single type - could merge into AC2xx in future)
**Status**: ✅ COMPLETED - Created 2025-11-27

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC301 | - | IRLZ44N N-Ch MOSFET | NEW | Logic-level, TO-220 (10pcs) |

---

#### AC4xx: Small Motors (Drone/Toy) (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Small-Motors/`
**Family**: YES (3 components + anchor)
**Status**: ✅ COMPLETED - Created 2025-11-27

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC400 | - | Small Motors (Drone/Toy) | NEW | Family anchor (index.md) with comparison table |
| AC401 | - | 716 Coreless Motor | NEW | 7x16mm, 3.7-4.2V with propeller (6pcs) |
| AC402 | - | N20 Gear Motor 60RPM | NEW | 3-6V metal gearbox (5pcs) |

---

#### AC5xx: Servos (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Servos/`
**Family**: YES (4 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC500 | - | Servos | NEW | Family anchor (index.md) with comparison table |
| AC501 | AC009 | SG92R Servo | RENAME | 180° rotation (add 2x more) |
| AC502 | - | SG90 180° Servo | NEW | |
| AC503 | - | SG90 360° Continuous | NEW | |

---

#### AC6xx: Cooling Fans (2 Drawers - Same Family) - ✅ COMPLETED
**Physical**: 2 small drawers (12V and 5V, adjacent)
**Folder**: `docs/components/Cooling-Fans/`
**Family**: YES (3 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC600 | - | Cooling Fans | NEW | Family anchor (index.md) with comparison table |
| AC601 | AC010 | 25mm Fan 12V | RENAME | Drawer 1 |
| AC602 | - | 25mm Fan 5V XH2.54 | NEW | Drawer 2, sleeve connector (5pcs) |

---

#### AC8xx: Audio Output (Speakers/Buzzers) (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Audio-Output/`
**Family**: YES (6 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated (incl OT001→AC804)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC800 | - | Audio Output | NEW | Family anchor (index.md) with comparison table |
| AC801 | AC002 | Ultra-thin Speaker | RENAME | Horn speaker |
| AC802 | AC003 | Piezo Ceramic | RENAME | Piezo disc |
| AC803 | AC004 | Passive Buzzer | RENAME | |
| AC804 | OT001 | LM386 Audio Amp | RENAME | Audio amplifier IC |
| AC805 | - | Active Buzzer | NEW | From fun kit (2-3pcs) |

---

#### AC9xx: High-Power LEDs & Lasers (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/High-Power-Light/`
**Family**: YES (4 components + anchor)
**Status**: ✅ COMPLETED - All components created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC900 | - | High-Power Light | NEW | Family anchor (index.md) with comparison table |
| AC901 | - | XPG3 S4 7W LED | NEW | Cold/warm/blue 777lm (10pcs) |
| AC902 | - | Laser Diode Module | NEW | 650nm red 5mW (10pcs) |
| AC903 | - | KY-008 Laser Module | NEW | From old pack |

---

#### AC011: Standard 5mm Indicator LEDs - ✅ COMPLETED
**Physical**: Original packaging (drawer TBD)
**Folder**: `docs/components/` (root level)
**Family**: NO (standalone)
**Status**: ✅ COMPLETED - Created 2025-11-27 (was AC1201 in original plan)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC011 | - | F5 LED 5mm Assorted | CREATED | Blue/green/red/yellow/white/RGB (100pcs) |

---

#### AC012: Solenoid Valve (Bulky Box) - ✅ COMPLETED
**Physical**: Bulky box
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)
**Status**: ✅ COMPLETED - Created 2025-11-27

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC012 | - | 12V Solenoid Valve 1/2" | CREATED | Normally closed (4pcs) |

---

#### AC013: Water Pressure Sensor (Bulky Box) - ✅ COMPLETED
**Physical**: Bulky box (next to AC012)
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)
**Status**: ✅ COMPLETED - Created 2025-11-27

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| AC013 | - | Water Pressure Sensor | CREATED | G1/4 1.2MPa |

---

### RF - Radio/Communication

#### RF101: RFID Reader (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/` (root level)
**Family**: NO (RC522 = MFRC522, same module)
**Status**: ✅ COMPLETED - Created as standalone component

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| RF101 | RF001 | MFRC522 RFID Reader | RENAME | RC522 from starter kit is same module |

---

#### RF2xx: Wireless/Ethernet (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/Wireless-Ethernet/`
**Family**: YES (2 types)
**Status**: ⏸️ PENDING - RF003 still at root

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| RF200 | - | Wireless/Ethernet | NEW | Family anchor (index.md) with comparison table |
| RF201 | RF003 | USR-ES1 W5500 | RENAME | Ethernet module |
| RF202 | - | RF-5V Transceiver | NEW | Wireless module from old pack |

---

#### RF3xx: Infrared (1 Drawer) - NOT YET CREATED
**Physical**: Small drawer
**Folder**: `docs/components/Infrared/`
**Family**: YES (2 types - paired)
**Status**: ⏸️ PENDING - Components not yet created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| RF300 | - | Infrared | NEW | Family anchor (index.md) with comparison table |
| RF301 | - | IR Receiver Module | NEW | From starter kit |
| RF302 | - | IR Remote Control | NEW | Pairs with RF301 |

---

#### RF002: WiFi Antenna - NO FAMILY (Keep as is)
**Physical**: Existing drawer
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| RF002 | RF002 | WiFi Antenna | KEEP | Keep existing ID |

---

### PS - Power Supplies

#### PS1xx: DC-DC Converters (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/DC-DC Converter/` (keep existing)
**Family**: YES (4 components + anchor - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized (PS000 was renamed to PS100)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PS100 | PS000 | DC-DC Converter | RENAMED | Family anchor (PS000→PS100) |
| PS101 | PS001 | TPS63020 | RENAMED | |
| PS102 | PS002 | Step Down | RENAMED | |
| PS103 | PS003 | LAOMAO 3R3 | RENAMED | |

---

#### PA004: Schottky Diodes - ✅ COMPLETED (moved from PS to PA)
**Physical**: Small drawer (existing)
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)
**Status**: ✅ COMPLETED - Created as PA004 instead of PS101

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PA004 | PS101 | Schottky Diodes | RENAMED | Moved from PS to PA category |

---

#### PS2xx: Battery Charging (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/Battery Charging/` (keep existing)
**Family**: YES (4 components + anchor - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PS200 | PS200 | Battery Charging | KEEP | Family anchor with comparison table |
| PS201 | PS201 | TP4056 LiPo Charger | KEEP | |
| PS202 | PS202 | CN3065 Solar Charger | KEEP | |
| PS203 | - | LiPo 3.7V 250mAh | NEW | For RC planes (2pcs) |
| PS204 | - | LiPo 3.7V 350mAh | NEW | For RC planes (2pcs) |
| PS205 | - | RC Battery Charger | NEW | Multi-battery charger |

---

#### PS3xx: LDO (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer (existing)
**Folder**: `docs/components/LDO/` (keep existing)
**Family**: YES (3 components + anchor - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PS300 | PS300 | LDO | KEEP | Family anchor |
| PS301 | PS301 | MCP1700 | KEEP | |
| PS302 | PS302 | HT7333 | KEEP | |

---

#### PS401: Multi-output Power Board - NO FAMILY (Keep as is)
**Physical**: Small drawer (existing)
**Folder**: `docs/components/` (root level)
**Family**: NO (single type)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PS401 | PS401 | Multi-output Power | KEEP | Linear power supply board |

---

### OT - Other/Misc

#### OT1xx: Logic ICs (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/Logic-ICs/`
**Family**: YES (3 components + anchor)
**Status**: ✅ COMPLETED - All components created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| OT100 | - | Logic ICs | NEW | Family anchor (index.md) with comparison table |
| OT101 | - | 74HC595 Shift Register | NEW | DIP-16 (2pcs) |
| OT102 | - | LMC555CN Timer IC | NEW | CMOS 555 (20pcs) |

---

#### OT2xx: RTC Modules (1 Drawer) - ✅ COMPLETED
**Physical**: Small drawer
**Folder**: `docs/components/RTC-Modules/`
**Family**: YES (3 components + anchor)
**Status**: ✅ COMPLETED - All components created

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| OT200 | - | RTC Modules | NEW | Family anchor (index.md) with comparison table |
| OT201 | - | DS1302 RTC Module | NEW | SPI, from old pack |
| OT202 | - | DS1307 RTC Module | NEW | I2C, from starter kit |

---

### SW - Switches & Buttons

#### SW1xx: Physical Switches & Buttons - ✅ COMPLETED
**Physical**: Various drawers (existing)
**Folder**: `docs/components/Switches-Buttons/`
**Family**: YES (8 components + anchor)
**Status**: ✅ COMPLETED - All components created and migrated, plus OT002→SW008

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| SW001 | SW001 | 3-pin MX Switch | KEEP | |
| SW002 | SW002 | Tact Switch Kit | KEEP | |
| SW003 | SW003 | MTS-102/103 Toggle | KEEP | |
| SW004 | SW004 | Momentary Push | KEEP | |
| SW005 | SW005 | Pushbutton | KEEP | |
| SW006 | SW006 | Mini Rocker Switch | KEEP | |
| SW007 | SW007 | Mini Rocker Switch | KEEP | |
| SW008 | OT002 | Key Lock Switch | RENAME | Move from OT |
| SW009 | - | Membrane Switch | NEW | 4x4 matrix from starter kit |

---

### PA - Passive Components

#### PA: Passive Components - ✅ COMPLETED (no families)
**Physical**: Various drawers
**Folder**: `docs/components/` (root level)
**Family**: NO (individual components only)
**Status**: ✅ COMPLETED - PA001-003 kept as is, PA004 created (Schottky Diodes from PS101)

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| PA001 | PA001 | 3296W Potentiometer | KEEP | |
| PA002 | PA002 | Axial Ferrite Beads | KEEP | |
| PA003 | PA003 | Electrolytic Capacitor | KEEP | |
| PA004 | - | RXEF030 PTC Fuse | NEW | 72V 0.3A resettable (10pcs) |

---

### CN - Connectors

#### CN: Connectors - ✅ COMPLETED (no families)
**Physical**: Various drawers (existing)
**Folder**: `docs/components/` (root level)
**Family**: NO (individual components only)
**Status**: ✅ COMPLETED - CN001-004 kept as is

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| CN001 | CN001 | Male Pin Header | KEEP | |
| CN002 | CN002 | Female Pin Header | KEEP | |
| CN003 | CN003 | Battery Spring Contacts | KEEP | |
| CN004 | CN004 | 8-pin DIP Socket | KEEP | |

---

### MC - Microcontrollers

#### MC1xx: ESP32 Family (Multiple Drawers) - ✅ COMPLETED
**Physical**: Multiple drawers (main + "Other" drawer for MC105-107)
**Folder**: `docs/components/esp32/` (keep existing nested structure with Other/ subfolder)
**Family**: YES (8 components + anchor - already exists)
**Status**: ✅ COMPLETED - Kept as is, already properly organized

| New ID | Old ID | Component Name | Status | Notes |
|--------|--------|----------------|--------|-------|
| MC100 | MC100 | ESP32 | KEEP | Family anchor |
| MC101 | MC101 | ESP32-C3 SuperMini | KEEP | Main drawer |
| MC102 | MC102 | ESP32-S3 SuperMini | KEEP | Main drawer |
| MC103 | MC103 | ESP32 CAM OV5640 | KEEP | Main drawer |
| MC104 | MC104 | ESP32 WROOM-32D | KEEP | Main drawer |
| MC105 | MC105 | T-Display ESP32 | KEEP | "ESP32 - Other" drawer |
| MC106 | MC106 | ESP32 LoRa OLED | KEEP | "ESP32 - Other" drawer |
| MC107 | MC107 | ESP32-CYD | KEEP | "ESP32 - Other" drawer |

---

## Summary Statistics

### Total Components
- **Existing components**: 68
- **Components to rename**: 15
- **New component types**: ~75
- **Total component types after**: ~140-145

### Families
- **Families with 2+ types**: 18 families (ENV1xx, ENV2xx, ENV3xx, ENV4xx, IO1xx, IO3xx, IO4xx, IO5xx, IO6xx, IO7xx, AC1xx, AC2xx, AC4xx, AC5xx, AC6xx, AC8xx, AC9xx, RF2xx, RF3xx, PS0xx, PS2xx, PS3xx, OT1xx, OT2xx, MC1xx)
- **Single components (no family)**: ~20 at root level

### Drawer Usage
- **Small drawers needed**: ~28-32
- **Bulky boxes needed**: 2 (AC011, AC012)
- **Total drawers available**: 60
- **Estimated free remaining**: ~28-32 drawers

### Component ID Changes (Renames)

| Old ID | New ID | Component Name | Reason |
|--------|--------|----------------|--------|
| TS001 | ENV101 | DS18B20 | Merge TS into ENV1xx family |
| ENV001 | ENV102 | BME280/BMP280 | Reorganize into ENV1xx family |
| ENV002 | ENV301 | LDR 5528 | Reorganize into ENV3xx family |
| IO001 | IO201 | TTP223 Touch | No family (single type) |
| IO003 | IO301 | KY-040 Rotary | Reorganize into IO3xx family |
| AC002 | AC801 | Speaker | Reorganize into AC8xx family |
| AC003 | AC802 | Piezo Ceramic | Reorganize into AC8xx family |
| AC004 | AC803 | Passive Buzzer | Reorganize into AC8xx family |
| AC009 | AC501 | SG92R Servo | Reorganize into AC5xx family |
| AC010 | AC601 | 25mm Fan 12V | Reorganize into AC6xx family |
| OT001 | AC804 | LM386 Amp | Move from OT to AC8xx |
| OT002 | SW008 | Key Lock Switch | Move from OT to SW |
| RF001 | RF101 | MFRC522 RFID | No family (RC522=MFRC522) |
| RF003 | RF201 | W5500 Ethernet | Reorganize into RF2xx family |

**Total renames**: 14 components (RF002 stays as is)

---

## Family Index Pages - Comparison Tables

Each family `index.md` should include:
- **Purpose**: Brief description
- **Comparison table**: Key specs to help choose
- **When to use**: Guidance for selection
- **{{ children() }} macro**: List components

**Example for ENV100 (Temperature & Humidity Sensors):**
```markdown
# Temperature & Humidity Sensors

Sensors for measuring ambient temperature and/or relative humidity.

## Comparison

| Component | Type | Temp Range | RH Range | Accuracy | Interface | Notes |
|-----------|------|------------|----------|----------|-----------|-------|
| ENV101 (DS18B20) | Temp only | -55 to 125°C | - | ±0.5°C | 1-Wire | Waterproof available |
| ENV102 (BME280) | Temp+RH+Press | -40 to 85°C | 0-100% | ±1°C, ±3% | I2C/SPI | Also pressure |
| ENV103 (DHT11) | Temp+RH | 0 to 50°C | 20-90% | ±2°C, ±5% | 1-Wire | Slow (1Hz) |
| ENV104 (SHT45) | Temp+RH | -40 to 125°C | 0-100% | ±0.1°C, ±1% | I2C | High precision |
| ENV105 (Thermistor) | Temp only | Varies | - | ~1°C | Analog | Needs calibration |

## When to Use
- **DS18B20**: Multiple sensors on one bus, outdoor/waterproof
- **BME280**: Weather stations (temp + humidity + pressure)
- **DHT11**: Quick prototypes, low precision OK
- **SHT45**: High-accuracy (lab, greenhouse)
- **Thermistor**: Simple analog, cost-sensitive

{{ children() }}
```

---

## Folder Structure Preview

```
docs/components/
├── Environmental/
│   ├── Temperature-Humidity/
│   │   ├── index.md (ENV100)
│   │   ├── ENV101.md (DS18B20)
│   │   ├── ENV102.md (BME280)
│   │   └── ...
│   ├── Air-Quality/
│   ├── Light/
│   └── Moisture-Water/
├── Input-Output/
│   ├── Rotary-Joystick/
│   ├── Motion-Orientation/
│   ├── Distance-Proximity/
│   ├── Audio-Input/
│   └── Displays/
├── Actuators/
│   ├── Motor-Drivers/
│   ├── Small-Motors/
│   ├── Servos/
│   ├── Cooling-Fans/
│   ├── Audio-Output/
│   └── High-Power-Light/
├── Communication/
│   ├── Wireless-Ethernet/
│   └── Infrared/
├── Other/
│   ├── Logic-ICs/
│   └── RTC-Modules/
├── Bipolar Junction Transistor/ (existing, keep)
├── DC-DC Converter/ (existing, keep)
├── LDO/ (existing, keep)
├── Battery Charging/ (existing, expand)
├── Magnetic Sensors/ (existing, keep)
├── esp32/ (existing, keep)
└── [Individual components: IO201, AC301, AC011, AC012, AC1201, RF101, RF002, PS101, PS401, SW001-009, PA001-004, CN001-004, etc.]
```

---

## Next Steps (After Your Approval)

1. **Create folder structure**
   - Create all new family folders
   - Move existing components with new IDs
   - Update all front-matter

2. **Generate family index pages**
   - Create `index.md` for all 18 families
   - Add comparison tables
   - Add `{{ children() }}` macros

3. **Create new component pages**
   - Batch-create ~75 new component pages
   - Use AliExpress/Pakronics links for specs
   - Keep names concise for stickers

4. **Update scripts if needed**
   - Ensure `generate_id_registry.py` handles structure
   - Ensure `build_labels.py` works correctly

5. **Regenerate everything**
   - Run `make registry_stickers`
   - Review all stickers (~140-145 total)

6. **Physical reorganization**
   - Print stickers
   - Label drawers
   - Move components

7. **Commit and deploy**
   - Git commit
   - Run `make publish`

---

**Ready to proceed?** Approve this plan and I'll start the reorganization!
