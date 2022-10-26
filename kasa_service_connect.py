import sys
import requests
from requests.auth import HTTPBasicAuth

this = sys.modules[__name__]

KASA_SERVICE_URL = 'http://0.0.0.0:8000'

this.current_token = None

def set_token(token):
  this.current_token = token

def print_token():
  print(this.current_token)

class ServiceResult:
  def __init__(self, success, message, result):
    self.success = success
    self.message = message
    self.result = result
  
  def json(self):
    return self.result.json()

class KasaService:
  def authenticate(username, password):
    result = requests.post(f'{KASA_SERVICE_URL}/token', data={'username': username, 'password': password})

    if result:
      return ServiceResult(True, '', result)
    else:
      return ServiceResult(False, result.text, result)

  def createUser(username, password):
    result = requests.post(f'{KASA_SERVICE_URL}/users', json={'email': username, 'password': password})  
    
    if result:
      return ServiceResult(True, 'User created', result)
    else:
      return ServiceResult(False, result.text, result)

  def load_bills(token):
    result = requests.get(f'{KASA_SERVICE_URL}/bills', headers={"Authorization": f"Bearer {token}"})

    if result:
      return ServiceResult(True, None, result)
    else:
      return ServiceResult(False, result.text, result)

  def createBill( title, description, category, payment_day, initial_value):
    result = requests.post(f'{KASA_SERVICE_URL}/bills', headers={"Authorization": f"Bearer {this.current_token}"}, json={
      "title": title,
      "description": description,
      "category": category,
      "payment_day": payment_day,
      "initial_value": initial_value
      } )

    if result:
      return ServiceResult(True, "Bill Created", result)
    else:
      return ServiceResult(False, result.text, result)

  def updateBill(id, title, description, category, payment_day, initial_value):
    result = requests.put(f'{KASA_SERVICE_URL}/bills/{id}', headers={"Authorization": f"Bearer {this.current_token}"}, json={
      "title": title,
      "description": description,
      "category": category,
      "payment_day": payment_day,
      "initial_value": initial_value
      } )

    if result:
      return ServiceResult(True, "Bill Updated", result)
    else:
      return ServiceResult(False, result.text, result)