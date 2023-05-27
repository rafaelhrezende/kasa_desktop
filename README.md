# kasa_desktop

Desktop app cliente to work with kasa_service.

## Informations

* Uses Pyside6 and QT

## Buils QT Files
* make will compile the QT files to pyt using uic 
  > PySide6: IN my environment I need to direct to qt6 if not will create using Qt2. 
  ``` /usr/lib/qt6/uic -g python designer/mainwindow.ui > package/ui/ui_mainwindow.py```
