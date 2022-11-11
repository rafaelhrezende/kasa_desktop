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

def headers():
    return {"Authorization": f"Bearer {this.current_token}"}

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

  def load_invoices(bill_id):
    result = requests.get(f'{KASA_SERVICE_URL}/bills/{bill_id}/invoices', headers={"Authorization": f"Bearer {this.current_token}"})

    if result:
      return ServiceResult(True, None, result)
    else:
      return ServiceResult(False, result.text, result)

  

class KasaBillService:
  def load_bill(bill_id):
     result = requests.get(f'{KASA_SERVICE_URL}/bills/{bill_id}', headers=this.headers())
     return transform_result(result, f"Loaded {bill_id}")

  def createBill( title, description, category, payment_day, initial_value):
    result = requests.post(f'{KASA_SERVICE_URL}/bills', headers=this.headers(), json={
      "title": title,
      "description": description,
      "category": category,
      "payment_day": payment_day,
      "initial_value": initial_value
      } )
    return transform_result(result, "Bill Created")

  def updateBill(id, title, description, category, payment_day, initial_value):
    result = requests.put(f'{KASA_SERVICE_URL}/bills/{id}', headers=this.headers(), json={
      "title": title,
      "description": description,
      "category": category,
      "payment_day": payment_day,
      "initial_value": initial_value
      } )
    return transform_result(result, "Bill Updated")

class KasaInvoiceService:
  def load_invoice(bill_id, invoice_id):
    result = requests.get(f'{KASA_SERVICE_URL}/bills/{bill_id}/invoices/{invoice_id}', headers=this.headers())
    return transform_result(result, f"Loaded Bill: {bill_id} | Invoice: {invoice_id}")

  def createInvoice(bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status):
    result = requests.post(f'{KASA_SERVICE_URL}/bills/{bill_id}/invoices/', headers=this.headers(), json={
      "method": method,
      "reference_year": refYear,
      "reference_month": refMonth,
      "value": value,
      "due_date": dueDate,
      "completion_date": completionDate,
      "pay_day": payDay,
      "status": status
      } )
    return transform_result(result, "Invoice Created")

  def updateInvoice(bill_id, invoice_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status):
    result = requests.put(f'{KASA_SERVICE_URL}/bills/{bill_id}/invoices/{invoice_id}/', headers=this.headers(), json={
      "method": method,
      "reference_year": refYear,
      "reference_month": refMonth,
      "value": value,
      "due_date": dueDate,
      "completion_date": completionDate,
      "pay_day": payDay,
      "status": status
      } )
    return transform_result(result, "Invoice Updated")

  def load_invoices_by_ref(refYear, refMonth):
    result = requests.get(f'{KASA_SERVICE_URL}/invoices/?reference_year={refYear}&reference_month={refMonth}', headers=this.headers())
    return transform_result(result, "invoice search completed")
