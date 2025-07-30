import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_lead(name, product):
    prompt = f"""
    You are a sales lead classifier. 
    Based on the following lead information, output ONLY one word: Hot, Warm, or Cold.
    Lead: {name}, Interested Product: {product}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI error:", e)
        return "Warm"  # fallback for demo
