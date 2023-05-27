from PySide6.QtCore import  QAbstractListModel, QModelIndex, Qt
from package.services import bill_service

def list_bills(token):
    request_result = bill_service.get_bills(token)
    if request_result.success:
        return request_result.json()
    else: #TODO Inform User
        print("loading bill fails")

class BillModel(QAbstractListModel):
    def __init__(self, current_login, parent=None):
        super(BillModel, self).__init__()
        self.current_login = current_login
        self.data_source = list_bills(self.current_login.user_token)

    def rowCount(self, parent)->int:
        return len(self.data_source)
        
    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                __current = self.data_source[index.row()]
                return f"{__current['id']} - {__current['title']}: R$ {__current['initial_value']}"
            else:
                return None
        except Exception as e:
            return None
    
    def get_bill(self, index):
        return self.data_source[index.row()]

    def reload(self):
        self.data_source = list_bills(self.current_login.user_token)
        self.layoutChanged.emit()
