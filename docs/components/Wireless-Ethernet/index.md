---
id: RF200
name: Wireless & Ethernet
title: Wireless & Ethernet Modules
category: RF
tags:
  - wireless
  - ethernet
  - wifi
  - network
  - connectivity
short: "Network connectivity • WiFi • Ethernet"
use: "internet connectivity, local network"
no_label: true
---

# Wireless & Ethernet Modules - RF200

Network connectivity modules for wired Ethernet and wireless WiFi communication. Enables internet access, local network communication, and IoT applications.

## Components in This Family

{{ children() }}

## Comparison

| Component | Type | Speed | Interface | Best For |
|-----------|------|-------|-----------|----------|
| [RF201](RF201.md) | Wired Ethernet | 10/100 Mbps | SPI | Reliable wired connection, no WiFi interference |
| [RF202](RF202.md) | WiFi 802.11 b/g/n | Up to 72 Mbps | UART (AT commands) | Adding WiFi to non-WiFi MCUs |

## Selection Guide

**For reliable wired connection:**
- Use RF201 (W5500 Ethernet)
- No WiFi interference
- More stable than wireless
- PoE capable (with PoE module)
- Industrial applications

**For wireless connectivity:**
- Use RF202 (ESP-01S WiFi)
- No cables needed
- Mobile/portable devices
- Already have MCU without WiFi

**For new projects:**
- Consider using ESP32 directly (built-in WiFi + Bluetooth)
- Cheaper and more integrated than MCU + WiFi module

## Key Concepts

**Ethernet (W5500):**
- Hardware TCP/IP stack on chip
- SPI interface to MCU
- Handles all network protocols in hardware
- Offloads network processing from MCU

**WiFi Module (ESP8266):**
- Full WiFi stack
- AT command interface via UART
- Can run standalone or as WiFi-to-serial bridge
- 2.4 GHz only (no 5 GHz)

**MAC Address:**
- Unique hardware identifier
- Required for network communication
- Usually pre-programmed in modules

**DHCP:**
- Automatic IP address assignment
- Simplifies network configuration
- Can also use static IP

## Gotchas

**Ethernet (W5500):**
- Requires RJ45 connector + magnetics (usually included on module)
- SPI pins needed (SCK, MISO, MOSI, CS)
- Cable length limited (~100m for Cat5e)
- Need network switch/router

**WiFi (ESP-01S):**
- 2.4 GHz only (crowded band)
- AT commands can be complex
- 3.3V only! (5V will damage)
- Limited GPIO pins exposed
- ESP32 often better choice than Arduino + ESP-01S

## Typical Applications

**Ethernet (RF201):**
- Industrial automation
- Server room equipment
- Home automation (wired backbone)
- Security systems
- PoE-powered devices

**WiFi (RF202):**
- IoT sensors
- Home automation
- Wireless data logging
- Adding WiFi to Arduino
- Portable devices
