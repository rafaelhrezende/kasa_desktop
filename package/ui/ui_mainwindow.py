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
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 947)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainTableView = QTableView(self.centralwidget)
        self.mainTableView.setObjectName(u"mainTableView")
        self.mainTableView.setGeometry(QRect(70, 100, 971, 621))
        self.mainTableView.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.mainTableView.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 730, 971, 136))
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
        self.messageTotal_value_label.setStyleSheet(u"color: rgb(170, 0, 0);")
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
        self.messagePaid_value_label.setStyleSheet(u"color: rgb(170, 0, 0);")
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
        self.messageToPay_value_label.setStyleSheet(u"color: rgb(170, 0, 0);")
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
        self.messageScheduled_value_label.setStyleSheet(u"color: rgb(170, 0, 0);")
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
        self.messageOpen_value_label.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.messageOpen_value_label.setAlignment(Qt.AlignCenter)

        self.messageOpen_verticalLayout.addWidget(self.messageOpen_value_label)


        self.horizontalLayout.addLayout(self.messageOpen_verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.messageTotal_title_label.setText(QCoreApplication.translate("MainWindow", u"Total to Pay", None))
        self.messageTotal_value_label.setText("")
        self.messagePaid_title_label.setText(QCoreApplication.translate("MainWindow", u"Paid", None))
        self.messagePaid_value_label.setText("")
        self.messageToPay_title_label.setText(QCoreApplication.translate("MainWindow", u"To Pay", None))
        self.messageToPay_value_label.setText("")
        self.messageScheduled_title_label.setText(QCoreApplication.translate("MainWindow", u"Scheduled", None))
        self.messageScheduled_value_label.setText("")
        self.messageOpen_title_label.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.messageOpen_value_label.setText("")
    # retranslateUi

