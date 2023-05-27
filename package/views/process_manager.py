from package.ui.ui_process_manager_dialog import Ui_ProcessManager
from package.views.base_view import BaseFormDialog, PROPERTY_MODEL_NAME, _permission_error_handler
from package.models.process_model import ProcessModel, AVAILABLE_PROCESS, new_process
from package.models.invoice_model import INVOICE_METHODS

class ProcessManagerForm(BaseFormDialog):
    def __init__(self, current_login):
        self.current_login = current_login
        super(ProcessManagerForm, self).__init__(Ui_ProcessManager())
        self.ui.process_tableView.setModel(self.get_model(self.current_login.user_token))
    
    def init_ui(self):
        super().init_ui()
        self.ui.process_comboBox.addItems(AVAILABLE_PROCESS)
        self.ui.method_comboBox.addItems(INVOICE_METHODS)
    
    def get_model(self, token):
        return ProcessModel(token)
    
    def connect_slots(self):
        self.ui.refresh_process_pushButton.clicked.connect(self.refresh_process_pushButton_clicked)
        self.ui.new_process_pushButton.clicked.connect(self.new_process_pushButton_clicked)
    
    @_permission_error_handler
    def refresh_process_pushButton_clicked(self):
        self.ui.process_tableView.model().reload(self.current_login.user_token)
    
    @_permission_error_handler
    def new_process_pushButton_clicked(self):
        params = {
            self.ui.year_spinBox.property(PROPERTY_MODEL_NAME):self.ui.year_spinBox.cleanText(),
            self.ui.month_spinBox.property(PROPERTY_MODEL_NAME): self.ui.month_spinBox.cleanText(),
            self.ui.method_comboBox.property(PROPERTY_MODEL_NAME):self.ui.method_comboBox.currentText()
        }
        result = new_process(self.current_login.user_token, self.ui.process_comboBox.currentText(), params)
        if result.success:
            self.ui.process_tableView.model().reload(self.current_login.user_token)
            super().show_info_message('Processo iniciado com sucesso.')
        else:
            super().show_error_message('Falha ao tentar iniciar processo.', detail = result.message)
        #default_method
        
    
    