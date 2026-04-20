# 📶 Wi-Fi Analyzer

A terminal-based Wi-Fi analyzer built in Python that scans nearby networks and displays signal strength, security type, band, and channel — all in a clean, colored UI.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📸 Features

- Scans all nearby Wi-Fi networks
- Shows **signal strength** with a visual bar indicator
- Displays **security type** (WPA3, WPA2, WPA, Open) with color coding
- Detects **band** (2.4 GHz vs 5 GHz)
- Shows **channel** number
- Sorts networks by signal strength (strongest first)
- Clean, colored terminal output using `rich`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Windows OS (uses `netsh` command)
- Wi-Fi adapter enabled

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/MelodicSam/wifi-analyzer.git
cd wifi-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analyzer
python wifi_analyzer.py
```

---

## 🖥️ Example Output

```
╭─────────────────────────────────────────╮
│  Wi-Fi Analyzer  by MelodicSam          │
│  Scanned at 2026-04-20 02:05:00         │
│  8 networks found                        │
╰─────────────────────────────────────────╯

 #   Network (SSID)       Signal             Strength    Security        Band      Channel
 ─────────────────────────────────────────────────────────────────────────────────────────
 1   HomeNetwork          █████  92%         Excellent   WPA2            5 GHz     36
 2   Office_WiFi          ████░  74%         Good        WPA3            5 GHz     40
 3   Neighbor_2.4         ███░░  55%         Fair        WPA2            2.4 GHz   6
 4   FreePublicWiFi       █░░░░  18%         Weak        Open ⚠          2.4 GHz   1
```

---

## 🛠️ Built With

- [Python](https://python.org) — Core language
- [rich](https://github.com/Textualize/rich) — Terminal UI styling
- `netsh` — Windows built-in network utility

---

## 📚 What I Learned

- Using Python's `subprocess` module to run system commands
- Parsing command-line output with `regex`
- Building clean terminal UIs with the `rich` library
- Wi-Fi concepts: signal strength, bands, channels, security protocols

---

## 🔮 Future Ideas

- [ ] Add Linux/macOS support
- [ ] Export results to CSV
- [ ] Continuous monitoring mode (refresh every N seconds)
- [ ] Show connected network highlighted

---

## 👤 Author

**Swayam Patel** — [@MelodicSam](https://github.com/MelodicSam)

---

## 📄 License

MIT License — feel free to use and modify.
