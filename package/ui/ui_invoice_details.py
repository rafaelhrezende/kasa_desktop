# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_details.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(775, 568)
        self.mainTableView = QTableView(Dialog)
        self.mainTableView.setObjectName(u"mainTableView")
        self.mainTableView.setGeometry(QRect(40, 220, 551, 311))
        self.mainTableView.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.mainTableView.horizontalHeader().setStretchLastSection(True)
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(130, 0, 371, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.title_label.setFont(font)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 50, 551, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.messageConta_verticalLayout = QVBoxLayout()
        self.messageConta_verticalLayout.setObjectName(u"messageConta_verticalLayout")
        self.messageContal_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageContal_title_label.setObjectName(u"messageContal_title_label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.messageContal_title_label.setFont(font1)
        self.messageContal_title_label.setAlignment(Qt.AlignCenter)

        self.messageConta_verticalLayout.addWidget(self.messageContal_title_label)

        self.messageConta_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageConta_value_label.setObjectName(u"messageConta_value_label")
        self.messageConta_value_label.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(True)
        self.messageConta_value_label.setFont(font2)
        self.messageConta_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageConta_value_label.setAlignment(Qt.AlignCenter)

        self.messageConta_verticalLayout.addWidget(self.messageConta_value_label)


        self.horizontalLayout.addLayout(self.messageConta_verticalLayout)

        self.messageReference_verticalLayout = QVBoxLayout()
        self.messageReference_verticalLayout.setObjectName(u"messageReference_verticalLayout")
        self.messageReference_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageReference_title_label.setObjectName(u"messageReference_title_label")
        self.messageReference_title_label.setFont(font1)
        self.messageReference_title_label.setAlignment(Qt.AlignCenter)

        self.messageReference_verticalLayout.addWidget(self.messageReference_title_label)

        self.messageReference_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageReference_value_label.setObjectName(u"messageReference_value_label")
        self.messageReference_value_label.setEnabled(True)
        self.messageReference_value_label.setFont(font2)
        self.messageReference_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageReference_value_label.setAlignment(Qt.AlignCenter)

        self.messageReference_verticalLayout.addWidget(self.messageReference_value_label)


        self.horizontalLayout.addLayout(self.messageReference_verticalLayout)

        self.messageTotal_verticalLayout = QVBoxLayout()
        self.messageTotal_verticalLayout.setObjectName(u"messageTotal_verticalLayout")
        self.messageTotal_title_label = QLabel(self.horizontalLayoutWidget)
        self.messageTotal_title_label.setObjectName(u"messageTotal_title_label")
        self.messageTotal_title_label.setFont(font1)
        self.messageTotal_title_label.setAlignment(Qt.AlignCenter)

        self.messageTotal_verticalLayout.addWidget(self.messageTotal_title_label)

        self.messageTotal_value_label = QLabel(self.horizontalLayoutWidget)
        self.messageTotal_value_label.setObjectName(u"messageTotal_value_label")
        self.messageTotal_value_label.setEnabled(True)
        self.messageTotal_value_label.setFont(font2)
        self.messageTotal_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.messageTotal_value_label.setAlignment(Qt.AlignCenter)

        self.messageTotal_verticalLayout.addWidget(self.messageTotal_value_label)


        self.horizontalLayout.addLayout(self.messageTotal_verticalLayout)

        self.horizontalLayoutWidget_5 = QWidget(Dialog)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(40, 170, 551, 45))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.new_pushButton = QPushButton(self.horizontalLayoutWidget_5)
        self.new_pushButton.setObjectName(u"new_pushButton")
        self.new_pushButton.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(12)
        self.new_pushButton.setFont(font3)

        self.horizontalLayout_2.addWidget(self.new_pushButton)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(610, 230, 151, 136))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SomaItems_verticalLayout = QVBoxLayout()
        self.SomaItems_verticalLayout.setObjectName(u"SomaItems_verticalLayout")
        self.somaItens_title_label = QLabel(self.verticalLayoutWidget)
        self.somaItens_title_label.setObjectName(u"somaItens_title_label")
        self.somaItens_title_label.setFont(font1)
        self.somaItens_title_label.setAlignment(Qt.AlignCenter)

        self.SomaItems_verticalLayout.addWidget(self.somaItens_title_label)

        self.somaItens_value_label = QLabel(self.verticalLayoutWidget)
        self.somaItens_value_label.setObjectName(u"somaItens_value_label")
        self.somaItens_value_label.setEnabled(True)
        self.somaItens_value_label.setFont(font2)
        self.somaItens_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.somaItens_value_label.setAlignment(Qt.AlignCenter)

        self.SomaItems_verticalLayout.addWidget(self.somaItens_value_label)


        self.verticalLayout.addLayout(self.SomaItems_verticalLayout)

        self.QuantidadeItens_verticalLayout = QVBoxLayout()
        self.QuantidadeItens_verticalLayout.setObjectName(u"QuantidadeItens_verticalLayout")
        self.quantidadeItens_title_label = QLabel(self.verticalLayoutWidget)
        self.quantidadeItens_title_label.setObjectName(u"quantidadeItens_title_label")
        self.quantidadeItens_title_label.setFont(font1)
        self.quantidadeItens_title_label.setAlignment(Qt.AlignCenter)

        self.QuantidadeItens_verticalLayout.addWidget(self.quantidadeItens_title_label)

        self.quantidadeItens_value_label = QLabel(self.verticalLayoutWidget)
        self.quantidadeItens_value_label.setObjectName(u"quantidadeItens_value_label")
        self.quantidadeItens_value_label.setEnabled(True)
        self.quantidadeItens_value_label.setFont(font2)
        self.quantidadeItens_value_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.quantidadeItens_value_label.setAlignment(Qt.AlignCenter)

        self.QuantidadeItens_verticalLayout.addWidget(self.quantidadeItens_value_label)


        self.verticalLayout.addLayout(self.QuantidadeItens_verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"Detalhamento Cobran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.messageContal_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageContal_title_label.setText(QCoreApplication.translate("Dialog", u"Conta", None))
        self.messageConta_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messageReference_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageReference_title_label.setText(QCoreApplication.translate("Dialog", u"Ano / M\u00eas", None))
        self.messageReference_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.messageTotal_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.messageTotal_title_label.setText(QCoreApplication.translate("Dialog", u"Total Realizado", None))
        self.messageTotal_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.new_pushButton.setToolTip(QCoreApplication.translate("Dialog", u"Inicia formul\u00e1rio para cadastro de nova cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.new_pushButton.setText(QCoreApplication.translate("Dialog", u" Adicionar Item", None))
#if QT_CONFIG(tooltip)
        self.somaItens_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.somaItens_title_label.setText(QCoreApplication.translate("Dialog", u"R$ Soma", None))
        self.somaItens_value_label.setText("")
#if QT_CONFIG(tooltip)
        self.quantidadeItens_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.quantidadeItens_title_label.setText(QCoreApplication.translate("Dialog", u"Quantidade", None))
        self.quantidadeItens_value_label.setText("")
    # retranslateUi

