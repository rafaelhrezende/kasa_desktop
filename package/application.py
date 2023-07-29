import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from package.views.main_window import MainWindow        

def startup():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
