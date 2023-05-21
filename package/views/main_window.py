import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from package.ui.ui_mainwindow import Ui_MainWindow
from package.views.login import LoginDialog
from package.models.login_model import Login
import package.services.invoice_service as invoice_service
import package.models.invoice_model as invoice_model

#import pdb # pdb.set_trace()

class MainWindow(QMainWindow):
   
    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_login = Login()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def show(self)->None:
        QMainWindow.show(self)
        self.authenticate()
        self.load_data()
        
    def load_data(self):
        print('Loading Data')
        result = invoice_service.search_invoices_by_ref(self.current_login.user_token, 2023,4)
        if result.success:
            invoice_source = invoice_model.InvoiceModel(result.json())
            self.ui.mainTableView.setModel(invoice_source)
            date_delegate = invoice_model.DateDelegate(self.ui.mainTableView)
            currency_delegate = invoice_model.CurrencyDelegate(self.ui.mainTableView)
            
            self.ui.mainTableView.setItemDelegateForColumn(4, currency_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(6, date_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(7, date_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(8, date_delegate)
            
    
    def authenticate(self):
       login = LoginDialog(self.current_login)
       login_result = login.exec_()
       if login_result:
           print('MainWindow: Authenticated')
       else:
           print(f"login result {login_result}")
           self.close()
