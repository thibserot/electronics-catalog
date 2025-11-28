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

Network connectivity modules for wired Ethernet and wireless WiFi/RF communication. Enables internet access, local network communication, and IoT applications.

## Comparison

| Component | Type | Range | Interface | Best For |
|-----------|------|-------|-----------|----------|
| [RF201](RF201.md) | Wired Ethernet | N/A (wired) | SPI | Reliable wired connection, no interference |
| [RF202](RF202.md) | 433MHz RF Transceiver | ~100m | UART | Wireless communication, point-to-point |

## Selection Guide

**For reliable wired connection:**
- Use RF201 (W5500 Ethernet)
- No WiFi interference
- More stable than wireless
- PoE capable (with PoE module)
- Industrial applications

**For wireless RF communication:**
- Use RF202 (RF-5V transceiver)
- Simple point-to-point wireless
- Remote control applications
- No internet needed (local wireless only)

## Key Concepts

**Ethernet (W5500):**
- Hardware TCP/IP stack on chip
- SPI interface to MCU
- Handles all network protocols in hardware
- Offloads network processing from MCU

**RF Transceiver (433MHz):**
- Simple wireless serial communication
- Point-to-point or broadcast
- No WiFi/internet (local only)
- Low power, long range

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

**RF Transceiver (RF-5V):**
- 433MHz (unlicensed ISM band)
- Limited data rate
- No error correction (packet loss possible)
- Range depends on environment/antenna

## Typical Applications

**Ethernet (RF201):**
- Industrial automation
- Server room equipment
- Home automation (wired backbone)
- Security systems
- PoE-powered devices

**RF Transceiver (RF202):**
- Wireless sensors
- Remote control
- Point-to-point communication
- Home automation (local only)
- Battery-powered devices

## Components in This Family

{{ children() }}
