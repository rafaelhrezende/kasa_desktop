import logging
from sqlalchemy import exc
from datetime import date
from package.services.database.models import Process, Invoice
from package.services.database import crud

process_info = {
    "key": "Create-Month-Invoices",
    "ExpectedParametersQuantity": 3,
    "ExpectedParameters": ["Year", "Month", "default_method"]
    }

def update_process_initialize(process: Process):
    process.start_at = date.today()
    process.status = 'Started'
    crud.save_process(process)

def update_process_finishing(process, status, observation):
    process.finish_at = date.today()
    process.status = status
    process.observation = observation
    crud.save_process(process)
    
def execute_process(process: Process, params):
    print("Process initialized")
    update_process_initialize(process)
    
    try:
        param_year = params['Year']
        param_month = params['Month']
        param_default_method = params['default_method']
        
        all_bills = crud.get_bills()

        current_invoices = crud.search_invoices(param_year, param_month)
        filtered_bills = filter(lambda bill: bool(bill.is_active) is True and
                                bill.id not in [invoice.bill_id for invoice in current_invoices],
                                all_bills)
        qtd = 0
        for bill in list(filtered_bills):
            invoice = Invoice(
                method =  param_default_method,
                reference_year = int(param_year),
                reference_month = int(param_month),
                value = bill.initial_value,
                status = 0,
                due_date = date.today(),
                bill_id = bill.id)
            crud.save_invoice(invoice)
            qtd += 1
        message = f"Invoices Created: {qtd}."
        update_process_finishing(process, 'Completed', message)
    except (ValueError, exc.SQLAlchemyError) as error:
        update_process_finishing(data_base, process, 'Fail', f"Exception: {error}")

def get_parameter(params, name):
    return list(filter(lambda param: param['name'] == name, params))[0]

def validate_params(process_key, params):
    print("params: ")
    print(params)
    if process_key != process_info['key']:
        return False, "Invalid process Key"
    if len(params) != process_info['ExpectedParametersQuantity']:
        return False, "Incorrect number of parameters"
    for param in params:
        if param.name not in process_info['ExpectedParameters']:
            return False, f'Invalid parameter {param.name}'
    return True, None
    
    