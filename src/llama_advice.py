import requests
import os

API_URL = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def get_disease_info(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        if isinstance(result, dict) and "error" in result:
            return "Error: " + result["error"]
        return result[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"