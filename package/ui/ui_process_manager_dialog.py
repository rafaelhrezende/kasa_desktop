# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_manager_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_ProcessManager(object):
    def setupUi(self, ProcessManager):
        if not ProcessManager.objectName():
            ProcessManager.setObjectName(u"ProcessManager")
        ProcessManager.resize(1000, 745)
        ProcessManager.setMinimumSize(QSize(619, 469))
        ProcessManager.setMaximumSize(QSize(1000, 1000))
        self.tabWidget = QTabWidget(ProcessManager)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 20, 961, 701))
        self.new_process_tab = QWidget()
        self.new_process_tab.setObjectName(u"new_process_tab")
        self.verticalLayoutWidget = QWidget(self.new_process_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 217, 309))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.process_verticalLayout = QVBoxLayout()
        self.process_verticalLayout.setObjectName(u"process_verticalLayout")
        self.header_title_label = QLabel(self.verticalLayoutWidget)
        self.header_title_label.setObjectName(u"header_title_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.header_title_label.setFont(font)
        self.header_title_label.setAlignment(Qt.AlignCenter)

        self.process_verticalLayout.addWidget(self.header_title_label)

        self.process_label = QLabel(self.verticalLayoutWidget)
        self.process_label.setObjectName(u"process_label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.process_label.setFont(font1)
        self.process_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.process_verticalLayout.addWidget(self.process_label)

        self.process_comboBox = QComboBox(self.verticalLayoutWidget)
        self.process_comboBox.setObjectName(u"process_comboBox")
        font2 = QFont()
        font2.setPointSize(12)
        self.process_comboBox.setFont(font2)
        self.process_comboBox.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.process_verticalLayout.addWidget(self.process_comboBox)


        self.verticalLayout.addLayout(self.process_verticalLayout)

        self.reference_verticalLayout = QVBoxLayout()
        self.reference_verticalLayout.setObjectName(u"reference_verticalLayout")
        self.ref_title_label = QLabel(self.verticalLayoutWidget)
        self.ref_title_label.setObjectName(u"ref_title_label")
        self.ref_title_label.setFont(font1)
        self.ref_title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.reference_verticalLayout.addWidget(self.ref_title_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.year_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.year_spinBox.setObjectName(u"year_spinBox")
        self.year_spinBox.setFont(font2)
        self.year_spinBox.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.year_spinBox.setMinimum(1900)
        self.year_spinBox.setMaximum(3000)
        self.year_spinBox.setValue(2023)

        self.horizontalLayout.addWidget(self.year_spinBox)

        self.month_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.month_spinBox.setObjectName(u"month_spinBox")
        self.month_spinBox.setFont(font2)
        self.month_spinBox.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.month_spinBox.setMinimum(1)
        self.month_spinBox.setMaximum(12)
        self.month_spinBox.setValue(5)

        self.horizontalLayout.addWidget(self.month_spinBox)


        self.reference_verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.reference_verticalLayout)

        self.method_verticalLayout = QVBoxLayout()
        self.method_verticalLayout.setObjectName(u"method_verticalLayout")
        self.method_label = QLabel(self.verticalLayoutWidget)
        self.method_label.setObjectName(u"method_label")
        self.method_label.setFont(font1)
        self.method_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.method_verticalLayout.addWidget(self.method_label)

        self.method_comboBox = QComboBox(self.verticalLayoutWidget)
        self.method_comboBox.setObjectName(u"method_comboBox")
        self.method_comboBox.setFont(font2)
        self.method_comboBox.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.method_verticalLayout.addWidget(self.method_comboBox)


        self.verticalLayout.addLayout(self.method_verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.new_process_pushButton = QPushButton(self.verticalLayoutWidget)
        self.new_process_pushButton.setObjectName(u"new_process_pushButton")

        self.verticalLayout.addWidget(self.new_process_pushButton)

        self.tabWidget.addTab(self.new_process_tab, "")
        self.process_list_tab = QWidget()
        self.process_list_tab.setObjectName(u"process_list_tab")
        self.process_tableView = QTableView(self.process_list_tab)
        self.process_tableView.setObjectName(u"process_tableView")
        self.process_tableView.setGeometry(QRect(10, 50, 931, 601))
        self.refresh_process_pushButton = QPushButton(self.process_list_tab)
        self.refresh_process_pushButton.setObjectName(u"refresh_process_pushButton")
        self.refresh_process_pushButton.setGeometry(QRect(850, 10, 88, 34))
        self.tabWidget.addTab(self.process_list_tab, "")

        self.retranslateUi(ProcessManager)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProcessManager)
    # setupUi

    def retranslateUi(self, ProcessManager):
        ProcessManager.setWindowTitle(QCoreApplication.translate("ProcessManager", u"Dialog", None))
        self.header_title_label.setText(QCoreApplication.translate("ProcessManager", u"Iniciar processo", None))
#if QT_CONFIG(tooltip)
        self.process_label.setToolTip(QCoreApplication.translate("ProcessManager", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.process_label.setText(QCoreApplication.translate("ProcessManager", u"Processo", None))
        self.process_comboBox.setProperty("model_name", QCoreApplication.translate("ProcessManager", u"method", None))
#if QT_CONFIG(tooltip)
        self.ref_title_label.setToolTip(QCoreApplication.translate("ProcessManager", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ref_title_label.setText(QCoreApplication.translate("ProcessManager", u"<html><head/><body><p align=\"center\">Ano / M\u00eas </p></body></html>", None))
        self.year_spinBox.setSuffix("")
        self.year_spinBox.setProperty("model_name", QCoreApplication.translate("ProcessManager", u"Year", None))
        self.month_spinBox.setProperty("model_name", QCoreApplication.translate("ProcessManager", u"Month", None))
#if QT_CONFIG(tooltip)
        self.method_label.setToolTip(QCoreApplication.translate("ProcessManager", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_label.setText(QCoreApplication.translate("ProcessManager", u"Forma Pagamento", None))
        self.method_comboBox.setProperty("model_name", QCoreApplication.translate("ProcessManager", u"default_method", None))
        self.new_process_pushButton.setText(QCoreApplication.translate("ProcessManager", u"Iniciar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_process_tab), QCoreApplication.translate("ProcessManager", u"Novo", None))
        self.refresh_process_pushButton.setText(QCoreApplication.translate("ProcessManager", u"Atualizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.process_list_tab), QCoreApplication.translate("ProcessManager", u"Processos", None))
    # retranslateUi

