import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def sentiment(payload):
    """
    Queries the Hugging Face model with the given payload.
    """
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print('response', response)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    
