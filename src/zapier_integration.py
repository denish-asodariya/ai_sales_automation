import os
import requests
from dotenv import load_dotenv

load_dotenv()
ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

def notify_zapier(name, email, product, priority):
    if not ZAPIER_WEBHOOK_URL:
        print("No Zapier webhook configured.")
        return
    payload = {
        "name": name,
        "email": email,
        "product": product,
        "priority": priority
    }
    response = requests.post(ZAPIER_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print(f"Zapier notified for {name}.")
    else:
        print(f"Zapier notification failed: {response.text}")
