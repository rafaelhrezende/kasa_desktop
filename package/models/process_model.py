from PySide6.QtCore import  QAbstractTableModel, Qt, QDate

import package.services.process_service as process_service
 
AVAILABLE_PROCESS = ['Create-Month-Invoices']
DEFAULT_PROCESS_TABLE_COLUMNS = ['id', 'process_key', 'observation', 'created_at', 'start_at', 'finish_at', 'status', 'user']
DEFAULT_PROCESS_TABLE_COLUMNS_HEADERS = ['Id.', 'Processo', 'Observações', 'Criação', 'Início', 'Término', 'Situação', 'Usuário'] 
DATE_COLUMNS = ['created_at', 'start_at', 'finish_at']

def list_processes(token):
    request_result = process_service.get_processes(token)
    if request_result.success:
        return request_result.json()

def new_process(token, process_key, params):
    return process_service.new_process(token, process_key, params)

class ProcessModel(QAbstractTableModel):
    def __init__(self, token):
        super(ProcessModel, self).__init__()
        self.table_columns_index = DEFAULT_PROCESS_TABLE_COLUMNS
        self.table_columns_header = DEFAULT_PROCESS_TABLE_COLUMNS_HEADERS
        self.load(token)
        
    def rowCount(self, parent)->int:
        if self.data_source is None:
            return 0
        return len(self.data_source)
    
    def columnCount(self, parent)->int:
        return len(self.table_columns_index)
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.table_columns_header[section]
        return None

    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                column_name = self.table_columns_index[index.column()]
                if column_name == 'user':
                    return self.data_source[index.row()]['user']['email']
                if column_name in DATE_COLUMNS:
                    date_value = self.data_source[index.row()][self.table_columns_index[index.column()]]
                    return QDate.fromString(date_value, 'yyyy-MM-dd')
                else:
                    return self.data_source[index.row()][self.table_columns_index[index.column()]]
            else:
                return None
        except:
            return None
    
    def load(self, token):
        self.data_source = list_processes(token)
        
    def reload(self, token):
        self.load(token)
        self.layoutChanged.emit()
    
    