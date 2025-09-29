print("🐍 Script is starting!")
import sys
print(f"Python version: {sys.version}")

print("🚀 Script is running!")

import requests
import base64

print("✅ Libraries imported successfully")

# Test basic request
try:
    response = requests.get("https://httpbin.org/get", timeout=5)
    print(f"🌐 Network test: {response.status_code}")
except Exception as e:
    print(f"❌ Network error: {e}")

print("🏁 Script finished")