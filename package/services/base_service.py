import sys
import requests
from requests.auth import HTTPBasicAuth

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