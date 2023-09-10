from PySide6.QtCore import  QAbstractTableModel
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QStyledItemDelegate
import package.services.bill_service as bill_service

TABLE_COLUMNS_INDEX = ["id", "description", "value", "date", "locale_description"]
TABLE_COLUMNS_HEADER = ["Id", "Descrição", "Valor R$", "Data", "Localidade"]
DATE_COLUMNS = ["date"]

class InvoiceDetailModel(QAbstractTableModel):
    def __init__(self, invoice, parent=None):
        super(InvoiceDetailModel, self).__init__()
        self.invoice = invoice
        
        self.load_data()
    
    def rowCount(self, parent)->int:
        if self.data_table is None:
            return 0
        return len(self.data_table)
    
    def columnCount(self, parent)->int:
        return len(TABLE_COLUMNS_INDEX)
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return TABLE_COLUMNS_HEADER[section]
        return None
        
    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                column_name = TABLE_COLUMNS_INDEX[index.column()]
                
                if column_name in DATE_COLUMNS:
                    return QDate(self.data_table[index.row()].get_field(column_name))
                else:
                    return self.data_table[index.row()].get_field(column_name)
            else:
                return None
        except:
            return None
    
    def get_selected(self, index):
        if index == None:
            return
        
        return self.data_table[index.row()]
    
    def load_data(self):
        self.data_table = None
        result = bill_service.get_invoice_details( self.invoice.id)
        if result.status:
            self.data_table = result.contents
        self.layoutChanged.emit()
    
    def add_item(self, invoice_id, description, value, date, locale_description,  invoice_detail_id = None):
        result = bill_service.save_invoice_detail(invoice_id, description, value, date, locale_description,  invoice_detail_id)
        self.load_data()
        return result
    
    def sum_value(self):
        if self.data_table == None:
            return 0
        
        return sum(item.value for item in self.data_table)
    
    def num_items(self):
        if self.data_table == None:
            return 0
        
        return len(self.data_table)

