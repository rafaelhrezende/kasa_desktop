from PySide6.QtWidgets import QDialog
from package.ui.ui_bill_form import Ui_Dialog
import package.services.bill_service as bill_service 
from package.views.base_view import BaseFormDialog, _permission_error_handler

class BillForm(BaseFormDialog):
    def __init__(self, bill = None):
        super(BillForm, self).__init__(Ui_Dialog())
        self.bill = bill
        if self.bill != None:
            self.load_widget_input()
    
    def connect_slots(self):
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
    
    def bill_id(self):
        if self.bill is None:
            return None
        return self.bill.id
    @_permission_error_handler
    def save_pushButton_clicked(self):
        result = bill_service.saveBill(self.ui.title_lineEdit.text(),
                                        self.ui.desc_lineEdit.text(),
                                        self.ui.category_lineEdit.text(),
                                        self.ui.pay_day_spinBox.text(),
                                        self.ui.initial_value_lineEdit.text(),
                                        self.ui.activated_true_radioButton.isChecked(),
                                        self.bill_id())
        if result.status:
            QDialog.accept(self)
        else:
            print(f'Bill - save_pushButton_clicked. Error: {result.contents}')
            self.show_error_message('Falha ao tentar salvar o registro', 'Verifique os campos indicados e tente novamente')
        
    def load_widget_input(self):
        self.ui.title_lineEdit.setText(self.bill.title)
        self.ui.desc_lineEdit.setText(self.bill.description)
        self.ui.category_lineEdit.setText(self.bill.category)
        self.ui.pay_day_spinBox.setValue(self.bill.payment_day)
        self.ui.initial_value_lineEdit.setText(str(self.bill.initial_value))
        
        self.ui.activated_false_radioButton.setChecked(True)
        self.ui.activated_true_radioButton.setChecked(self.bill.is_active)
        
        