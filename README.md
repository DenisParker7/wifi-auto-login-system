# 🚀 WiFi Auto Login System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Automation](https://img.shields.io/badge/Automation-WiFi%20Login-orange)

Automates login for captive portal WiFi networks (e.g., college/hostel WiFi).

Once set up, your system will automatically log in whenever internet access is required — no manual intervention needed.

---

## ✨ Features

* 🔐 Secure credential handling using environment variables
* 🔄 Auto-detects internet connectivity
* ⚡ Automatically logs in when disconnected
* 🧠 Retry mechanism for unstable networks
* 🖥️ Can run silently in background

---

## 🛠️ Tech Stack

* Python
* requests
* python-dotenv

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/your-username/wifi-auto-login-system.git
cd wifi-auto-login-system

2. Install dependencies:

pip install -r requirements.txt

---

## ⚙️ Configuration

Create a `.env` file in the root directory:

WIFI_USER=your_username
WIFI_PASS=your_password
LOGIN_URL=http://your-login-url/cgi-bin/authlogin
WIFI_URI=http://example.com
SERVICE_NAME=ProntoAuthentication

⚠️ Do NOT commit `.env` file to GitHub.

---

## ▶️ Usage

Run the script:

python wifi_auto_login.py

---

## 🔁 How It Works

* The script checks internet connectivity every 60 seconds
* If no internet is detected:

  * It opens the captive portal
  * Sends login credentials automatically
* If already connected:

  * It does nothing

---

## ⚠️ Important Notes

* Your WiFi network must have **"Connect Automatically" enabled**
* This script does NOT connect to WiFi — it only logs in
* Runs once every 60 seconds (can be changed in code)

---

## 🤖 Full Automation (Recommended)

### Run in Background (No Terminal)

Rename the file:

wifi_auto_login.py → wifi_auto_login.pyw

This runs the script silently (no command window).

---

### Auto Start Using Task Scheduler

1. Open Task Scheduler
2. Click Create Basic Task
3. Name: WiFi Auto Login
4. Trigger: At system startup
5. Action:
   Program/script: python
   Arguments: C:\path\to\wifi_auto_login.pyw

Now the script runs automatically when your system starts.

---

## 🛑 How to Stop the Script

### If running manually:

Press:
Ctrl + C

---

### If running via Task Scheduler:

Disable task:

1. Open Task Scheduler
2. Find WiFi Auto Login
3. Right-click → Disable

Delete task:

1. Right-click → Delete

---

### Kill running process (if needed)

taskkill /IM python.exe /F

⚠️ This will stop all Python processes.

---

## 🔒 Security

* Credentials are stored in `.env`
* `.gitignore` prevents accidental upload
* No sensitive data is stored in code

---

## 📄 License

MIT License

---

## 🚀 Future Improvements

* GUI dashboard
* Multi-network support
* Notifications on login
* Smarter event-based trigger (instead of loop)
