import requests
import time
import os

#LOGIN_URL = "http://phc.prontonetworks.com/cgi-bin/authlogin" #DNS Failed so using IP
LOGIN_URL = "http://172.16.1.1/cgi-bin/authlogin"

# 🔐 Get credentials securely from environment variables
USER_ID = os.getenv("WIFI_USER")
PASSWORD = os.getenv("WIFI_PASS")

if not USER_ID or not PASSWORD:
    print("❌ ERROR: WIFI_USER or WIFI_PASS not set!")
    exit()

DATA = {
    "userId": USER_ID,
    "password": PASSWORD,
    "serviceName": "ProntoAuthentication",
    "URI": "http://example.com"
}

def check_internet():
    try:
        response = requests.get("http://clients3.google.com/generate_204", timeout=5)

        # Real internet returns 204 (No Content)
        if response.status_code == 204:
            return True
        else:
            return False

    except:
        return False

def login():
    try:
        session = requests.Session()

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # ⏳ Wait for WiFi to stabilize
        print("⏳ Waiting for network...")
        time.sleep(5)

        # Step 1: Try opening login page (retry if DNS fails)
        for i in range(5):
            try:
                session.get(
                    "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect",
                    headers=headers,
                    timeout=5
                )
                break
            except:
                print(f"🔁 Retry {i+1}/5...")
                time.sleep(2)

        # Step 2: Send login POST
        response = session.post(
            "http://phc.prontonetworks.com/cgi-bin/authlogin",
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