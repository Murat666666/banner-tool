# 🔎 Banner Tool - Mini Recon Framework

A lightweight multi-threaded network reconnaissance tool written in Python.

## 🚀 Features

- TCP Port Scanning
- Banner Grabbing
- Service Detection
- Basic Vulnerability Matching
- Multi-threaded Scanning
- Progress Bar
- Clean Table Output
- JSON Export

## 📦 Installation

```bash
git clone https://github.com/yourusername/banner-tool.git
cd banner-tool
pip install -r requirements.txt

⚡ Usage
python main.py <host> -p <ports>
Examples

Scan common ports:

python main.py example.com -p 21,22,80

Scan range:

python main.py example.com -p 1-1000

Use threads:

python main.py example.com -p 1-1000 -t 20

Only show open ports:

python main.py example.com -p 1-1000 --open-only

Save results:

python main.py example.com -p 1-1000 -o results.json
📊 Output
PORT    STATUS    SERVICE        VULNS
----------------------------------------
22      open      SSH            NO
80      open      HTTP           NO
⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Do not use it on systems without permission.

## 🔥 Live CVE Lookup

The tool integrates with CVE APIs to fetch real-time vulnerability data based on detected service versions.

🧠 Future Improvements
CVE API Integration
Service Fingerprinting
UDP Scanning
Web Dashboard