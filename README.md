Simple Recon Scanner

🔍🔥 Simple Recon Scanner 🔥🔍 is a Python CLI tool that performs quick reconnaissance
on a target IP or domain using multiple public OSINT sources.

It combines Shodan, HackerTarget, and IP-API lookups into a single run
so you can get useful information fast without switching tools.

=========================================

👀 Overview

Recon usually means opening multiple websites,
copy-pasting targets,
and waiting for results 😵‍💫

This tool automates that process.
Enter a target once,
and it fetches available data from different services instantly.

=========================================

🚀 Features

- Optional Shodan lookup using API key 🔑  
- Free Nmap scan via HackerTarget 🌐  
- IP and geolocation info using IP-API 📍  
- Works with IP addresses and domains  
- Beginner-friendly and interactive  

=========================================

⚙️ How It Works

The tool asks for a target and an optional Shodan API key.

If a key is provided,
it fetches host information from Shodan.

Regardless of Shodan usage,
it also queries HackerTarget for Nmap data
and IP-API for basic IP intelligence.

Results are printed directly to the terminal.

=========================================

🧪 Usage

Run the program  
python simple_scanner.py

Enter the target when prompted.
Provide a Shodan API key if you have one,
or press Enter to skip.

=========================================

📤 Example Output

--- Shodan Lookup ---  
Status: 200  

--- Hackertarget Nmap ---  
Status: 200  

--- IP-API Info ---  
Status: 200  

=========================================

📦 Requirements

- Python 3.x  
- requests library  

Install requests if needed  
pip install requests

=========================================

🗿 Final Words

Recon doesn’t need to be complicated.
Sometimes all you need is one script
that asks the right questions 🔥

=========================================
