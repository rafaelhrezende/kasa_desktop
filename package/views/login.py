import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from package.ui.ui_login_dialog import Ui_Dialog      
import package.services.login_service as login_service

class LoginDialog(QDialog):
    def __init__(self, current_login, allow_override = True):
        super(LoginDialog, self).__init__()
        self.current_login = current_login
        self.allow_override = allow_override
        self.init_ui()
        
    def init_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.userNameLineEdit.setText(self.current_login.user_name)    
        
    def validate_current_login_state(self):
        result = login_service.get_user_data(self.current_login.user_token)
        return result.success
        
    def authenticate(self):   
        user_name= self.ui.userNameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        result = login_service.authenticate(user_name, password)
        
        if result.success:
            self.current_login.set(user_name, result.json()['access_token'])
            self.current_login.save()
        
        self.ui.messageLabel.setText(result.message)
        return result.success
    
    def done(self, arg__1:int)->None:
        if arg__1 == 1 :
            if (self.authenticate()):
                QDialog.done(self, arg__1)
        else:            
            QDialog.done(self, arg__1)
    
    def exec_(self)->int:
        if self.allow_override == True and self.validate_current_login_state():
            return QDialog.DialogCode.Accepted
        return QDialog.exec_(self)
    