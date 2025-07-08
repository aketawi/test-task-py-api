import os
import requests

"""
Documentation: https://apilayer.com/marketplace/sentiment-api#documentation-tab
"""

URL = "https://api.apilayer.com/sentiment/spamchecker"

def analyze():
    payload = "waaaaaa im so sad lol this si the worst evarr".encode("utf-8")
    headers= {
      "apikey": os.environ["APILAYER_TOKEN"]
    }

    response = requests.request("POST", URL, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    print(status_code, result)
