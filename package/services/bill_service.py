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

def save_invoice(token, bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status=-1, invoice_id = None):
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
    if invoice_id is None:
        return request_kasa_service(token, RequestMethods.POST, f'bills/{bill_id}/invoices/', body = body)
    else:
        return request_kasa_service(token, RequestMethods.PUT, f'bills/{bill_id}/invoices/{invoice_id}', body = body)

def saveBill(token, title, description, category, payment_day, initial_value, is_active, bill_id = None):
    body = {
      "title": title,
      "description": description,
      "category": category,
      "payment_day": payment_day,
      "initial_value": initial_value,
      "is_active": is_active
    }

    if bill_id is None:
        return request_kasa_service(token, RequestMethods.POST, f'bills', body = body)
    else:
        return request_kasa_service(token, RequestMethods.PUT, f'bills/{bill_id}', body = body)
