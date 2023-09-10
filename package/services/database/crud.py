"""Module with the basic data base operations."""
import sys
import logging
from datetime import date
from sqlalchemy.orm import Session
from package.services.database import models
from package.services.database.database import get_data_session 

from sqlalchemy.testing.config import db

def crud_handler(fnc):
    def handler(*args, **kwargs):
        result = None
        data_session = get_data_session()
        try:
            return fnc(data_session, *args, **kwargs)
        except:
            logging.warning(sys.exc_info())
            data_session.rollback()
            raise
    return handler

@crud_handler
def get_bills(data_session):
    return data_session.query(models.Bill).\
        filter(models.Bill.is_active == 1).all()

@crud_handler
def get_bill(data_session, bill_id: int):
    return data_session.get(models.Bill, bill_id)

@crud_handler
def get_invoices(data_session, bill_id: int):
    return data_session.query(models.Invoice).\
            filter(models.Invoice.bill_id == bill_id).all()

@crud_handler
def save_bill(data_session, bill: models.Bill):
    if bill.id is not None:
        db_bill = data_session.get(models.Bill, bill.id)
        db_bill.update_attributes(bill)
        data_session.commit()
        data_session.refresh(db_bill)
        return db_bill
    else:
        data_session.add(bill)
        data_session.commit()
        data_session.refresh(bill)
        return bill

@crud_handler
def save_invoice(data_session, invoice: models.Invoice):
    if invoice.id is not None:
        db_invoice = data_session.get(models.Invoice, invoice.id)
        db_invoice.method = invoice.method
        db_invoice.reference_year = invoice.reference_year
        db_invoice.reference_month = invoice.reference_month
        db_invoice.description = invoice.description
        db_invoice.value = invoice.value
        db_invoice.due_date = invoice.due_date
        db_invoice.completion_date = invoice.completion_date
        db_invoice.pay_day = invoice.pay_day
        db_invoice.status = invoice.status
        data_session.commit()
    else:
        data_session.add(invoice)
        data_session.commit()
        data_session.refresh(invoice)
    return invoice

@crud_handler
def search_invoices(data_session, reference_year: int, reference_month: int):
    return data_session.query(models.Invoice).\
        filter( models.Invoice.reference_year == reference_year,
                models.Invoice.reference_month == reference_month).all()

@crud_handler
def get_processes(data_session):
    return data_session.query(models.Process).all()

@crud_handler
def get_process(data_session, process_id: int):
    return data_session.get(models.Process, process_id)

@crud_handler
def save_process(data_session, process: models.Process):
    if process.id is not None:
        db_process = data_session.get(models.Process, process.id)
        db_process.update_attributes(process)
        data_session.commit()
        data_session.refresh(db_process)
        return db_process
    else:
        process.created_at = date.today()
        data_session.add(process)
        data_session.commit()
        data_session.refresh(process)
        return process

@crud_handler
def get_invoice_details(data_session, invoice_id: int):
    return data_session.query(models.InvoiceDetail).\
            filter(models.InvoiceDetail.invoice_id == invoice_id).all()

@crud_handler
def save_invoice_detail(data_session, invoice_detail: models.InvoiceDetail):
    if invoice_detail.id is not None:
        db_invoice_detail = data_session.get(models.InvoiceDetail, invoice_detail.id)
        db_invoice_detail.description = invoice_detail.description
        db_invoice_detail.value = invoice_detail.value
        db_invoice_detail.date = invoice_detail.date
        db_invoice_detail.locale_description = invoice_detail.locale_description
        data_session.commit()
    else:
        data_session.add(invoice_detail)
        data_session.commit()
        data_session.refresh(invoice_detail)
    return invoice_detail


