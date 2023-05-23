# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1900, 996)
        MainWindow.setMinimumSize(QSize(1900, 996))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainTableView = QTableView(self.centralwidget)
        self.mainTableView.setObjectName(u"mainTableView")
        self.mainTableView.setGeometry(QRect(70, 150, 971, 641))
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
        self.bills_listView.setGeometry(QRect(1220, 140, 471, 511))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(True)
        self.bills_listView.setFont(font3)
        self.header_bills_label = QLabel(self.centralwidget)
        self.header_bills_label.setObjectName(u"header_bills_label")
        self.header_bills_label.setGeometry(QRect(1310, 10, 281, 51))
        self.header_bills_label.setFont(font2)
        self.bill_invoices_TableView = QTableView(self.centralwidget)
        self.bill_invoices_TableView.setObjectName(u"bill_invoices_TableView")
        self.bill_invoices_TableView.setGeometry(QRect(1130, 700, 651, 241))
        self.bill_invoices_TableView.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.bill_invoices_TableView.horizontalHeader().setStretchLastSection(True)
        self.bill_invoices_TableView.verticalHeader().setDefaultSectionSize(30)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(70, 100, 971, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(1130, 660, 651, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.new_invoice_pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.new_invoice_pushButton.setObjectName(u"new_invoice_pushButton")
        self.new_invoice_pushButton.setEnabled(True)
        self.new_invoice_pushButton.setFont(font4)

        self.horizontalLayout_3.addWidget(self.new_invoice_pushButton)

        self.pushButton_10 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(1220, 99, 471, 45))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_8)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1694, 220, 202, 311))
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.header_bills_label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Contas", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Criar Um", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia processo de cria\u00e7\u00e3o de todas cobran\u00e7as n\u00e3o registradas no m\u00eas.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Criar Todos", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"In\u00edcia formul\u00e1rio para edi\u00e7\u00e3o da cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Remove cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
#if QT_CONFIG(tooltip)
        self.new_invoice_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.new_invoice_pushButton.setText(QCoreApplication.translate("MainWindow", u"Nova Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("MainWindow", u"In\u00edcia formul\u00e1rio para edi\u00e7\u00e3o da cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Editar Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("MainWindow", u"Remove cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Remover Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Nova Conta", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"In\u00edcia formul\u00e1rio para edi\u00e7\u00e3o da cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Remove cobran\u00e7a selecionada.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
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
    # retranslateUi

