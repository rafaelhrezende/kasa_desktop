import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaService, print_token
import pdb # pdb.set_trace()

class Invoice:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent
    #self.clear()

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

  def initiateWidget(self):
    self.Widget = self.loader.load("layouts/invoice.ui", self.parent)
    self.Widget.savePushButton.clicked.connect(self.save)

    self.Widget.setDueDatePushButton.clicked.connect(self.setDueDatePushButton_clicked)
    self.Widget.setCompletionDatePushButton.clicked.connect(self.setCompletionDatePushButton_clicked)
    self.Widget.setPayDayPushButton.clicked.connect(self.setPayDayPushButton_clicked)

  def openDialog(self, bill_id, invoice_id = None, refYear = None, refMonth = None, bill = None,
                  value = None, method = None, dueDate = None, completionDate = None, payDay = None, status = None):
    self.initiateWidget()
    self.bill_id = bill_id
    self.invoice_id = invoice_id

    self.Widget.refYearLineEdit.insert(refYear)
    self.Widget.refMonthLineEdit.insert(refMonth)
    self.Widget.billLineEdit.insert(bill)
    self.Widget.valueLineEdit.insert(value)
    self.Widget.dueDateLineEdit.insert(dueDate)
    self.Widget.completionDateLineEdit.insert(completionDate)
    self.Widget.payDayLineEdit.insert(payDay)
    self.Widget.statusLineEdit.insert(status)

    method_index = self.Widget.methodComboBox.findText(method)
    if method_index >= 0:
      self.Widget.methodComboBox.setCurrentIndex(method_index)
    
    self.Widget.show()

  def save(self):
    print("save button pressed")

    refYear = self.Widget.refYearLineEdit.text()
    refMonth = self.Widget.refMonthLineEdit.text()
    value = self.Widget.valueLineEdit.text()
    dueDate = self.Widget.dueDateLineEdit.text()
    completionDate = self.Widget.completionDateLineEdit.text()
    payDay = self.Widget.payDayLineEdit.text()
    status = self.Widget.statusLineEdit.text()
    method = self.Widget.methodComboBox.currentText()

    if self.invoice_id != None:  
      result = KasaService.updateInvoice(self.bill_id, self.invoice_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status)
    else:
      result = KasaService.createInvoice(self.bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status)

    self.Widget.messageLabel.setText(result.message)