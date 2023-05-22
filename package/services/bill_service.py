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