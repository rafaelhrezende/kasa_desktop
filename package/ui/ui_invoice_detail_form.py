# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_detail_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(351, 568)
        Dialog.setMinimumSize(QSize(351, 568))
        Dialog.setMaximumSize(QSize(487, 772))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 321, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_verticalLayout = QVBoxLayout()
        self.header_verticalLayout.setObjectName(u"header_verticalLayout")
        self.header_title_label = QLabel(self.verticalLayoutWidget)
        self.header_title_label.setObjectName(u"header_title_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.header_title_label.setFont(font)
        self.header_title_label.setAlignment(Qt.AlignCenter)

        self.header_verticalLayout.addWidget(self.header_title_label)

        self.bill_title_label = QLabel(self.verticalLayoutWidget)
        self.bill_title_label.setObjectName(u"bill_title_label")
        self.bill_title_label.setEnabled(True)
        self.bill_title_label.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(True)
        self.bill_title_label.setFont(font1)
        self.bill_title_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.bill_title_label.setAlignment(Qt.AlignCenter)

        self.header_verticalLayout.addWidget(self.bill_title_label)


        self.verticalLayout.addLayout(self.header_verticalLayout)

        self.desc_verticalLayout = QVBoxLayout()
        self.desc_verticalLayout.setObjectName(u"desc_verticalLayout")
        self.desc_label = QLabel(self.verticalLayoutWidget)
        self.desc_label.setObjectName(u"desc_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.desc_label.setFont(font2)
        self.desc_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.desc_verticalLayout.addWidget(self.desc_label)

        self.desc_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.desc_lineEdit.setObjectName(u"desc_lineEdit")

        self.desc_verticalLayout.addWidget(self.desc_lineEdit)


        self.verticalLayout.addLayout(self.desc_verticalLayout)

        self.value_verticalLayout = QVBoxLayout()
        self.value_verticalLayout.setObjectName(u"value_verticalLayout")
        self.value_label = QLabel(self.verticalLayoutWidget)
        self.value_label.setObjectName(u"value_label")
        self.value_label.setFont(font2)
        self.value_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.value_verticalLayout.addWidget(self.value_label)

        self.value_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.value_lineEdit.setObjectName(u"value_lineEdit")
        font3 = QFont()
        font3.setPointSize(12)
        self.value_lineEdit.setFont(font3)
        self.value_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.value_verticalLayout.addWidget(self.value_lineEdit)


        self.verticalLayout.addLayout(self.value_verticalLayout)

        self.date_verticalLayout = QVBoxLayout()
        self.date_verticalLayout.setObjectName(u"date_verticalLayout")
        self.date_label = QLabel(self.verticalLayoutWidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font2)
        self.date_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.date_verticalLayout.addWidget(self.date_label)

        self.date_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.date_lineEdit.setObjectName(u"date_lineEdit")
        self.date_lineEdit.setFont(font3)
        self.date_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.date_verticalLayout.addWidget(self.date_lineEdit)


        self.verticalLayout.addLayout(self.date_verticalLayout)

        self.localidade_verticalLayout = QVBoxLayout()
        self.localidade_verticalLayout.setObjectName(u"localidade_verticalLayout")
        self.localidade_label = QLabel(self.verticalLayoutWidget)
        self.localidade_label.setObjectName(u"localidade_label")
        self.localidade_label.setFont(font2)
        self.localidade_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.localidade_verticalLayout.addWidget(self.localidade_label)

        self.localidade_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.localidade_lineEdit.setObjectName(u"localidade_lineEdit")

        self.localidade_verticalLayout.addWidget(self.localidade_lineEdit)


        self.verticalLayout.addLayout(self.localidade_verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.acttions_horizontalLayout = QHBoxLayout()
        self.acttions_horizontalLayout.setObjectName(u"acttions_horizontalLayout")
        self.cancel_pushButton = QPushButton(self.verticalLayoutWidget)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setFont(font2)
        self.cancel_pushButton.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.acttions_horizontalLayout.addWidget(self.cancel_pushButton)

        self.save_pushButton = QPushButton(self.verticalLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setFont(font2)
        self.save_pushButton.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.save_pushButton.setAutoDefault(False)

        self.acttions_horizontalLayout.addWidget(self.save_pushButton)


        self.verticalLayout.addLayout(self.acttions_horizontalLayout)

        QWidget.setTabOrder(self.desc_lineEdit, self.value_lineEdit)
        QWidget.setTabOrder(self.value_lineEdit, self.date_lineEdit)
        QWidget.setTabOrder(self.date_lineEdit, self.localidade_lineEdit)
        QWidget.setTabOrder(self.localidade_lineEdit, self.save_pushButton)
        QWidget.setTabOrder(self.save_pushButton, self.cancel_pushButton)

        self.retranslateUi(Dialog)
        self.cancel_pushButton.clicked.connect(Dialog.reject)

        self.save_pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cobran\u00e7a", None))
        self.header_title_label.setText(QCoreApplication.translate("Dialog", u"Item de Cobran\u00e7a", None))
        self.bill_title_label.setText(QCoreApplication.translate("Dialog", u" -", None))
#if QT_CONFIG(tooltip)
        self.desc_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.desc_label.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o", None))
        self.desc_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"description", None))
#if QT_CONFIG(tooltip)
        self.value_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.value_label.setText(QCoreApplication.translate("Dialog", u"Valor", None))
        self.value_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"99999.99", None))
        self.value_lineEdit.setText(QCoreApplication.translate("Dialog", u".", None))
        self.value_lineEdit.setPlaceholderText("")
        self.value_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"value", None))
#if QT_CONFIG(tooltip)
        self.date_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.date_label.setText(QCoreApplication.translate("Dialog", u"Data", None))
        self.date_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"00/00/0000", None))
        self.date_lineEdit.setText(QCoreApplication.translate("Dialog", u"//", None))
        self.date_lineEdit.setPlaceholderText("")
        self.date_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"pay_day", None))
#if QT_CONFIG(tooltip)
        self.localidade_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.localidade_label.setText(QCoreApplication.translate("Dialog", u"Local", None))
        self.localidade_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"description", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.save_pushButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
    # retranslateUi

