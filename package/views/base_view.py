from PySide6.QtWidgets import QDialog, QMessageBox

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
    
    def show_error_message(self, message, detail = None):
         return show_message(message, detail, QMessageBox.Icon.Critical)
    
    def show_info_message(self, message, detail = None):
        return show_message(message, detail, QMessageBox.Icon.Information)

def show_message(message:str, detail:str, icon:QMessageBox.Icon):
    message_box = QMessageBox()
    message_box.setText(message)
    message_box.setInformativeText(detail)
    message_box.setIcon(icon)
    return message_box.exec()
        
def show_error_message(message:str, detail:str = None):
    return show_message(message, detail, QMessageBox.Icon.Critical)
    

def _permission_error_handler(fnc):
    def handler( self, *args, **kwargs ):
        try:
            return fnc(self, *args, **kwargs)
        except PermissionError:
            show_error_message('Falha na autenticação!', 'Tente novamente ou retorne para Home e autentique novamente.')
    return handler
