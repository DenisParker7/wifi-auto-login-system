import requests
import time
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# 🔐 Get credentials
USER_ID = os.getenv("WIFI_USER")
PASSWORD = os.getenv("WIFI_PASS")

# 🌐 Configurable settings
LOGIN_URL = os.getenv("LOGIN_URL", "http://172.16.1.1/cgi-bin/authlogin")
URI = os.getenv("WIFI_URI", "http://example.com")
SERVICE_NAME = os.getenv("SERVICE_NAME", "ProntoAuthentication")

if not USER_ID or not PASSWORD:
    print("❌ ERROR: WIFI_USER or WIFI_PASS not set!")
    exit()

DATA = {
    "userId": USER_ID,
    "password": PASSWORD,
    "serviceName": SERVICE_NAME,
    "URI": URI
}

def check_internet():
    try:
        response = requests.get("http://clients3.google.com/generate_204", timeout=5)
        return response.status_code == 204
    except:
        return False

def login():
    try:
        session = requests.Session()

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        print("⏳ Waiting for network...")
        time.sleep(5)

        # 🔁 Retry opening login page (clean handling)
        success = False

        for i in range(5):
            try:
                session.get(
                    f"{LOGIN_URL}?URI={URI}",
                    headers=headers,
                    timeout=5
                )
                success = True
                break
            except:
                print(f"🔁 Retry {i+1}/5...")
                time.sleep(2)

        if not success:
            print("⚠️ Network not ready, will retry later")
            return

        # Step 2: Send login POST
        response = session.post(
            LOGIN_URL,
            data=DATA,
            headers=headers,
            timeout=5
        )

        if "logged in" in response.text.lower():
            print("✅ Logged in successfully!")
        else:
            print("⚠️ Login may have failed")

    except Exception as e:
        print("❌ Error:", e)

# 🔄 Auto reconnect loop
while True:
    if not check_internet():
        print("🔌 No internet... logging in")
        login()
    else:
        print("🌐 Already connected")

    time.sleep(60)