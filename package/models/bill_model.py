from PySide6.QtCore import  QAbstractListModel, QModelIndex, Qt
from package.services import bill_service

def list_bills():
    result = bill_service.get_bills()
    if result.status:
        return result.contents
    else:
#TODO: Informar Erro ao usuarios
        return []
    

class BillModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(BillModel, self).__init__()
        self.data_source = list_bills()

    def rowCount(self, parent)->int:
        return len(self.data_source)
        
    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                __current = self.data_source[index.row()]
                return __current.to_string()
            else:
                return None
        except Exception as e:
            return None
    
    def get_bill(self, index):
        return self.data_source[index.row()]

    def reload(self):
        self.data_source = list_bills()
        self.layoutChanged.emit()
