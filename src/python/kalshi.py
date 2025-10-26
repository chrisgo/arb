import requests
import json
import importlib
import base64
import datetime
from colorama import Fore, Back, Style, Cursor
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature

class Kalshi:
    """Connects to Kalshi"""
    
    def __init__(self):
    	pass


    def list(self):
    	pass


    def get(self):
        base_url = 'https://demo-api.kalshi.co'
        path = '/trade-api/v2/portfolio/balance'
        method = "GET"
        headers = headers(path, method)
        response = requests.get(base_url + path, headers=headers)
        print(response.text)
    	pass


    def load_private_key_from_file(self, file_path):
        with open(file_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,  # or provide a password if your key is encrypted
                backend=default_backend()
            )
        return private_key


    def sign_pss_text(self, private_key: rsa.RSAPrivateKey, text: str) -> str:
        message = text.encode('utf-8')
        try:
            signature = private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.DIGEST_LENGTH
                ),
                hashes.SHA256()
            )
            return base64.b64encode(signature).decode('utf-8')
        except InvalidSignature as e:
            raise ValueError("RSA sign PSS failed") from e


    def headers(self, path, method = 'GET'):
        # (1) Get some variables ready for the signing ceremony
        current_time = datetime.datetime.now()
        timestamp = current_time.timestamp()
        current_time_milliseconds = int(timestamp * 1000)
        header_timestamp = str(current_time_milliseconds)
        # (2) Get the private key
        private_key = load_private_key_from_file('kalshi-key-2.key')
        # (3) Strip query parameters from path before signing
        path_without_query = path.split('?')[0]
        # (4) Build the message string
        message = timestampt_str + method + path_without_query
        # (5) Sign the message
        header_signature = sign_pss_text(private_key, message)
        # (6) Get the access key 
        header_key = 'a952bcbe-ec3b-4b5b-b8f9-11dae589608c'
        headers = {
            'KALSHI-ACCESS-KEY': header_key,
            'KALSHI-ACCESS-SIGNATURE': header_signature,
            'KALSHI-ACCESS-TIMESTAMP': header_timestamp
        }
        return headers


    # def connect(self):
    #     current_time = datetime.datetime.now()
    #     timestamp = current_time.timestamp()
    #     current_time_milliseconds = int(timestamp * 1000)
    #     timestampt_str = str(current_time_milliseconds)

    #     private_key = load_private_key_from_file('kalshi-key-2.key')

    #     method = "GET"
    #     base_url = 'https://demo-api.kalshi.co'
    #     path='/trade-api/v2/portfolio/balance'

    #     # Strip query parameters from path before signing
    #     path_without_query = path.split('?')[0]
    #     msg_string = timestampt_str + method + path_without_query
    #     sig = sign_pss_text(private_key, msg_string)

    #     headers = {
    #         'KALSHI-ACCESS-KEY': 'a952bcbe-ec3b-4b5b-b8f9-11dae589608c',
    #         'KALSHI-ACCESS-SIGNATURE': sig,
    #         'KALSHI-ACCESS-TIMESTAMP': timestampt_str
    #     }
    #     response = requests.get(base_url + path, headers=headers)
    #     print(response.text)


kalshi = Kalshi()