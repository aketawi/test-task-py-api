import os
import requests

"""
Documentation: https://apilayer.com/marketplace/sentiment-api#documentation-tab
"""

URL = "https://api.apilayer.com/sentiment/analysis"

async def analyze(text: str) -> str:
    payload = text.encode("utf-8")
    headers = { "apikey": os.environ["APILAYER_TOKEN"] }
    response = requests.request("POST", URL, headers=headers, data=payload)

    if response.status_code >=300 or response.status_code <200:
        print("Error while requesting sentiment analysis: ", response.status_code)
        return "unknown"
    
    data = response.json()
    try: 
        return data["sentiment"].strip()
    except Exception as e: 
        print("Error while processing sentiment analysis: \n", e)
        return "unknown"
