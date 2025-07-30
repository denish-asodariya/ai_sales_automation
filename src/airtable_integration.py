import os
import requests
from dotenv import load_dotenv

load_dotenv()
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME", "Leads")

AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

def push_to_airtable(name, email, product, priority, generated_email):
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
    "fields": {
        "Name": name,
        "E-mail": email,  
        "Product": product,
        "Priority": priority,
        "Generated Email": generated_email
    }
}

    response = requests.post(AIRTABLE_URL, json=data, headers=headers)
    if response.status_code == 200:
        print(f"Lead {name} synced to Airtable.")
    else:
        print(f"Failed to sync to Airtable: {response.text}")
