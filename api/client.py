import requests
import json


class APIClient:
    def __init__(self, base_url="https://automationexercise.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.response = None

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        self.response = self.session.get(url, params=params)
        return self.response

    def post(self, endpoint, data=None, json_data=None, files=None):
        url = f"{self.base_url}{endpoint}"
        self.response = self.session.post(url, data=data, json=json_data, files=files)
        return self.response

    def put(self, endpoint, data=None, json_data=None):
        url = f"{self.base_url}{endpoint}"
        self.response = self.session.put(url, data=data, json=json_data)
        return self.response

    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        self.response = self.session.delete(url, data=data)
        return self.response

    def get_status_code(self):
        return self.response.status_code if self.response else None

    def get_response_json(self):
        try:
            return self.response.json()
        except:
            return {}

    def get_response_text(self):
        return self.response.text if self.response else ""

    def verify_response_code(self, expected_code):
        return self.get_status_code() == expected_code

    def verify_response_message(self, expected_message):
        response_data = self.get_response_json()
        return response_data.get('message') == expected_message

    def verify_response_contains(self, key):
        response_data = self.get_response_json()
        return key in response_data