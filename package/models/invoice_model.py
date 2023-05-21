from PySide6.QtCore import  QAbstractTableModel
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QStyledItemDelegate

#import pdb 
#pdb.set_trace()

from sqlalchemy.sql.expression import column

INVOICE_TABLE_COLUMNS_INDEX = ["id", "bill", "reference_year", "reference_month", "value", "method","due_date", "completion_date", "pay_day" ]
INVOICE_TABLE_COLUMNS_HEADER = ["Id", "Bill", "Year", "Month", "Value", "Method","Due", "Completion", "Payment" ]
INVOICE_DATE_COLUMNS = ["due_date", "completion_date", "pay_day"]

class InvoiceModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(InvoiceModel, self).__init__()
        self.data_table = data

    def rowCount(self, parent)->int:
        return len(self.data_table)
    
    def columnCount(self, parent)->int:
        return len(INVOICE_TABLE_COLUMNS_INDEX)
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return INVOICE_TABLE_COLUMNS_HEADER[section]
        return None
        
    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                column_name = INVOICE_TABLE_COLUMNS_INDEX[index.column()]
                if column_name == 'bill':
                    return self.data_table[index.row()]['bill']['title']
                if column_name in INVOICE_DATE_COLUMNS:
                    date_value = self.data_table[index.row()][INVOICE_TABLE_COLUMNS_INDEX[index.column()]]
                    return QDate.fromString(date_value, 'yyyy-MM-dd')
                else:
                    return self.data_table[index.row()][INVOICE_TABLE_COLUMNS_INDEX[index.column()]]
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
    