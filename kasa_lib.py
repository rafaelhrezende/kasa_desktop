import sys
from PySide2 import QtCore, QtGui, QtWidgets

def set_field_to_text(qt_item, json, field_name):
	qt_item.insert(str(json[field_name]))
