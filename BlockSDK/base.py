from datetime import date, datetime, timedelta
import requests 
import json

class Base:
    def __init__(self, api_token, endpoint="https://testnet-api.blocksdk.com"):
        self.api_token = api_token
        self.endpoint = endpoint

    def request(self, method, path, data = {}):
        url = f"{self.endpoint}/v3{path}"

        headers = {
            'x-api-token': self.api_token
        }

        try:
            if method == "GET":
                params = "&".join([f"{key}={value}" for key, value in data.items()])
                full_url = f"{url}?{params}"
                response = requests.get(full_url, headers=headers)

            elif method == "POST":
                headers['Content-Type'] = 'application/json'
                response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                payload = response.json().get('payload', {})
                payload['requestData'] = data
                return payload
            else:
                print(f"Error: {response.status_code}")
                return False

        except Exception as e:
            print(url)
            print(e)
            return False
#print(baseInstance.getUsage({'start_date': '','end_date': ''}))
# print(baseInstance.getHashType({'hash':'000000000000000089d2938df30be807844feea4c3340ad32873bb1b692b7f1a'}))
