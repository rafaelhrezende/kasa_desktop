from datetime import datetime
from PySide6.QtWidgets import QDialog
from package.ui.ui_invoice_form import Ui_Dialog
from package.models.invoice_model import INVOICE_METHODS , save_invoice
from package.views.base_view import BaseFormDialog, _permission_error_handler

PROPERTY_MODEL_NAME = 'model_name'

class InvoiceForm(BaseFormDialog):
    def __init__(self, bill, invoice = None):
        super(InvoiceForm, self).__init__(Ui_Dialog())
        self.bill = bill
        self.invoice = invoice
        
        if invoice != None:
            self.load_widget_input()
            if self.bill is None and self.invoice.bill != None:
                self.bill = self.invoice.bill
        
        self.change_bill_title()
    
    def init_ui(self):
        super().init_ui()
        self.ui.method_comboBox.addItems(INVOICE_METHODS)
        
    def change_bill_title(self):
        self.ui.bill_title_label.setText(self.bill.to_string())
        
    def connect_slots(self):
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
    
    def invoice_id(self):
        if self.invoice is None:
            return None
        return self.invoice.id
    
    @_permission_error_handler
    def save_pushButton_clicked(self):
        result = save_invoice(self.bill.id,
                               self.ui.year_spinBox.cleanText(),
                               self.ui.month_spinBox.cleanText(),
                               self.ui.value_lineEdit.text(),
                               self.ui.method_comboBox.currentText(),
                               self.ui.due_date_lineEdit.text(),
                               self.ui.completion_lineEdit.text(),
                               self.ui.pay_day_lineEdit.text(),
                               self.invoice_id())
        if result.status:
            QDialog.accept(self)
        else:
            print(f"Invoice - save_pushButton_clicked Error. {result.contents}")
            self.show_error_message('Falha ao tentar salvar o registro', 'Verifique os campos indicados e tente novamente')           
            
    def lineEdit_text_to_service_date_format(self, widget):
        try:
            if len(widget.text()) > 2:
                input_date = datetime.strptime(widget.text(), '%d/%m/%Y')
                return input_date.strftime('%Y-%m-%d')
            return None
        except ValueError as e:
            print('invalid date format')
            self.set_error_color(widget)
            raise e
    
    def service_date_to_lineEdit_text_format(self, str_value):
        try:
            if str_value != None and len(str_value) > 2:
                input_date =  datetime.strptime(str_value, '%Y-%m-%d')
                return input_date.strftime('%d/%m/%Y')
            return None
        except ValueError as e:
            print('invalid date format')
            raise e

    def load_widget_input(self):
        self.ui.year_spinBox.setValue(self.invoice.reference_year)
        self.ui.month_spinBox.setValue(self.invoice.reference_month)
        self.ui.value_lineEdit.setText(str(self.invoice.value))
        method_index = self.ui.method_comboBox.findText(self.invoice.method)
        if method_index >= 0:
            self.ui.method_comboBox.setCurrentIndex(method_index)
        
        if self.invoice.due_date != None:
            self.ui.due_date_lineEdit.setText(self.invoice.due_date.strftime('%d/%m/%Y'))
        
        if self.invoice.completion_date != None:
            self.ui.completion_lineEdit.setText(self.invoice.completion_date.strftime('%d/%m/%Y'))
        
        if self.invoice.pay_day != None:
            self.ui.pay_day_lineEdit.setText(self.invoice.pay_day.strftime('%d/%m/%Y'))
        
            