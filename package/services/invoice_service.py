import sys
import requests
from requests.auth import HTTPBasicAuth
from package.services.base_service import *

def search_invoices_by_ref(token, refYear, refMonth):
    return request_kasa_service(token, RequestMethods.GET, 'invoices', f'reference_year={refYear}&reference_month={refMonth}')

def search_invoices_totals_by_ref(token, refYear, refMonth):
    return request_kasa_service(token, RequestMethods.GET, 'invoices/totals', f'reference_year={refYear}&reference_month={refMonth}')

