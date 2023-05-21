import sys
import requests
from requests.auth import HTTPBasicAuth
from package.services.base_service import *

def search_invoices_by_ref(token, refYear, refMonth):
    result = requests.get(f'{KASA_SERVICE_URL}/invoices/?reference_year={refYear}&reference_month={refMonth}', headers=set_headers(token))
    return transform_result(result, "invoice search completed")