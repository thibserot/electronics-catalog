---
id: IO100
name: Magnetic Sensors
title: Magnetic Sensors
category: IO
tags:
  - magnetic
  - switch
  - reed
  - hall
  - proximity
  - step-up
---


# Magnetic Sensors

{{ children() }}

---

## Comparison: Reed vs Hall (A3144E)
| Aspect | Reed Switch | A3144E (Hall) |
|---|---|---|
| Power needed | **None** | **Yes** (≥4.5 V) |
| Output type | Dry contact (polarity‑free) | Open‑collector (active LOW) |
| Bounce | **Yes** (needs debounce) | No (clean edges) |
| Speed | Low–medium | Medium–high |
| Distance/pole | Non‑polarity, needs sufficient field | **Unipolar**; sensitive face/pole matters |
| Robustness | Glass capsule, shock sensitive | Solid‑state |
| Price | Very cheap | Cheap |

**Rule of thumb:** For **simple door/end‑stop** or battery‑off operation, **reed** is perfect. For **RPM** or noisy environments, pick the **Hall**.


---

*QR for printing will appear here after you run the script:*

![QR sticker](../stickers/IO100.png)
