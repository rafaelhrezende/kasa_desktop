import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from package.ui.ui_mainwindow import Ui_MainWindow
from package.views.login import LoginDialog
from package.models.login_model import Login

print('Declaring MainWindow')
class MainWindow(QMainWindow):
   
    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_login = Login()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def show(self)->None:
        QMainWindow.show(self)
        self.authenticate()    
    
    def authenticate(self):
       login = LoginDialog(self.current_login,allow_override= False)
       login_result = login.exec_()
       if login_result:
           print('MainWindow: Authenticated')
       else:
           print(f"login result {login_result}")
           self.close()
