import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import kasa_login
import kasa_bill
import kasa_invoice
from kasa_lib import *

from kasa_service_connect import KasaService

def add_bill_table(tableWidget, bill, row_index):
  addJsonFieldToTable(tableWidget, bill,  'id', row_index, 0)
  addJsonFieldToTable(tableWidget, bill,  "title", row_index, 1)
  addJsonFieldToTable(tableWidget, bill,  "description", row_index, 2)
  addJsonFieldToTable(tableWidget, bill,  "category", row_index, 3)
  addJsonFieldToTable(tableWidget, bill,  "initial_value", row_index, 4)
  addJsonFieldToTable(tableWidget, bill,  "payment_day", row_index, 5)

# Remover
def add_invoice_table(tableWidget, bill_title, invoice, row_index):
  addJsonFieldToTable(tableWidget, invoice,  'id', row_index, 0)
  addJsonFieldToTable(tableWidget, invoice,  'reference_year', row_index, 1)
  addJsonFieldToTable(tableWidget, invoice,  'reference_month', row_index, 2)
  tableWidget.setItem(row_index, 3,QtWidgets.QTableWidgetItem(bill_title))
  addJsonFieldToTable(tableWidget, invoice,  'value', row_index, 4)
  addJsonFieldToTable(tableWidget, invoice,  'method', row_index, 5)
  addJsonFieldToTable(tableWidget, invoice,  'due_date', row_index, 6)
  addJsonFieldToTable(tableWidget, invoice,  'completion_date', row_index, 7)
  addJsonFieldToTable(tableWidget, invoice,  'pay_day', row_index, 8)
  addJsonFieldToTable(tableWidget, invoice,  'status', row_index, 9)

def load_bills():
  clearTable(window.bills_table)
  result = KasaService.load_bills(login.token)
  if result.success:
    bills = result.json()
    for bill in bills:
      row_index = window.bills_table.rowCount()
      row = window.bills_table.insertRow(row_index)
      add_bill_table(window.bills_table, bill, row_index)
  else:
    print(result.message)

def tableBillWidget_cellDoubleClicked(row, column):
  bill_id = window.bills_table.item(row, 0).text()
  bill.openDialog(bill_id)

def load_invoices():
  clearTable(window.invoices_table)
  current_bill_id = get_current_bill_field(0)
  billTitle = window.bills_table.item(window.bills_table.currentRow(), 1).text()
  result = KasaService.load_invoices(current_bill_id)

  if result.success:
    invoices = result.json()
    for invoice in invoices:
      row_index = window.invoices_table.rowCount()
      row = window.invoices_table.insertRow(row_index)
      add_invoice_table(window.invoices_table,billTitle, invoice, row_index)
  else:
    print(result.message)

def tableInvoiceWidget_cellDoubleClicked(row, column):
  invoice_id = window.invoices_table.item(row, 0).text()
  bill_title = window.invoices_table.item(row, 3).text()  
  invoice.openDialog(get_current_bill_field(0), invoice_id, bill_title)

def get_current_bill_field(index):
  return window.bills_table.item(window.bills_table.currentRow(), index).text()

def new_invoice_action():
  current_bill_id = get_current_bill_field(0)
  if current_bill_id == None:
    print ('Bill not selected')
    return

  invoice.openDialog(current_bill_id, bill = get_current_bill_field(1))

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("layouts/kasa_desktop.ui", None)

login =  kasa_login.Login(window)
bill = kasa_bill.Bill(window)
invoice = kasa_invoice.Invoice(window)
invoice_management = kasa_invoice.InvoiceManagement(window)

window.actionLogin.triggered.connect(login.openLoginDialog)
window.actionNew_User.triggered.connect(login.openUserDialog)

window.actionLoad_Bills.triggered.connect(load_bills)
window.actionNew_Bill.triggered.connect(bill.openDialog)
window.bills_table.cellDoubleClicked.connect(tableBillWidget_cellDoubleClicked)
window.bills_table.cellClicked.connect(load_invoices)

window.actionLoad_Invoices.triggered.connect(load_invoices)
window.actionNew_invoice.triggered.connect(new_invoice_action)
window.actionManagement_Invoice.triggered.connect(invoice_management.openDialog)
window.invoices_table.cellDoubleClicked.connect(tableInvoiceWidget_cellDoubleClicked)

window.show()
app.exec_()

