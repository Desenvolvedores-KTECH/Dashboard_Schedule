import requests
import base64
import json


URL_TOKEN_GENESYS = 'https://login.mypurecloud.com'


def get_access_token(org:str):
    with open(r'Token/config.json', 'r') as f:
        config = json.load(f)
        
    if org not in config.keys():
        raise Exception(f'Falha no token da organização: {org}')
    authorization = base64.b64encode(bytes(f"{config[org]['CLIENT_ID']}:{config[org]['CLIENT_SECRET']}", "ISO-8859-1")).decode("ascii")

    request_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {authorization}'
    }
    request_body = {
        "grant_type": "client_credentials"
    }

    response = requests.post(
        f'{URL_TOKEN_GENESYS}/oauth/token', data=request_body, headers=request_headers)
    
    result = response.json()
    token = result.get('access_token')
    if token == None:
        raise Exception(f'Falha no token da organização: {org}')
    return token