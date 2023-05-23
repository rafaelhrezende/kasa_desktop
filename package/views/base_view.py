from PySide6.QtWidgets import QDialog

import pdb

PROPERTY_MODEL_NAME = 'model_name'

class BaseFormDialog(QDialog):
    def __init__(self, ui):
        super(BaseFormDialog, self).__init__()
        self.ui = ui
        self.init_ui()
        self.children_list = []
        
    widget_style_sheet_invalid = u"color: rgb(255, 0, 0);"
    widget_style_sheet_valid = u"color: rgb(0, 255, 127);"
    
    def init_ui(self):
        self.ui.setupUi(self)
        self.connect_slots()
    
    def connect_slots(self):
        pass
    
    def load_children_to_list(self, widget):
        for child in widget.children():
            if child.property(PROPERTY_MODEL_NAME) != None:
                self.children_list.append(child)
            self.load_children_to_list(child)        
    
    def validate_widget_invalid(self, invalid_models_names):
        if len(self.children_list) == 0:
            self.load_children_to_list(self)
        
        for widget in self.children_list:
            if widget.property(PROPERTY_MODEL_NAME) in invalid_models_names:
                widget.setStyleSheet(self.widget_style_sheet_invalid)
            else:
                widget.setStyleSheet(self.widget_style_sheet_valid)