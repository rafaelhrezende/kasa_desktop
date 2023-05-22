from PySide6.QtCore import  QAbstractListModel, QModelIndex, Qt
from package.services import bill_service

def load_bill_model(token):
    request_result = bill_service.get_bills(token)
    if request_result.success:
        print(f'load Bill results in {len(request_result.json())} bills')
        return BillModel(request_result.json())

class BillModel(QAbstractListModel):
    def __init__(self, data, parent=None):
        super(BillModel, self).__init__()
        self.data_source = data

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
