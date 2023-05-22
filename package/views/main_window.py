import sys
from datetime import date, timedelta
from enum import Enum
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView
from package.ui.ui_mainwindow import Ui_MainWindow
from package.views.login import LoginDialog
from package.models.login_model import Login
import package.services.invoice_service as invoice_service
from package.models.bill_model import load_bill_model
import package.models.invoice_model as invoice_model

import pdb # pdb.set_trace()

class MonthEventOptions(Enum):
    NONE = 0
    NEXT = 1
    PREVIOUS = 2
    TO_DAY = 3
    
def get_first_month_day_date(dt: date):
    return dt.replace(day = 1)

def get_previous_month(dt: date):
    return get_first_month_day_date(dt) - timedelta(days = 5)

def get_next_month(dt: date):
    return get_first_month_day_date(dt) + timedelta(days = 35)

class MainWindow(QMainWindow):
   
    def __init__(self):   
        super(MainWindow, self).__init__()
        self.current_login = Login()
        self.initialize_ui()
        self.date = date.today()
    
    def initialize_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_slots()
    
    def connect_slots(self):
        self.ui.next_month_pushButton.clicked.connect(self.next_month_pushButton_clicked)
        self.ui.previous_month_pushButton.clicked.connect(self.previous_month_pushButton_clicked)
        self.ui.current_month_label_pushButton.clicked.connect(self.current_month_label_pushButton_clicked)
        self.ui.bills_listView.clicked.connect(self.bills_listView_clicked)
        
    def show(self)->None:
        QMainWindow.show(self)
        self.authenticate()
        self.select_current_month()
        self.load_bills()
        
    def load_invoice_data(self):
        self.load_invoices()
        self.load_invoice_totals()
    
    def load_invoices(self):
        result = invoice_service.search_invoices_by_ref(self.current_login.user_token, self.date.year,self.date.month)
        if result.success:
            invoice_source = invoice_model.InvoiceModel(result.json())
            self.ui.mainTableView.setModel(invoice_source)
            date_delegate = invoice_model.DateDelegate(self.ui.mainTableView)
            currency_delegate = invoice_model.CurrencyDelegate(self.ui.mainTableView)
            
            self.ui.mainTableView.setItemDelegateForColumn(4, currency_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(6, date_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(7, date_delegate)
            self.ui.mainTableView.setItemDelegateForColumn(8, date_delegate)
    
    def load_invoice_totals(self):
        result = invoice_service.search_invoices_totals_by_ref(self.current_login.user_token, self.date.year,self.date.month)
        if result.success:
            self.ui.messageTotal_value_label.setText('R$ {:,.2f}'.format(result.json()['total']))
            self.ui.messageToPay_value_label.setText('R$ {:,.2f}'.format(result.json()['to_pay']))
            self.ui.messagePaid_value_label.setText('R$ {:,.2f}'.format(result.json()['paid']))
            self.ui.messageScheduled_value_label.setText('R$ {:,.2f}'.format(result.json()['scheduled']))
            self.ui.messageOpen_value_label.setText('R$ {:,.2f}'.format(result.json()['pending']))
    
    def load_bills(self):
        self.bills_Model = load_bill_model(self.current_login.user_token)
        self.ui.bills_listView.setModel(self.bills_Model)
    
    def load_bill_invoices_TableView(self, bill_id:int):
        model = invoice_model.invoice_model_from_bill_id(self.current_login.user_token, bill_id)
        self.ui.bill_invoices_TableView.setModel(model)
        #self.ui.bill_invoices_TableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if model != None:
            self.load_bill_invoices_totals(model.data_table)
    
    def load_bill_invoices_totals(self, data_table):
        paid_invoices = [invoice for invoice in data_table if invoice['pay_day'] != None and date.fromisoformat(invoice['pay_day']) < date.today()]
        len_invoices = len(paid_invoices)
        if len_invoices > 0:
            paid = sum(invoice['value'] for invoice in paid_invoices )
            self.ui.bill_totals_Total_value_label.setText('R$ {:,.2f}'.format(paid))
        
            if len_invoices >= 3:
                indexes = [len_invoices-1, len_invoices-2, len_invoices-3]
                last_payments = [paid_invoices[index] for index in indexes]
                total_last_payments = sum(invoice['value'] for invoice in last_payments )
                if total_last_payments > 0:
                    avg = total_last_payments / 3
                    self.ui.bill_totals_Avg_value_label.setText('R$ {:,.2f}'.format(avg))
            #pdb.set_trace()
            last_payment = paid_invoices[len_invoices-1]
            self.ui.bill_totals_LastPayment_value_label.setText('R$ {:,.2f}'.format(last_payment['value']))
    
    def clear_invoices_totals(self):
        self.ui.bill_totals_Avg_value_label.setText(None)
        self.ui.bill_totals_Total_value_label.setText(None)
        self.ui.bill_totals_LastPayment_value_label.setText(None)
        
    def authenticate(self):
       login = LoginDialog(self.current_login)
       login_result = login.exec_()
       if login_result:
           print('MainWindow: Authenticated')
       else:
           print(f"login result {login_result}")
           self.close()
    
    def select_current_month(self, month_option: MonthEventOptions = MonthEventOptions.NONE ):
        if month_option == MonthEventOptions.NEXT:
            self.date = get_next_month(self.date)
        elif month_option == MonthEventOptions.PREVIOUS:
            self.date = get_previous_month(self.date)
        elif month_option == MonthEventOptions.TO_DAY:
            self.date = date.today()
        
        self.ui.current_month_label_pushButton.setText('{:%B - %Y}'.format(self.date))
        self.ui.next_month_pushButton.setText('{:%B - %Y}'.format(get_next_month(self.date)))
        self.ui.previous_month_pushButton.setText('{:%B - %Y}'.format(get_previous_month(self.date)))
        
        self.load_invoice_data()    

    def next_month_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.NEXT)
        
    def previous_month_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.PREVIOUS)
        
    def current_month_label_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.TO_DAY)
    
    def bills_listView_clicked(self, index):
        self.clear_invoices_totals()
        selected_bill = self.bills_Model.get_bill(index)
        self.load_bill_invoices_TableView(selected_bill['id'])
        
