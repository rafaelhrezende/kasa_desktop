import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaInvoiceService, print_token
import kasa_lib

class Invoice:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent
    #self.clear()

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
      kasa_lib.set_field_to_text(self.Widget.refYearLineEdit, invoice_result.json(), 'reference_year')
      kasa_lib.set_field_to_text(self.Widget.refMonthLineEdit, invoice_result.json(), 'reference_month')
      kasa_lib.set_field_to_text(self.Widget.valueLineEdit, invoice_result.json(), 'value')
      kasa_lib.set_field_to_text(self.Widget.dueDateLineEdit, invoice_result.json(), 'due_date')
      kasa_lib.set_field_to_text(self.Widget.completionDateLineEdit, invoice_result.json(), 'completion_date')
      kasa_lib.set_field_to_text(self.Widget.payDayLineEdit, invoice_result.json(), 'pay_day')
      kasa_lib.set_field_to_text(self.Widget.statusLineEdit, invoice_result.json(), 'status')
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
    print("save button pressed")

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