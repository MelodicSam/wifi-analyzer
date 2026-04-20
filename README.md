<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=210&section=header&text=Wi-Fi%20Analyzer&fontSize=50&fontAlignY=36&desc=Scan%20Nearby%20Networks%20with%20a%20Clean%20Python%20CLI&descAlignY=58&color=0:0f172a,50:0ea5e9,100:22d3ee"/>

# 📶 Wi-Fi Analyzer

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2600&pause=900&color=00D9FF&center=true&vCenter=true&width=700&lines=Scan+Nearby+Networks;Analyze+Signal+Strength+and+Security;Built+with+Python+and+Rich" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Terminal UI](https://img.shields.io/badge/UI-Rich_Terminal-111827?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-06b6d4?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<br/><br/>

> **Wi-Fi Analyzer** is a Python-based terminal tool that scans nearby wireless networks and displays **signal strength, security type, frequency band, and channel information** in a clean, colorful interface.

</div>

---

## ✨ Overview

This project gives you a fast way to inspect nearby Wi-Fi networks directly from the terminal.  
It is lightweight, simple to run, and especially useful for students, homelab users, and anyone learning networking fundamentals.

---

## 🧭 Visual Summary

<div align="center">

| Scan | Analyze | Understand |
|:---:|:---:|:---:|
| 📡 Detect nearby Wi-Fi networks | 📶 Measure signal quality | 🔐 Inspect security and band |

</div>

---

## 🎯 Features

<div align="center">

| Feature | Description |
|---|---|
| 📡 **Network Scan** | Detects nearby Wi-Fi networks |
| 📶 **Signal Strength** | Shows percentages with visual strength bars |
| 🔐 **Security Detection** | Identifies WPA3, WPA2, WPA, and Open networks |
| 📊 **Band Detection** | Distinguishes between 2.4 GHz and 5 GHz |
| 📍 **Channel Display** | Shows the Wi-Fi channel number |
| ⚡ **Sorted Output** | Lists strongest signals first |
| 🎨 **Rich UI** | Clean terminal interface powered by `rich` |

</div>

---

## 🖼️ How It Works

```text
[ Wi-Fi Adapter ]
        │
        ▼
[ netsh wlan show networks mode=bssid ]
        │
        ▼
[ Python Parser + Regex ]
        │
        ▼
[ Signal / Security / Band / Channel Extraction ]
        │
        ▼
[ Rich Terminal Table Output ]
```

---

## 🖥️ Example Output

```text
╭─────────────────────────────────────────╮
│  Wi-Fi Analyzer  by MelodicSam          │
│  Scanned at 2026-04-20 02:05:00         │
│  8 networks found                       │
╰─────────────────────────────────────────╯

 #   Network (SSID)       Signal             Strength    Security        Band      Channel
 ─────────────────────────────────────────────────────────────────────────────────────────
 1   HomeNetwork          █████  92%         Excellent   WPA2            5 GHz     36
 2   Office_WiFi          ████░  74%         Good        WPA3            5 GHz     40
 3   Neighbor_2.4         ███░░  55%         Fair        WPA2            2.4 GHz   6
 4   FreePublicWiFi       █░░░░  18%         Weak        Open ⚠          2.4 GHz   1
```

---

## 📊 Signal Strength Guide

<div align="center">

| Bars | Range | Quality |
|:---:|:---:|:---:|
| █████ | 80–100% | Excellent |
| ████░ | 60–79% | Good |
| ███░░ | 40–59% | Fair |
| ██░░░ | 20–39% | Poor |
| █░░░░ | 0–19% | Weak |

</div>

---

## 🔐 Security Types at a Glance

<div align="center">

| Security | Meaning |
|---|---|
| **WPA3** | Strong modern protection |
| **WPA2** | Common and secure |
| **WPA** | Older and weaker |
| **Open ⚠** | No password protection |

</div>

---

## 🚀 Installation

### 1) Clone the repository

```bash
git clone https://github.com/MelodicSam/wifi-analyzer.git
cd wifi-analyzer
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the analyzer

```bash
python wifi_analyzer.py
```

---

## 🛠️ Built With

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-374151?style=for-the-badge)
![Regex](https://img.shields.io/badge/Regex-Parsing-0ea5e9?style=for-the-badge)
![netsh](https://img.shields.io/badge/netsh-Windows_Network_Utility-0078D6?style=for-the-badge&logo=windows&logoColor=white)

</div>

---

## 📚 What I Learned

- Using Python's `subprocess` module to run system commands
- Parsing command-line output with regex
- Building a clean terminal UI with `rich`
- Understanding Wi-Fi basics like channels, bands, and security types

---

## 🗺️ Future Improvements

- [ ] Linux support
- [ ] macOS support
- [ ] Export results to CSV
- [ ] Continuous monitoring mode
- [ ] Highlight currently connected network

---

## 👤 Author

<div align="center">

**Swayam Patel**

[![GitHub](https://img.shields.io/badge/GitHub-MelodicSam-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MelodicSam)

</div>

---

## 📄 License

MIT License — free to use and modify.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:0f172a,50:0ea5e9,100:22d3ee"/>

</div>
