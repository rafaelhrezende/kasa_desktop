import sys
from datetime import date
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaInvoiceService, print_token
from kasa_lib import *
import pyqtgraph as pg

def fill_invoice_table(invoiceTable, invoicesJson):
  for invoice in invoicesJson:
    row_index = invoiceTable.rowCount()
    row = invoiceTable.insertRow(row_index)
    add_invoice_to_table(invoiceTable, invoice['bill']['title'], invoice, row_index)

def add_invoice_to_table(tableWidget, bill_title, invoice, row_index):
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

class Invoice:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent

  def get_text_if_present(self, qObject):
    return qObject.text() if qObject.text() != "" else None

  def getSelectedDate(self):
    return self.Widget.calendarWidget.selectedDate().toString("yyyy-MM-dd")

  def setDateLineEditValue(self, lineEdit):
    lineEdit.setText(self.getSelectedDate())

  def setDueDatePushButton_clicked(self, event):
    self.setDateLineEditValue(self.Widget.dueDateLineEdit)

  def setCompletionDatePushButton_clicked(self):
    self.setDateLineEditValue(self.Widget.completionDateLineEdit)

  def setPayDayPushButton_clicked(self):
    self.setDateLineEditValue(self.Widget.payDayLineEdit)

  def load(self, bill_id, invoice_id):
    if bill_id == False or bill_id == None or bill_id == "":
      return
    if invoice_id == False or invoice_id == None or invoice_id == "":
      return

    invoice_result = KasaInvoiceService.load_invoice(bill_id, invoice_id)
    if invoice_result:
      self.invoice_id = invoice_id
      set_field_to_text(self.Widget.refYearLineEdit, invoice_result.json(), 'reference_year')
      set_field_to_text(self.Widget.refMonthLineEdit, invoice_result.json(), 'reference_month')
      set_field_to_text(self.Widget.valueLineEdit, invoice_result.json(), 'value')
      set_field_to_text(self.Widget.dueDateLineEdit, invoice_result.json(), 'due_date')
      set_field_to_text(self.Widget.completionDateLineEdit, invoice_result.json(), 'completion_date')
      set_field_to_text(self.Widget.payDayLineEdit, invoice_result.json(), 'pay_day')
      set_field_to_text(self.Widget.statusLineEdit, invoice_result.json(), 'status')
      method_index = self.Widget.methodComboBox.findText(str(invoice_result.json()['method']))
      
      if method_index >= 0:
        self.Widget.methodComboBox.setCurrentIndex(method_index)

    self.Widget.messageLabel.setText(invoice_result.message)

  def initiateWidget(self):
    self.Widget = self.loader.load("layouts/invoice.ui", self.parent)
    self.Widget.savePushButton.clicked.connect(self.save)

    self.Widget.setDueDatePushButton.clicked.connect(self.setDueDatePushButton_clicked)
    self.Widget.setCompletionDatePushButton.clicked.connect(self.setCompletionDatePushButton_clicked)
    self.Widget.setPayDayPushButton.clicked.connect(self.setPayDayPushButton_clicked)

  def openDialog(self, bill_id, invoice_id = None, bill = None):
    self.initiateWidget()
    self.bill_id = bill_id
    self.invoice_id = None
    self.Widget.billLineEdit.insert(bill)
    self.load(bill_id, invoice_id)
    
    self.Widget.show()

  def save(self):
    refYear = self.get_text_if_present(self.Widget.refYearLineEdit)
    refMonth = self.get_text_if_present(self.Widget.refMonthLineEdit)
    value = self.get_text_if_present(self.Widget.valueLineEdit)
    dueDate = self.get_text_if_present(self.Widget.dueDateLineEdit)
    completionDate = self.get_text_if_present(self.Widget.completionDateLineEdit)
    payDay = self.get_text_if_present(self.Widget.payDayLineEdit)
    status = self.get_text_if_present(self.Widget.statusLineEdit)
    method = self.Widget.methodComboBox.currentText()

    if self.invoice_id != None:  
      result = KasaInvoiceService.updateInvoice(self.bill_id, self.invoice_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status)
    else:
      result = KasaInvoiceService.createInvoice(self.bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status)

    self.Widget.messageLabel.setText(result.message)

class InvoiceManagement(BaseWindows):
  def __init__(self, parent):
    BaseWindows.__init__(self, parent)

  def referenceYear(self):
    return self.Widget.referenceYear_spinBox.text()

  def referenceMonth(self):
    return self.Widget.referenceMonth_spinBox.text()

  def invoicesTable(self):
    return self.Widget.invoices_table

  def compute_invoice(self, invoicesJson):
    total = sum(invoice['value'] for invoice in invoicesJson)
    totalPaid = sum(invoice['value'] for invoice in invoicesJson if invoice['status'] == 1)
    totalScheduled = sum(invoice['value'] for invoice in invoicesJson if invoice['status'] == 2)
    totalOpen = sum(invoice['value'] for invoice in invoicesJson if invoice['status'] == 0)

    totalToPay = totalScheduled + totalOpen
    
    self.Widget.total_lineEdit.setText(str(total))
    self.Widget.totalPaid_lineEdit.setText(str(totalPaid))
    self.Widget.totalScheduled_lineEdit.setText(str(totalScheduled))
    self.Widget.totalOpen_lineEdit.setText(str(totalOpen))
    self.Widget.totalToPay_lineEdit.setText(str(totalToPay))

    return [total, totalPaid, totalToPay]

  def clear(self):
    clearTable(self.invoicesTable())
    self.Widget.total_lineEdit.setText('')
    self.Widget.totalPaid_lineEdit.setText('')
    self.Widget.totalScheduled_lineEdit.setText('')
    self.Widget.totalOpen_lineEdit.setText('')
    self.graphWidget.clear()

  def load(self):
    result = KasaInvoiceService.load_invoices_by_ref(self.referenceYear(), self.referenceMonth())
    self.clear()
    fill_invoice_table(self.invoicesTable(), result.json())
    computedValues = self.compute_invoice(result.json())

    self.loadChart(*computedValues)
    self.logMessage(result.message)

  def openDialog(self):
    self.initiateWidget('layouts/invoice_management.ui')
    self.Widget.referenceYear_spinBox.setValue(date.today().year)
    self.Widget.referenceMonth_spinBox.setValue(date.today().month)
    self.Widget.filter_pushButton.clicked.connect(self.load)
    self.graphWidget = pg.PlotWidget()  
    self.Widget.chartArea_verticalLayout.addWidget(self.graphWidget)

    self.load()
    self.show()


  def loadChart(self, total, totalPaid, totalToPay):
    self.graphWidget.addItem(self.createBar([1],[total],'r'))
    self.graphWidget.addItem(self.createBar([2],[totalPaid],'g'))
    self.graphWidget.addItem(self.createBar([3],[totalToPay],'b'))

    labels=[(1, 'A'), (2, 'B'), (3, 'C')]
    self.graphWidget.plot(labels=labels)
    ax =self.graphWidget.getAxis('bottom')
    ax.setTicks([labels])

  def createBar(self, x,y,brush):
    return pg.BarGraphItem(x = x, height = y, width = 0.6, brush = brush)
