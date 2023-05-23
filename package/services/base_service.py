import sys
import requests
from requests.auth import HTTPBasicAuth
from enum import Enum 

KASA_SERVICE_URL = 'http://0.0.0.0:8000'

def set_headers(token):
    return {"Authorization": f"Bearer {token}"}

def transform_result(result, success_message):
  if result:
    return ServiceResult(True, success_message, result)
  else:
    return ServiceResult(False, result.text, result)

class ServiceResult:
  def __init__(self, success, message, result):
    self.success = success
    self.message = message
    self.result = result
  
  def json(self):
    return self.result.json()

class RequestMethods(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'

def request_kasa_service(token, method:RequestMethods, resource_name, url_params = '', body = None ):
    if len(url_params) > 0:
        url_params = f'/?{url_params}'
    if method == RequestMethods.POST:
        return transform_result(requests.post(f'{KASA_SERVICE_URL}/{resource_name}{url_params}', headers = set_headers(token), json = body ), f'{method}: {resource_name} completed')
    else:
        return transform_result(requests.get(f'{KASA_SERVICE_URL}/{resource_name}{url_params}', headers = set_headers(token)), f'{method}: {resource_name} completed')
    
    
    