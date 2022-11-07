import sys
from PySide2 import QtCore, QtGui, QtWidgets

def set_field_to_text(qt_item, json, field_name):
  qt_item.insert(get_json_field_value(json, field_name))

def get_json_field_value(json, field_name):
  if field_name in json.keys() and json[field_name] != None:
    return str(json[field_name])
