import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaBillService, print_token
import kasa_lib 

class Bill:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent
    #self.clear()

  def initiateWidget(self):
    self.billWidget = self.loader.load("kasa_bill.ui", self.parent)
    self.billWidget.savePushButton.clicked.connect(self.save)

  def getIsActiveProp(self):
    return self.billWidget.is_active_checkBox.isChecked()

  def setIsActiveProp(self, state: bool):
    self.billWidget.is_active_checkBox.setChecked(state)    

  def load(self, bill_id):
    if bill_id == False or bill_id == None or bill_id == "":
      return

    bill_result = KasaBillService.load_bill(bill_id)
    if bill_result.success:
      self.bill_id = bill_id

      kasa_lib.set_field_to_text(self.billWidget.titleLineEdit, bill_result.json(), 'title')
      kasa_lib.set_field_to_text(self.billWidget.descriptionLineEdit, bill_result.json(), 'description')
      kasa_lib.set_field_to_text(self.billWidget.categoryLineEdit, bill_result.json(), 'category')
      kasa_lib.set_field_to_text(self.billWidget.initial_valueLineEdit, bill_result.json(), 'initial_value')
      kasa_lib.set_field_to_text(self.billWidget.payment_dayLineEdit, bill_result.json(), 'payment_day')
      self.setIsActiveProp(kasa_lib.get_json_field_value(bill_result.json(), 'is_active', kasa_lib.FieldType.BOOLEAN))

    self.billWidget.messageLabel.setText(bill_result.message)

  def openDialog(self, bill_id=None):
    self.initiateWidget()
    self.bill_id = None
    self.load(bill_id)
    self.billWidget.show()

  def save(self):
    title = self.billWidget.titleLineEdit.text()
    description = self.billWidget.descriptionLineEdit.text()
    category = self.billWidget.categoryLineEdit.text()
    payment_day = self.billWidget.payment_dayLineEdit.text()
    initial_value = self.billWidget.initial_valueLineEdit.text()

    if self.bill_id != None:  
      result = KasaBillService.updateBill(self.bill_id, title, description, category, payment_day, initial_value, self.getIsActiveProp())
    else:
      result = KasaBillService.createBill(title, description, category, payment_day, initial_value, self.getIsActiveProp())

    self.billWidget.messageLabel.setText(result.message)


