import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(name, product):
    prompt = f"""
    Write a short, friendly follow-up email for {name} about the {product}.
    Limit to 4 sentences. End with a call to action like scheduling a demo or test drive.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI error:", e)
        return f"Hi {name}, thanks for your interest in our {product}! Let’s set up a quick time to connect."
