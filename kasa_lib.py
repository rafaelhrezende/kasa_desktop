import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

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

def get_json_field_value(json, field_name):
  if field_name in json.keys() and json[field_name] != None:
    return str(json[field_name])

def clearTable(tableWidget):
  print (f'clearTable: Row Count: {tableWidget.rowCount()}')
  while tableWidget.rowCount() > 0:
    tableWidget.removeRow(0)

def addJsonFieldToTable(tableWidget, json, field, row_index, columnIndex):
  tableWidget.setItem(row_index, columnIndex,QtWidgets.QTableWidgetItem(get_json_field_value(json, field)))
