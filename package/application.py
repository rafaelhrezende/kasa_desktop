import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from package.views.main_window import MainWindow        
from package import local_storage 

def startup():
    initialize_resources()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    
def initialize_resources():
    local_storage.initializing_app_data()