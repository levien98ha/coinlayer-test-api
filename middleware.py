import requests
from config import private_key, api_url
import time

retries=3
delay=2

def handle_request(endpoint):
    price_endpoint = f"{api_url}{endpoint}?access_key={private_key}"

    for attempt in range(retries):
        try:
            response = requests.get(price_endpoint)
            return handle_response(response)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        
        if attempt < retries - 1:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

def handle_response(response):
    response_format = response.json()
    if response_format["success"]:
        return response_format
    else:
        print(f"Unexpected Error")
