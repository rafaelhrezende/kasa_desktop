from datetime import datetime
from PySide6.QtWidgets import QDialog
from package.ui.ui_invoice_detail_form import Ui_Dialog
from package.models.invoice_model import INVOICE_METHODS , save_invoice
from package.views.base_view import BaseFormDialog, _permission_error_handler

class InvoiceDetailForm(BaseFormDialog):
    def __init__(self, model, invoice, invoice_detail = None):
        super(InvoiceDetailForm, self).__init__(Ui_Dialog())
        self.invoice = invoice
        self.invoice_detail = invoice_detail
        self.model = model
        
        self.load_inputs()
    
    def connect_slots(self):
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
     
    def load_inputs(self):
        if self.invoice_detail == None:
            return 
        self.set_description(self.invoice_detail.description)
        self.set_value(self.invoice_detail.value)
        self.set_date(self.invoice_detail.date)
        self.set_locale_description(self.invoice_detail.locale_description)
        
    
    def save_pushButton_clicked(self):
        result = self.model.add_item(self.get_invoice_id(), self.get_description(), self.get_value(), self.get_date(), self.get_locale_description(),  self.get_invoice_detail_id())
        if result.status:
             QDialog.accept(self)
        else:
            self.show_error_message('Falha ao tentar salvar o registro!', 'Não foi possível salvar o registro, verifique os campos informados e tente novamente.')
        
    def get_invoice_id(self):
        return self.invoice.id
    
    def get_description(self):
        return self.ui.desc_lineEdit.text()
    
    def set_description(self, value:str):
        self.ui.desc_lineEdit.setText(value)
    
    def get_value(self):
        return self.ui.value_lineEdit.text()
    
    def set_value(self, value):
        self.ui.value_lineEdit.setText(str(value))
    
    def get_date(self):
        return self.ui.date_lineEdit.text()
    
    def set_date(self, value):
        if value == None:
            return
        
        self.ui.date_lineEdit.setText(value.strftime('%d/%m/%Y'))
    
    def get_locale_description(self):
        return self.ui.localidade_lineEdit.text()
    
    def set_locale_description(self, value:str):
        self.ui.localidade_lineEdit.setText(value)
    
    def get_invoice_detail_id(self):
        if self.invoice_detail != None:
            return self.invoice_detail.id
        
