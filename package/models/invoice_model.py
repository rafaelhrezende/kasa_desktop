from PySide6.QtCore import  QAbstractTableModel
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QStyledItemDelegate
import package.services.bill_service as bill_service
import package.services.invoice_service as invoice_service #TODO refactor to single file or search_service  

INVOICE_TABLE_COLUMNS_INDEX = ["id", "bill", "reference_year", "reference_month", "value", "method","due_date", "completion_date", "pay_day" ]
INVOICE_TABLE_COLUMNS_HEADER = ["Id.", "Conta", "Ref. Ano", "Ref. Mês", "Valor", "Método","Vencimento", "Realização", "Pagamento" ]
INVOICE_DATE_COLUMNS = ["due_date", "completion_date", "pay_day"]

#TODO - Lookup on service
INVOICE_METHODS = ['Débito Automático', 'PIX', 'Débito', 'Dinheiro']

def list_invoices_from_bill_id(token, id:int):
    request_result = bill_service.get_bill_invoices(token, id)
    if request_result.success:
        return request_result.json()

def list_invoices_from_searching(token,year, month):
    request_result = invoice_service.search_invoices_by_ref(token, year, month)
    if request_result:
        return request_result.json()

def save_invoice(token, bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, invoice_id):
    return bill_service.save_invoice(token, bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, invoice_id = invoice_id)    

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

    def reload(self, token):
        if self.bill_id != None:
            self.data_table = list_invoices_from_bill_id(token, self.bill_id)
            self.layoutChanged.emit()
        elif self.ref_year != None and self.ref_month != None:
            self.data_table = list_invoices_from_searching(token, self.ref_year, self.ref_month)
            self.layoutChanged.emit()
            
    def get_invoice(self, index):
        return self.data_table[index.row()]
    
class DateDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return value.toString() 
    
class CurrencyDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return f"R$ {value}" 

 