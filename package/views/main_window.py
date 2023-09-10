import sys
from datetime import date, timedelta
from enum import Enum
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView
from package.ui.ui_mainwindow import Ui_MainWindow
import package.views.base_view as base_view
from package.views.invoice import InvoiceForm
from package.views.bill import BillForm
from package.views.process_manager import ProcessManagerForm
from package.views.invoice_details import InvoiceDetails
import package.services.invoice_service as invoice_service
from package.models.bill_model import BillModel
import package.models.invoice_model as invoice_model

import pdb

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
        self.ui.bills_listView.doubleClicked.connect(self.bills_listView_doubleClicked)
        self.ui.new_invoice_pushButton.clicked.connect(self.new_invoice_pushButton_clicked)
        self.ui.new_bill_pushButton.clicked.connect(self.new_bill_pushButton_clicked)
        self.ui.bill_invoices_TableView.doubleClicked.connect(self.bill_invoices_TableView_doubleClicked)
        self.ui.mainTableView.doubleClicked.connect(self.mainTableView_doubleClicked)
        self.ui.action_process_manager.triggered.connect(self.action_process_manager_triggered) 
        self.ui.details_invoice_pushButton.clicked.connect(self.details_invoice_pushButton_clicked)
        
    def show(self)->None:
        QMainWindow.show(self)
        self.select_current_month()
        self.load_bills()
    
    def _permission_error_handler(fnc):
        def handler( self, *args, **kwargs ):
            try:
                fnc(self, *args, **kwargs)
            except PermissionError:
                self.authenticate()
        return handler
    
    def load_invoice_data(self):
        self.load_invoices()
        self.load_invoice_totals()
    
    @_permission_error_handler
    def load_invoices(self):
        invoice_list = invoice_model.list_invoices_from_searching(self.date.year, self.date.month)
        main_table_invoice_model = invoice_model.InvoiceModel(invoice_list, ref_year = self.date.year, ref_month = self.date.month )
        self.ui.mainTableView.setModel(main_table_invoice_model)
        date_delegate = invoice_model.DateDelegate(self.ui.mainTableView)
        currency_delegate = invoice_model.CurrencyDelegate(self.ui.mainTableView)
        
        self.ui.mainTableView.setItemDelegateForColumn(4, currency_delegate)
        self.ui.mainTableView.setItemDelegateForColumn(6, date_delegate)
        self.ui.mainTableView.setItemDelegateForColumn(7, date_delegate)
        self.ui.mainTableView.setItemDelegateForColumn(8, date_delegate)
    
    @_permission_error_handler
    def load_invoice_totals(self):
        result = invoice_service.search_invoices_totals_by_ref(self.date.year,self.date.month)
        if result.status:
            self.ui.messageTotal_value_label.setText('R$ {:,.2f}'.format(result.contents['total']))
            self.ui.messageToPay_value_label.setText('R$ {:,.2f}'.format(result.contents['to_pay']))
            self.ui.messagePaid_value_label.setText('R$ {:,.2f}'.format(result.contents['paid']))
            self.ui.messageScheduled_value_label.setText('R$ {:,.2f}'.format(result.contents['scheduled']))
            self.ui.messageOpen_value_label.setText('R$ {:,.2f}'.format(result.contents['pending']))
    
    @_permission_error_handler
    def load_bills(self):
        self.ui.bills_listView.setModel(BillModel())
    
    @_permission_error_handler
    def load_bill_invoices_TableView(self, bill_id:int):
        invoice_list = invoice_model.list_invoices_from_bill_id(bill_id)
        
        model = invoice_model.InvoiceModel(invoice_list, bill_id = bill_id)
        model.table_columns_index.remove('bill')
        model.table_columns_header.remove('Conta')
        model.table_columns_index.remove('completion_date')
        model.table_columns_header.remove('Realização')
        self.ui.bill_invoices_TableView.setModel(model)

        currency_delegate = invoice_model.CurrencyDelegate(self.ui.bill_invoices_TableView)
        self.ui.bill_invoices_TableView.setItemDelegateForColumn(3, currency_delegate)

        if model != None and model.data_table != None:
            self.load_bill_invoices_totals()
    
    @_permission_error_handler
    def load_bill_invoices_totals(self):
        if self.ui.bill_invoices_TableView.model() != None and self.ui.bill_invoices_TableView.model().data_table != None:
            paid_invoices = [invoice for invoice in self.ui.bill_invoices_TableView.model().data_table if invoice.pay_day != None and invoice.pay_day < date.today()]
            len_invoices = len(paid_invoices)
            if len_invoices > 0:
                paid = sum(invoice.value for invoice in paid_invoices )
                self.ui.bill_totals_Total_value_label.setText('R$ {:,.2f}'.format(paid))
            
                if len_invoices >= 3:
                    indexes = [len_invoices-1, len_invoices-2, len_invoices-3]
                    last_payments = [paid_invoices[index] for index in indexes]
                    total_last_payments = sum(invoice.value for invoice in last_payments )
                    if total_last_payments > 0:
                        avg = total_last_payments / 3
                        self.ui.bill_totals_Avg_value_label.setText('R$ {:,.2f}'.format(avg))
                last_payment = paid_invoices[len_invoices-1]
                self.ui.bill_totals_LastPayment_value_label.setText('R$ {:,.2f}'.format(last_payment.value))
    
    def clear_invoices_totals(self):
        self.ui.bill_totals_Avg_value_label.setText(None)
        self.ui.bill_totals_Total_value_label.setText(None)
        self.ui.bill_totals_LastPayment_value_label.setText(None)
    
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
    
    @_permission_error_handler
    def reload_invoices_views(self):
        if self.ui.bill_invoices_TableView.model() != None:
            self.ui.bill_invoices_TableView.model().reload()
        self.ui.mainTableView.model().reload()
        self.load_bill_invoices_totals()
        self.load_invoice_totals()

    def next_month_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.NEXT)
        
    def previous_month_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.PREVIOUS)
        
    def current_month_label_pushButton_clicked(self):
        self.select_current_month(MonthEventOptions.TO_DAY)
    
    def bills_listView_clicked(self, index):
        self.clear_invoices_totals()
        selected_bill = self.ui.bills_listView.model().get_bill(index)
        self.load_bill_invoices_TableView(selected_bill.id)
    
    @_permission_error_handler
    def bills_listView_doubleClicked(self, index):
        selected_bill = self.ui.bills_listView.model().get_bill(index)
        bill_form = BillForm(selected_bill)
        if bill_form.exec():
            self.ui.bills_listView.model().reload()
    
    @_permission_error_handler
    def new_invoice_pushButton_clicked(self):
        selected_indexes = self.ui.bills_listView.selectedIndexes()
        if len(selected_indexes) > 0:
            bill = selected_indexes[0].model().get_bill(selected_indexes[0])
            invoice_form_dialog = InvoiceForm(bill)
            if invoice_form_dialog.exec():
                self.reload_invoices_views()
        else:#TODO: Organizar as mensagens e possibilitar traduções
            base_view.show_error_message("Nenhuma Conta está selecionada.","Selecione uma conta da lista para criar uma cobrança")
    
    @_permission_error_handler
    def new_bill_pushButton_clicked(self):
        bill_form = BillForm()
        if bill_form.exec():
            self.ui.bills_listView.model().reload()
 
    @_permission_error_handler
    def bill_invoices_TableView_doubleClicked(self, index):
        selected_invoice = self.ui.bill_invoices_TableView.model().get_invoice(index)
        selected_indexes = self.ui.bills_listView.selectedIndexes()
        if len(selected_indexes) > 0:
            bill = selected_indexes[0].model().get_bill(selected_indexes[0])
            invoice_form_dialog = InvoiceForm(bill, selected_invoice)
            if invoice_form_dialog.exec():
                self.reload_invoices_views()
        else:#TODO: Organizar as mensagens e possibilitar traduções
            base_view.show_error_message("Nenhuma Conta está selecionada.","Selecione uma conta da lista para criar uma cobrança")
        
    @_permission_error_handler
    def mainTableView_doubleClicked(self, index):
        selected_invoice = self.ui.mainTableView.model().get_invoice(index)
        invoice_form_dialog = InvoiceForm(None, selected_invoice)
        if invoice_form_dialog.exec():
            self.reload_invoices_views()

    def action_process_manager_triggered(self):
        ProcessManagerForm().exec()
        
    def details_invoice_pushButton_clicked(self):
        selected_invoice = self.ui.bill_invoices_TableView.selectedIndexes()
        selected_bill = self.ui.bills_listView.selectedIndexes()
        if selected_invoice != [] and  selected_bill != []:
            invoice = self.ui.bill_invoices_TableView.model().get_invoice(selected_invoice[0])
            bill = self.ui.bills_listView.model().get_bill(selected_bill[0])
            invoice_detail_form = InvoiceDetails(invoice, bill.title)
            invoice_detail_form.exec()
        