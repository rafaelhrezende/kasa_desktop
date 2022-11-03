import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from kasa_service_connect import KasaService, set_token

class Login:
    
    def __init__(self, parent):
        self.loader = QUiLoader()
        self.parent = parent
        self.clear()

    def clear(self):
        set_token(None)
        self.accessToken = None
        self.userName = None
        self.parent.username_label.setText(self.userName)
        self.parent.actionLoad_Bills.setEnabled(False)
        self.parent.actionNew_Bill.setEnabled(False)

    def openLoginDialog(self):
        self.loginWidget = self.loader.load("layouts/login.ui", self.parent)
        self.loginWidget.loginButton.clicked.connect(self.authenticate)
        self.loginWidget.messageLabel.setText('')
        self.loginWidget.show()

    def authenticate(self):
        self.clear()
        self.userName = self.loginWidget.userNameLineEdit.text()
        password = self.loginWidget.passwordLineEdit.text()
        result = KasaService.authenticate(self.userName, password)
        if result.success:
            self.token = result.json()['access_token']
            set_token(self.token)
            self.loginWidget.messageLabel.setText('User Authenticated')
            self.parent.username_label.setText(self.userName)
            self.parent.actionLoad_Bills.setEnabled(True)
            self.parent.actionNew_Bill.setEnabled(True)
            
            self.loginWidget.hide()
            del self.loginWidget
        else:
            self.userName = None
            self.loginWidget.messageLabel.setText(result.message)

    def openUserDialog(self):
        self.createWidget = self.loader.load("kasa_user.ui", self.parent)
        self.createWidget.createButton.clicked.connect(self.createUser)
        self.createWidget.show()
    
    def createUser(self):
        username = self.createWidget.userNameLineEdit.text()
        password = self.createWidget.passwordLineEdit.text()
        confirm_password = self.createWidget.passwordLineEdit_2.text()
        if len(username) < 4:
            self.createWidget.messageLabel.setText('User Name is too short')
            return
        if password != confirm_password:
            self.createWidget.messageLabel.setText('Password are not equals')
            return

        result = KasaService.createUser(username, password)
        self.createWidget.messageLabel.setText(result.message)