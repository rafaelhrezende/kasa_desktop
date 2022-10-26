import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaService, print_token

class Bill:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent
    #self.clear()

  def initiateWidget(self):
    self.billWidget = self.loader.load("kasa_bill.ui", self.parent)
    self.billWidget.savePushButton.clicked.connect(self.save)

  def openDialog(self, bill_id=None, bill_title=None, bill_description=None, bill_category=None, bill_initial_value=None, bill_payment_day=None):
    self.initiateWidget()
    self.bill_id = bill_id
    self.billWidget.titleLineEdit.insert(bill_title)
    self.billWidget.descriptionLineEdit.insert(bill_description)
    self.billWidget.categoryLineEdit.insert(bill_category)
    self.billWidget.initial_valueLineEdit.insert(bill_initial_value)
    self.billWidget.payment_dayLineEdit.insert(bill_payment_day)
    self.billWidget.show()

  def save(self):
    print("save button pressed")
    title = self.billWidget.titleLineEdit.text()
    description = self.billWidget.descriptionLineEdit.text()
    category = self.billWidget.categoryLineEdit.text()
    payment_day = self.billWidget.payment_dayLineEdit.text()
    initial_value = self.billWidget.initial_valueLineEdit.text()

    if self.bill_id != None:  
      result = KasaService.updateBill(self.bill_id, title, description, category, payment_day, initial_value)
    else:
      result = KasaService.createBill(title, description, category, payment_day, initial_value)

    self.billWidget.messageLabel.setText(result.message)
