from datetime import datetime
from PySide6.QtWidgets import QDialog
from package.ui.ui_invoice_details import Ui_Dialog
from package.views.base_view import BaseFormDialog, _permission_error_handler
from package.views.invoice_detail_form import InvoiceDetailForm
from package.models.invoice_detail_model import InvoiceDetailModel
from package.models.models_delegates import CurrencyDelegate

class InvoiceDetails(BaseFormDialog):
    def __init__(self, invoice, bill_title):
        super(InvoiceDetails, self).__init__(Ui_Dialog())
        self.invoice = invoice
        self.bill_title = bill_title
        self.set_model()
        self.update_labels()
        
    def set_model(self):
        self.model = InvoiceDetailModel(self.invoice)
        self.ui.mainTableView.setModel(self.model)
        currency_delegate = CurrencyDelegate(self.ui.mainTableView)
        
        self.ui.mainTableView.setItemDelegateForColumn(2, currency_delegate)
        
        self.model.layoutChanged.connect(self.model_layoutChanged)
        self.model_layoutChanged()
    
    def model_layoutChanged(self):
        self.set_totals()
        
    def update_labels(self):
        self.ui.messageConta_value_label.setText(self.bill_title)
        self.ui.messageReference_value_label.setText(f"{self.invoice.reference_year}/{self.invoice.reference_month}")
        self.ui.messageTotal_value_label.setText(f"{self.invoice.value}")
        
    def connect_slots(self):
        self.ui.new_pushButton.clicked.connect(self.new_pushButton_clicked)
        self.ui.mainTableView.doubleClicked.connect(self.mainTableView_doubleClicked)
        
    # Events
    def  new_pushButton_clicked(self):
        InvoiceDetailForm(self.model, self.invoice).exec()    
    
    def mainTableView_doubleClicked(self, index):
        selected_item = self.ui.mainTableView.model().get_selected(index)
        InvoiceDetailForm(self.model, self.invoice, selected_item).exec()
    
    def set_totals(self):
        self.ui.somaItens_value_label.setText('R$ {:,.2f}'.format(self.model.sum_value()))
        self.ui.quantidadeItens_value_label.setText(str(self.model.num_items()))

    