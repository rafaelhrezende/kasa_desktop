import sys
import requests
from requests.auth import HTTPBasicAuth
from package.services.base_service import *

def get_bills(token):
    return request_kasa_service(token, RequestMethods.GET, 'bills')

def get_bill(token, id:int):
    return request_kasa_service(token, RequestMethods.GET, f'bills/{id}')

def get_bill_invoices(token, id:int):
    return request_kasa_service(token, RequestMethods.GET, f'bills/{id}/invoices')

def create_invoice(token, bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status=-1):
    body = {
      "method": method,
      "reference_year": refYear,
      "reference_month": refMonth,
      "value": value,
      "due_date": dueDate,
      "completion_date": completionDate,
      "pay_day": payDay,
      "status": status
      }
    return request_kasa_service(token, RequestMethods.POST, f'bills/{bill_id}/invoices/', body = body)
