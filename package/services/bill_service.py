import sys
from package.services.base_service import *
from package.services.database import crud
from package.services.database import models

@service_handler
def get_bills():
    return crud.get_bills()

@service_handler
def get_bill(id:int):
    return crud.get_bill(id)

@service_handler
def get_bill_invoices(bill_id:int):
    return crud.get_invoices(bill_id)

@service_handler
def save_invoice(bill_id, reference_year, reference_month, value, method, due_date, completion_date, pay_day, status=-1, invoice_id = None):
    invoice = models.Invoice(
        id=invoice_id,
        method=method,
        reference_year=reference_year,
        reference_month=reference_month,
        description='',
        value=value,
        due_date=convert_text_to_date(due_date),
        completion_date=convert_text_to_date(completion_date),
        pay_day=convert_text_to_date(pay_day),
        status=status,
        bill_id=bill_id)
    
    return crud.save_invoice(invoice)

@service_handler
def saveBill(title, description, category, payment_day, initial_value, is_active, bill_id = None):
    bill = models.Bill(
        id=bill_id,
        title=title,
        description=description,
        category=category,
        initial_value=initial_value,
        payment_day=payment_day,
        is_active=is_active)
    
    return crud.save_bill(bill)


