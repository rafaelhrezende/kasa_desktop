import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from enum import Enum

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("layouts/kasa_desktop.ui", None)

class FieldType(Enum):
  STRING = 1
  BOOLEAN = 2

class BaseWindows:
  def __init__(self, parent):
    self.loader = QUiLoader()
    self.parent = parent

  def initiateWidget(self, path):
    self.Widget = self.loader.load(path, self.parent)

  def show(self):
    self.Widget.show()

  def logMessage(self, message):
    self.Widget.messageLabel.setText(message)

def set_field_to_text(qt_item, json, field_name):
  qt_item.insert(get_json_field_value(json, field_name))

def get_json_field_value(json, field_name, field_type: FieldType = FieldType.STRING):

  if field_name in json.keys() and json[field_name] != None:
    if field_type == FieldType.STRING:
      return str(json[field_name])

    if field_type == FieldType.BOOLEAN:
      return json[field_name]

def clearTable(tableWidget):
  while tableWidget.rowCount() > 0:
    tableWidget.removeRow(0)

def addJsonFieldToTable(tableWidget, json, field, row_index, columnIndex):
  tableWidget.setItem(row_index, columnIndex,QtWidgets.QTableWidgetItem(get_json_field_value(json, field)))
