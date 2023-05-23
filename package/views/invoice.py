from datetime import datetime
from PySide6.QtWidgets import QDialog
from package.ui.ui_invoice_form import Ui_Dialog
from package.models.invoice_model import INVOICE_METHODS , create_invoice
from package.views.base_view import BaseFormDialog
PROPERTY_MODEL_NAME = 'model_name'

def exec_invoice_form_dialog(current_login, bill):
    form = InvoiceForm(current_login, bill['id'])
    form.ui.bill_title_label.setText(f"{bill['id']} - {bill['title']}")
    return form.exec() 
    
class InvoiceForm(BaseFormDialog):
    def __init__(self, current_login, bill_id):
        super(InvoiceForm, self).__init__(Ui_Dialog())
        self.current_login = current_login
        self.bill_id = bill_id
    
    def init_ui(self):
        super().init_ui()
        self.ui.method_comboBox.addItems(INVOICE_METHODS)
    
    def connect_slots(self):
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
    
    def save_pushButton_clicked(self):
        result = create_invoice(self.current_login.user_token, 
                       self.bill_id,
                       self.ui.year_spinBox.cleanText(),
                       self.ui.month_spinBox.cleanText(),
                       self.ui.value_lineEdit.text(),
                       self.ui.method_comboBox.currentText(),
                       self.get_lineEdit_text_date(self.ui.due_date_lineEdit),
                       self.get_lineEdit_text_date(self.ui.completion_lineEdit),
                       self.get_lineEdit_text_date(self.ui.pay_day_lineEdit))
        if result.success:
            QDialog.accept(self)
        else: # TODO: exibir mensagem de erro
            print(f'Fail to Create Invoice: {result.message}')
                        
            #TODO Remove validation - check status code on service and raise 
            if result.json()['detail'].__class__ == str:
                print("NOT IMPLEMENTED")
            else:
                errors_loc = [error['loc'][2] for error in result.json()['detail']]
                self.validate_widget_invalid(errors_loc)
        
    def get_lineEdit_text_date(self, widget):
        try:
            if len(widget.text()) > 2:
                input_date = datetime.strptime(widget.text(), '%d/%m/%Y')
                return input_date.strftime('%Y-%m-%d')
            return None
        except ValueError as e:
            print('invalid date format')
            self.set_error_color(widget)
            raise e
            