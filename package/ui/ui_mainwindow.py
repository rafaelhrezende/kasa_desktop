# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1900, 996)
        MainWindow.setMinimumSize(QSize(1900, 996))
        self.action_process_manager = QAction(MainWindow)
        self.action_process_manager.setObjectName(u"action_process_manager")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainTableView = QTableView(self.centralwidget)
        self.mainTableView.setObjectName(u"mainTableView")
        self.mainTableView.setGeometry(QRect(70, 110, 971, 681))
        self.mainTableView.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.mainTableView.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 800, 971, 136))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.messageTotal_verticalLayout = QVBoxLayout()
        self.messageTotal_verticalLayout.setObjectName(u"messageTotal_verticalLayout")
        self.messageTotal_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageTotal_title_label.setObjectName(u"messageTotal_title_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.messageTotal_title_label.setFont(font)
        self.messageTotal_title_label.setAlignment(Qt.AlignCenter)

        self.messageTotal_verticalLayout.addWidget(self.messageTotal_title_label)

        self.messageTotal_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageTotal_value_label.setObjectName(u"messageTotal_value_label")
        self.messageTotal_value_label.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(True)
        self.messageTotal_value_label.setFont(font1)
        self.messageTotal_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageTotal_value_label.setAlignment(Qt.AlignCenter)

        self.messageTotal_verticalLayout.addWidget(self.messageTotal_value_label)


        self.horizontalLayout.addLayout(self.messageTotal_verticalLayout)

        self.line_2 = QFrame(self.horizontalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.messagePaid_verticalLayout = QVBoxLayout()
        self.messagePaid_verticalLayout.setObjectName(u"messagePaid_verticalLayout")
        self.messagePaid_title_label = QLabel(self.horizontalLayoutWidget)
        self.messagePaid_title_label.setObjectName(u"messagePaid_title_label")
        self.messagePaid_title_label.setFont(font)
        self.messagePaid_title_label.setAlignment(Qt.AlignCenter)

        self.messagePaid_verticalLayout.addWidget(self.messagePaid_title_label)

        self.messagePaid_value_label = QLabel(self.horizontalLayoutWidget)
        self.messagePaid_value_label.setObjectName(u"messagePaid_value_label")
        self.messagePaid_value_label.setEnabled(True)
        self.messagePaid_value_label.setFont(font1)
        self.messagePaid_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messagePaid_value_label.setAlignment(Qt.AlignCenter)

        self.messagePaid_verticalLayout.addWidget(self.messagePaid_value_label)


        self.horizontalLayout.addLayout(self.messagePaid_verticalLayout)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.messageToPay_verticalLayout = QVBoxLayout()
        self.messageToPay_verticalLayout.setObjectName(u"messageToPay_verticalLayout")
        self.messageToPay_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageToPay_title_label.setObjectName(u"messageToPay_title_label")
        self.messageToPay_title_label.setFont(font)
        self.messageToPay_title_label.setAlignment(Qt.AlignCenter)

        self.messageToPay_verticalLayout.addWidget(self.messageToPay_title_label)

        self.messageToPay_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageToPay_value_label.setObjectName(u"messageToPay_value_label")
        self.messageToPay_value_label.setEnabled(True)
        self.messageToPay_value_label.setFont(font1)
        self.messageToPay_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageToPay_value_label.setAlignment(Qt.AlignCenter)

        self.messageToPay_verticalLayout.addWidget(self.messageToPay_value_label)


        self.horizontalLayout.addLayout(self.messageToPay_verticalLayout)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.messageScheduled_verticalLayout = QVBoxLayout()
        self.messageScheduled_verticalLayout.setObjectName(u"messageScheduled_verticalLayout")
        self.messageScheduled_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageScheduled_title_label.setObjectName(u"messageScheduled_title_label")
        self.messageScheduled_title_label.setFont(font)
        self.messageScheduled_title_label.setAlignment(Qt.AlignCenter)

        self.messageScheduled_verticalLayout.addWidget(self.messageScheduled_title_label)

        self.messageScheduled_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageScheduled_value_label.setObjectName(u"messageScheduled_value_label")
        self.messageScheduled_value_label.setEnabled(True)
        self.messageScheduled_value_label.setFont(font1)
        self.messageScheduled_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageScheduled_value_label.setAlignment(Qt.AlignCenter)

        self.messageScheduled_verticalLayout.addWidget(self.messageScheduled_value_label)


        self.horizontalLayout.addLayout(self.messageScheduled_verticalLayout)

        self.line_4 = QFrame(self.horizontalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.messageOpen_verticalLayout = QVBoxLayout()
        self.messageOpen_verticalLayout.setObjectName(u"messageOpen_verticalLayout")
        self.messageOpen_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageOpen_title_label.setObjectName(u"messageOpen_title_label")
        self.messageOpen_title_label.setFont(font)
        self.messageOpen_title_label.setAlignment(Qt.AlignCenter)

        self.messageOpen_verticalLayout.addWidget(self.messageOpen_title_label)

        self.messageOpen_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageOpen_value_label.setObjectName(u"messageOpen_value_label")
        self.messageOpen_value_label.setEnabled(True)
        self.messageOpen_value_label.setFont(font1)
        self.messageOpen_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageOpen_value_label.setAlignment(Qt.AlignCenter)

        self.messageOpen_verticalLayout.addWidget(self.messageOpen_value_label)


        self.horizontalLayout.addLayout(self.messageOpen_verticalLayout)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(70, 40, 971, 51))
        self.header_horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.header_horizontalLayout.setObjectName(u"header_horizontalLayout")
        self.header_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_month_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.previous_month_pushButton.setObjectName(u"previous_month_pushButton")
        self.previous_month_pushButton.setFont(font)

        self.header_horizontalLayout.addWidget(self.previous_month_pushButton)

        self.current_month_label_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.current_month_label_pushButton.setObjectName(u"current_month_label_pushButton")
        self.current_month_label_pushButton.setFont(font)
        self.current_month_label_pushButton.setFlat(True)

        self.header_horizontalLayout.addWidget(self.current_month_label_pushButton)

        self.next_month_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.next_month_pushButton.setObjectName(u"next_month_pushButton")
        self.next_month_pushButton.setFont(font)

        self.header_horizontalLayout.addWidget(self.next_month_pushButton)

        self.header_invoices_label = QLabel(self.centralwidget)
        self.header_invoices_label.setObjectName(u"header_invoices_label")
        self.header_invoices_label.setGeometry(QRect(430, 0, 238, 41))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(True)
        self.header_invoices_label.setFont(font2)
        self.bills_listView = QListView(self.centralwidget)
        self.bills_listView.setObjectName(u"bills_listView")
        self.bills_listView.setGeometry(QRect(1130, 140, 471, 511))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(True)
        self.bills_listView.setFont(font3)
        self.header_bills_label = QLabel(self.centralwidget)
        self.header_bills_label.setObjectName(u"header_bills_label")
        self.header_bills_label.setGeometry(QRect(1130, 30, 471, 51))
        self.header_bills_label.setFont(font2)
        self.header_bills_label.setAlignment(Qt.AlignCenter)
        self.bill_invoices_TableView = QTableView(self.centralwidget)
        self.bill_invoices_TableView.setObjectName(u"bill_invoices_TableView")
        self.bill_invoices_TableView.setGeometry(QRect(1130, 700, 721, 241))
        self.bill_invoices_TableView.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.bill_invoices_TableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.bill_invoices_TableView.horizontalHeader().setStretchLastSection(True)
        self.bill_invoices_TableView.verticalHeader().setDefaultSectionSize(30)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(1130, 655, 721, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.new_invoice_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.new_invoice_pushButton.setObjectName(u"new_invoice_pushButton")
        self.new_invoice_pushButton.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(12)
        self.new_invoice_pushButton.setFont(font4)

        self.horizontalLayout_3.addWidget(self.new_invoice_pushButton)

        self.edit_invoice_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.edit_invoice_pushButton.setObjectName(u"edit_invoice_pushButton")
        self.edit_invoice_pushButton.setEnabled(False)
        self.edit_invoice_pushButton.setFont(font4)

        self.horizontalLayout_3.addWidget(self.edit_invoice_pushButton)

        self.details_invoice_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.details_invoice_pushButton.setObjectName(u"details_invoice_pushButton")
        self.details_invoice_pushButton.setEnabled(True)
        self.details_invoice_pushButton.setFont(font4)

        self.horizontalLayout_3.addWidget(self.details_invoice_pushButton)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(1130, 90, 471, 45))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.new_bill_pushButton = QPushButton(self.horizontalLayoutWidget_5)
        self.new_bill_pushButton.setObjectName(u"new_bill_pushButton")
        self.new_bill_pushButton.setEnabled(True)
        self.new_bill_pushButton.setFont(font4)

        self.horizontalLayout_4.addWidget(self.new_bill_pushButton)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1650, 220, 202, 311))
        self.bill_totals_verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.bill_totals_verticalLayout.setObjectName(u"bill_totals_verticalLayout")
        self.bill_totals_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bill_totals_Total_verticalLayout = QVBoxLayout()
        self.bill_totals_Total_verticalLayout.setObjectName(u"bill_totals_Total_verticalLayout")
        self.bill_totals_Total_title_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_Total_title_label.setObjectName(u"bill_totals_Total_title_label")
        self.bill_totals_Total_title_label.setFont(font)
        self.bill_totals_Total_title_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_Total_verticalLayout.addWidget(self.bill_totals_Total_title_label)

        self.bill_totals_Total_value_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_Total_value_label.setObjectName(u"bill_totals_Total_value_label")
        self.bill_totals_Total_value_label.setEnabled(True)
        self.bill_totals_Total_value_label.setFont(font1)
        self.bill_totals_Total_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.bill_totals_Total_value_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_Total_verticalLayout.addWidget(self.bill_totals_Total_value_label)


        self.bill_totals_verticalLayout.addLayout(self.bill_totals_Total_verticalLayout)

        self.line_5 = QFrame(self.verticalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.bill_totals_verticalLayout.addWidget(self.line_5)

        self.bill_totals_Avg_verticalLayout = QVBoxLayout()
        self.bill_totals_Avg_verticalLayout.setObjectName(u"bill_totals_Avg_verticalLayout")
        self.bill_totals_Avg_title_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_Avg_title_label.setObjectName(u"bill_totals_Avg_title_label")
        self.bill_totals_Avg_title_label.setFont(font)
        self.bill_totals_Avg_title_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_Avg_verticalLayout.addWidget(self.bill_totals_Avg_title_label)

        self.bill_totals_Avg_value_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_Avg_value_label.setObjectName(u"bill_totals_Avg_value_label")
        self.bill_totals_Avg_value_label.setEnabled(True)
        self.bill_totals_Avg_value_label.setFont(font1)
        self.bill_totals_Avg_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.bill_totals_Avg_value_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_Avg_verticalLayout.addWidget(self.bill_totals_Avg_value_label)


        self.bill_totals_verticalLayout.addLayout(self.bill_totals_Avg_verticalLayout)

        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.bill_totals_verticalLayout.addWidget(self.line_6)

        self.bill_totals_LastPayment_verticalLayout = QVBoxLayout()
        self.bill_totals_LastPayment_verticalLayout.setObjectName(u"bill_totals_LastPayment_verticalLayout")
        self.bill_totals_LastPayment_title_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_LastPayment_title_label.setObjectName(u"bill_totals_LastPayment_title_label")
        self.bill_totals_LastPayment_title_label.setFont(font)
        self.bill_totals_LastPayment_title_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_LastPayment_verticalLayout.addWidget(self.bill_totals_LastPayment_title_label)

        self.bill_totals_LastPayment_value_label = QLabel(self.verticalLayoutWidget)
        self.bill_totals_LastPayment_value_label.setObjectName(u"bill_totals_LastPayment_value_label")
        self.bill_totals_LastPayment_value_label.setEnabled(True)
        self.bill_totals_LastPayment_value_label.setFont(font1)
        self.bill_totals_LastPayment_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.bill_totals_LastPayment_value_label.setAlignment(Qt.AlignCenter)

        self.bill_totals_LastPayment_verticalLayout.addWidget(self.bill_totals_LastPayment_value_label)


        self.bill_totals_verticalLayout.addLayout(self.bill_totals_LastPayment_verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1900, 30))
        self.menuProcessos = QMenu(self.menubar)
        self.menuProcessos.setObjectName(u"menuProcessos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProcessos.menuAction())
        self.menuProcessos.addAction(self.action_process_manager)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_process_manager.setText(QCoreApplication.translate("MainWindow", u"Gerenciador de Processos", None))
#if QT_CONFIG(tooltip)
        self.messageTotal_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageTotal_title_label.setText(QCoreApplication.translate("MainWindow", u"Total do M\u00eas", None))
        self.messageTotal_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messagePaid_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of paid invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messagePaid_title_label.setText(QCoreApplication.translate("MainWindow", u"Pago", None))
        self.messagePaid_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messageToPay_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of not paid invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageToPay_title_label.setText(QCoreApplication.translate("MainWindow", u"A pagar", None))
        self.messageToPay_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messageScheduled_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of scheduled invoice's values.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageScheduled_title_label.setText(QCoreApplication.translate("MainWindow", u"Agendado", None))
        self.messageScheduled_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messageOpen_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of invoices that are not scheduled to pay.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageOpen_title_label.setText(QCoreApplication.translate("MainWindow", u"Pendente", None))
        self.messageOpen_value_label.setText("")
        self.previous_month_pushButton.setText(QCoreApplication.translate("MainWindow", u"Abril", None))
        self.current_month_label_pushButton.setText(QCoreApplication.translate("MainWindow", u"Maio", None))
        self.next_month_pushButton.setText(QCoreApplication.translate("MainWindow", u"Junho", None))
        self.header_invoices_label.setText(QCoreApplication.translate("MainWindow", u"Cobran\u00e7as M\u00eas", None))
        self.header_bills_label.setText(QCoreApplication.translate("MainWindow", u"Contas", None))
#if QT_CONFIG(tooltip)
        self.new_invoice_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.new_invoice_pushButton.setText(QCoreApplication.translate("MainWindow", u"Nova Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.edit_invoice_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.edit_invoice_pushButton.setText(QCoreApplication.translate("MainWindow", u"Editar Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.details_invoice_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.details_invoice_pushButton.setText(QCoreApplication.translate("MainWindow", u"Visualizar Detalhes", None))
#if QT_CONFIG(tooltip)
        self.new_bill_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.new_bill_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Nova Conta", None))
#if QT_CONFIG(tooltip)
        self.bill_totals_Total_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bill_totals_Total_title_label.setText(QCoreApplication.translate("MainWindow", u"Total Pago", None))
        self.bill_totals_Total_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.bill_totals_Avg_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bill_totals_Avg_title_label.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia \u00falt. 3", None))
        self.bill_totals_Avg_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.bill_totals_LastPayment_title_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bill_totals_LastPayment_title_label.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo Pagamento", None))
        self.bill_totals_LastPayment_value_label.setText("")
        self.menuProcessos.setTitle(QCoreApplication.translate("MainWindow", u"Processos", None))
    # retranslateUi

