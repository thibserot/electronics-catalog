---
id: AC200
name: Transistor
title: Bipolar Junction Transistor
category: AC
tags:
  - transistor
  - bjt
  - npn
  - pnp
  - small-signal
  - selector
short: "Bipolar Junction Transistor"
use: "NPN/PNP"
---

# Small‑signal BJTs – AC2xx family overview - AC200

This family groups together **common small‑signal BJTs** (both NPN and PNP) that you’re likely to reach for when you
need a simple transistor for switching or low‑power amplification. The idea is that you can land on this page, scan the
table, and then jump to the specific device page that best matches your required **voltage**, **current** and **role**.

{{ children() }}

## Quick comparison

| ID | Part | Polarity | Vceo (approx) | Ic max (approx) | Package | Typical role |
|----|------|----------|---------------|-----------------|---------|--------------|
| AC201 | BC337 | NPN | ~45 V | ~800 mA | TO-92 | medium‑current NPN switch / amplifier |
| AC202 | BC327 | PNP | ~45 V | ~800 mA | TO-92 | medium‑current PNP switch / amplifier |
| AC203 | 2N2222 | NPN | ~40 V | ~600 mA | TO-92 / TO-18 | robust NPN switch up to ~500–600 mA |
| AC204 | 2N2907 | PNP | ~40 V | ~600 mA | TO-92 / TO-18 | robust PNP switch up to ~500–600 mA |
| AC205 | 2N3904 | NPN | ~40 V | ~200 mA | TO-92 | low‑current fast NPN general‑purpose |
| AC206 | 2N3906 | PNP | ~40 V | ~200 mA | TO-92 | low‑current fast PNP general‑purpose |
| AC207 | S8050 | NPN | ~25 V | ~1.5 A | TO-92 | low‑voltage NPN up to ~1.5 A |
| AC208 | S8550 | PNP | ~25 V | ~1.5 A | TO-92 | low‑voltage PNP up to ~1.5 A |
| AC209 | A1015 | PNP | ~50 V | ~150 mA | TO-92 / SOT‑23 | audio PNP / small‑signal switch |
| AC210 | C1815 | NPN | ~50 V | ~150 mA | TO-92 / SOT‑23 | audio NPN / small‑signal switch |

Very hand‑wavy guidance:

- Use the **2N3904 / 2N3906 / A1015 / C1815** parts for **signal‑level** and **audio** work up to ~100–150 mA.
- Use **BC337 / BC327** when you want **more current** capability in a very common through‑hole TO‑92 package.
- Use **S8050 / S8550** when you want a cheap **low‑voltage, up‑to‑~1.5 A** discrete transistor instead of a MOSFET module.

From here, jump into the individual part pages (AC201–AC210) for more detail on each device.

---

*QR for printing will appear here after you run the script:*

![QR sticker](../stickers/AC200.png)
