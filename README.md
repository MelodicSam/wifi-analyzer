<div align="center">



<br/>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge&logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00D9FF?style=for-the-badge)

<br/>

> **A powerful terminal-based Wi-Fi analyzer that scans nearby networks and displays signal strength, security type, frequency band, and channel — all in a stunning colored UI.**

<br/>

---

</div>

## ✨ Features

| Feature | Description |
|--------|-------------|
| 📡 **Network Scanner** | Detects all nearby Wi-Fi networks instantly |
| 📊 **Signal Strength** | Visual bar indicator + percentage for each network |
| 🔒 **Security Analysis** | Color-coded WPA3 / WPA2 / WPA / Open detection |
| 📻 **Band Detection** | Identifies 2.4 GHz vs 5 GHz networks |
| 📺 **Channel Info** | Displays the channel each network is broadcasting on |
| 🎨 **Rich Terminal UI** | Beautiful colored output using the `rich` library |
| 🔃 **Auto Sort** | Networks sorted by signal strength (strongest first) |

---

## 🖥️ Preview

```
╭──────────────────────────────────────────────────────────╮
│  📶 Wi-Fi Analyzer  by MelodicSam                        │
│  Scanned at 2026-04-20 02:26:00  |  8 networks found     │
╰──────────────────────────────────────────────────────────╯

 #   Network (SSID)        Signal              Strength     Security        Band       Channel
 ─────────────────────────────────────────────────────────────────────────────────────────────
 1   HomeNetwork_5G        █████  96%          Excellent    WPA3            5 GHz      36
 2   Swayam_WiFi           ████░  78%          Good         WPA2            5 GHz      40
 3   Office_Network        ███░░  52%          Fair         WPA2            2.4 GHz    6
 4   Neighbor_Home         ██░░░  34%          Weak         WPA2            2.4 GHz    11
 5   FreePublicWiFi        █░░░░  15%          Very Weak    Open ⚠          2.4 GHz    1

╭──────────────────────────────────────────────────────────╮
│  Legend                                                   │
│  WPA3 = Most secure   WPA2 = Secure   WPA = Outdated     │
│  Open ⚠ = No password    5GHz = Fast   2.4GHz = Range    │
╰──────────────────────────────────────────────────────────╯
```

---

## 🚀 Getting Started

### Prerequisites

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=flat&logo=windows&logoColor=white)
![WiFi](https://img.shields.io/badge/Wi--Fi-Adapter_Required-00D9FF?style=flat)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/MelodicSam/wifi-analyzer.git

# 2. Navigate into the folder
cd wifi-analyzer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run it!
python wifi_analyzer.py
```

---

## 🛠️ Built With

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich_Library-grey?style=for-the-badge&logo=pypi&logoColor=white)
![Windows Terminal](https://img.shields.io/badge/Windows_Terminal-4D4D4D?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-Parsing-orange?style=for-the-badge)
![Netsh](https://img.shields.io/badge/Netsh-Windows_CLI-0078D6?style=for-the-badge&logo=windows&logoColor=white)

</div>

---

## 📂 Project Structure

```
📁 wifi-analyzer/
├── 📄 wifi_analyzer.py    # Main script
├── 📄 requirements.txt    # Dependencies
├── 📄 .gitignore          # Git ignore rules
└── 📄 README.md           # You are here!
```

---

## 📚 What I Learned

- 🐍 Using Python's `subprocess` module to run system commands
- 🔍 Parsing CLI output with **Regular Expressions (regex)**
- 🎨 Building beautiful terminal UIs with the `rich` library
- 📡 Wi-Fi concepts: signal strength (dBm), bands, channels, security protocols (WPA2/WPA3)
- 🗂️ Structuring a clean, professional GitHub repository

---

## 🔮 Upcoming Features

- [ ] 🐧 Linux & macOS support
- [ ] 📁 Export results to CSV / JSON
- [ ] 🔄 Live monitoring mode (auto-refresh every N seconds)
- [ ] 🌐 Show currently connected network highlighted
- [ ] 📈 Signal strength history graph

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

<div align="center">

**Swayam Patel**

[![GitHub](https://img.shields.io/badge/GitHub-MelodicSam-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MelodicSam)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Swayam_Patel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/swayam-patel-131b84339/)
[![Email](https://img.shields.io/badge/Email-swayampatel2827@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:swayampatel2827@gmail.com)

</div>

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**If you found this useful, please consider giving it a ⭐ — it means a lot!**

![Wave](https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg)

</div>
