from PySide6.QtCore import  QAbstractTableModel
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QStyledItemDelegate
import package.services.bill_service as bill_service
import package.services.invoice_service as invoice_service #TODO refactor to single file or search_service  

import pdb # pdb.set_trace()

INVOICE_TABLE_COLUMNS_INDEX = ["id", "bill", "reference_year", "reference_month", "value", "method","due_date", "completion_date", "pay_day" ]
INVOICE_TABLE_COLUMNS_HEADER = ["Id.", "Conta", "Ref. Ano", "Ref. Mês", "Valor", "Método","Vencimento", "Realização", "Pagamento" ]
INVOICE_DATE_COLUMNS = ["due_date", "completion_date", "pay_day"]

#TODO - Lookup on service
INVOICE_METHODS = ['Débito Automático', 'PIX', 'Débito', 'Dinheiro']

def list_invoices_from_bill_id(id:int):
    result = bill_service.get_bill_invoices(id)
    if result.status:
        return result.contents
    else:
        return [] 

def list_invoices_from_searching(year, month):
    result = invoice_service.search_invoices_by_ref(year, month)
    if result.status:
        return result.contents

def save_invoice(bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, invoice_id):
    return bill_service.save_invoice(bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, invoice_id = invoice_id)    

class InvoiceModel(QAbstractTableModel):
    def __init__(self, data, bill_id = None, ref_year = None, ref_month = None, parent=None):
        super(InvoiceModel, self).__init__()
        self.bill_id = bill_id
        self.ref_year = ref_year
        self.ref_month = ref_month
        self.data_table = data
        self.table_columns_index = INVOICE_TABLE_COLUMNS_INDEX.copy()
        self.table_columns_header = INVOICE_TABLE_COLUMNS_HEADER.copy()

    def rowCount(self, parent)->int:
        if self.data_table is None:
            return 0
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
                
                if column_name in INVOICE_DATE_COLUMNS:
                    return QDate(self.data_table[index.row()].get_field(column_name))
                else:
                    return self.data_table[index.row()].get_field(column_name)
            else:
                return None
        except:
            return None

    def reload(self):
        if self.bill_id != None:
            self.data_table = list_invoices_from_bill_id(self.bill_id)
            self.layoutChanged.emit()
        elif self.ref_year != None and self.ref_month != None:
            self.data_table = list_invoices_from_searching(self.ref_year, self.ref_month)
            self.layoutChanged.emit()
            
    def get_invoice(self, index):
        return self.data_table[index.row()]
    
class DateDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return value.toString() 
    
class CurrencyDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return f"R$ {value}" 

 