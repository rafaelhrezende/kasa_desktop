from PySide6.QtCore import  QAbstractTableModel
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QStyledItemDelegate
from package.services.bill_service import get_bill_invoices
#import pdb 
#pdb.set_trace()

INVOICE_TABLE_COLUMNS_INDEX = ["id", "bill", "reference_year", "reference_month", "value", "method","due_date", "completion_date", "pay_day" ]
INVOICE_TABLE_COLUMNS_HEADER = ["Id.", "Conta", "Ref. Ano", "Ref. Mês", "Valor", "Método","Vencimento", "Realização", "Pagamento" ]
INVOICE_DATE_COLUMNS = ["due_date", "completion_date", "pay_day"]

def invoice_model_from_bill_id(token, id:int):
    request_result = get_bill_invoices(token, id)
    if request_result.success:
        result_model = InvoiceModel(request_result.json())
        result_model.table_columns_index.remove('bill')
        result_model.table_columns_header.remove('Conta')
        result_model.table_columns_index.remove('completion_date')
        result_model.table_columns_header.remove('Realização')
        return result_model

class InvoiceModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(InvoiceModel, self).__init__()
        self.data_table = data
        self.table_columns_index = INVOICE_TABLE_COLUMNS_INDEX.copy()
        self.table_columns_header = INVOICE_TABLE_COLUMNS_HEADER.copy()

    def rowCount(self, parent)->int:
        return len(self.data_table)
    
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
                if column_name == 'bill':
                    return self.data_table[index.row()]['bill']['title']
                if column_name in INVOICE_DATE_COLUMNS:
                    date_value = self.data_table[index.row()][self.table_columns_index[index.column()]]
                    return QDate.fromString(date_value, 'yyyy-MM-dd')
                else:
                    return self.data_table[index.row()][self.table_columns_index[index.column()]]
            else:
                return None
        except:
            return None
    
    #def setData(self, index, value, role=QtCore.Qt.EditRole):
     #   if role == QtCore.Qt.EditRole:
      #      row = index.row()
       #     column = index.column()
        #    self.table_data[row][column] = value
         #   self.dataChanged.emit(index, index)
          #  return True
        #return QtCore.QAbstractTableModel.setData(self, index, value, role)

class DateDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return value.toString() 
    
class CurrencyDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return f"R$ {value}" 
    