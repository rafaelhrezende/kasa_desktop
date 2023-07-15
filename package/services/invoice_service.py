import sys
from datetime import date
from package.services.base_service import *
from package.services.database import crud

@service_handler
def search_invoices_by_ref(reference_year, reference_month):
    return crud.search_invoices(reference_year, reference_month)

@service_handler
def search_invoices_totals_by_ref(reference_year, reference_month):
    invoices = crud.search_invoices(reference_year, reference_month)
    total = sum(invoice.value for invoice in invoices)
    paid = sum(invoice.value for invoice in invoices
                if invoice.pay_day is not None and invoice.pay_day <= date.today())
    to_pay = total - paid
    scheduled = sum(invoice.value for invoice in invoices
                    if invoice.pay_day is not None and invoice.pay_day > date.today())
    pending = to_pay - scheduled
    return {
        'total': total,
        'paid': paid,
        'to_pay': to_pay,
        'scheduled': scheduled,
        'pending': pending
        }
