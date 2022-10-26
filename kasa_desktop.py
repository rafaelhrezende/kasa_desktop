import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import kasa_login
import kasa_bill
from kasa_service_connect import KasaService

def addJsonFieldToTable(tableWidget, json, field, row_index, columnIndex):
  field_data = str(json[field])
  tableWidget.setItem(row_index, columnIndex,QtWidgets.QTableWidgetItem(field_data))

def add_bill_table(tableWidget, bill, row_index):
  print("add_bill_table")
 
  addJsonFieldToTable(tableWidget, bill,  'id', row_index, 0)
  addJsonFieldToTable(tableWidget, bill,  "title", row_index, 1)
  addJsonFieldToTable(tableWidget, bill,  "description", row_index, 2)
  addJsonFieldToTable(tableWidget, bill,  "category", row_index, 3)
  addJsonFieldToTable(tableWidget, bill,  "initial_value", row_index, 4)
  addJsonFieldToTable(tableWidget, bill,  "payment_day", row_index, 5)

def clearTable(tableWidget):
  print (f'clearTable: Row Count: {tableWidget.rowCount()}')
  while tableWidget.rowCount() > 0:
    tableWidget.removeRow(0)

def load_bills():
  print( "Load Bill")
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
  bill_title = window.bills_table.item(row, 1).text()
  bill_description = window.bills_table.item(row, 2).text()
  bill_category = window.bills_table.item(row, 3).text()
  bill_initial_value = window.bills_table.item(row, 4).text()
  bill_payment_day = window.bills_table.item(row, 5).text()
  bill.openDialog(bill_id, bill_title, bill_description, bill_category, bill_initial_value, bill_payment_day)

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("kasa_desktop.ui", None)

login =  kasa_login.Login(window)
bill = kasa_bill.Bill(window)

window.actionLogin.triggered.connect(login.openLoginDialog)
window.actionNew_User.triggered.connect(login.openUserDialog)
window.actionLoad_Bills.triggered.connect(load_bills)
window.actionNew_Bill.triggered.connect(bill.openDialog)
window.bills_table.cellDoubleClicked.connect(tableBillWidget_cellDoubleClicked)

window.show()
app.exec_()

