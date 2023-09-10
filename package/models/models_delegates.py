# Delegates for QT Presentations
from PySide6.QtWidgets import QStyledItemDelegate

class CurrencyDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return f"R$ {value}" 