import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class Credentials:
    consumer_key = '5OflCzFookhIpf5HRzgpIJQymNyjhCY91zPQbA4YEw3jgBAX'
    consumer_secret = 'MtAP4DEaQlBzQGTNRwtRqgjklAihiFnnmG6PHStAdNkHyU1eGynQM0gUu7kQGcw2'
    apiurl = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'  # Fixed URL

class AccessToken:
    @staticmethod
    def get_access_token():
        response = requests.get(
            Credentials.apiurl,
            auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret)
        )
        if response.status_code == 200:
            return response.json().get('access_token', None)
        else:
            print("Error fetching access token:", response.text)
            return None

class Password:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = '174379'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    to_encode = shortcode + passkey + timestamp
    encoded_password = base64.b64encode(to_encode.encode())  # Fixed encoding
    decoded_password = encoded_password.decode('utf-8')



