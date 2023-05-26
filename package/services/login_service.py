import sys
import requests
from requests.auth import HTTPBasicAuth
from package.services.base_service import *

def authenticate(user_name, password):
    result = requests.post(f'{KASA_SERVICE_URL}/token', data={'username': user_name, 'password': password})
    return transform_result(result, '', raise_permission_error = False)

def get_user_data(token):
    result = requests.get(f"{KASA_SERVICE_URL}/users/me", headers = set_headers(token))
    return transform_result(result, '', raise_permission_error = False) 