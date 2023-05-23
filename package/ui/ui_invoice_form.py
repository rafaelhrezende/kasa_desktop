# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_form.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(487, 772)
        Dialog.setMinimumSize(QSize(487, 772))
        Dialog.setMaximumSize(QSize(487, 772))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 461, 751))
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
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(True)
        self.bill_title_label.setFont(font1)
        self.bill_title_label.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.bill_title_label.setAlignment(Qt.AlignCenter)

        self.header_verticalLayout.addWidget(self.bill_title_label)


        self.verticalLayout.addLayout(self.header_verticalLayout)

        self.reference_verticalLayout = QVBoxLayout()
        self.reference_verticalLayout.setObjectName(u"reference_verticalLayout")
        self.ref_title_label = QLabel(self.verticalLayoutWidget)
        self.ref_title_label.setObjectName(u"ref_title_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.ref_title_label.setFont(font2)
        self.ref_title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.reference_verticalLayout.addWidget(self.ref_title_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.year_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.year_spinBox.setObjectName(u"year_spinBox")
        font3 = QFont()
        font3.setPointSize(12)
        self.year_spinBox.setFont(font3)
        self.year_spinBox.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.year_spinBox.setMinimum(1900)
        self.year_spinBox.setMaximum(3000)
        self.year_spinBox.setValue(2023)

        self.horizontalLayout.addWidget(self.year_spinBox)

        self.month_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.month_spinBox.setObjectName(u"month_spinBox")
        self.month_spinBox.setFont(font3)
        self.month_spinBox.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.month_spinBox.setMinimum(1)
        self.month_spinBox.setMaximum(12)
        self.month_spinBox.setValue(5)

        self.horizontalLayout.addWidget(self.month_spinBox)


        self.reference_verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.reference_verticalLayout)

        self.value_verticalLayout = QVBoxLayout()
        self.value_verticalLayout.setObjectName(u"value_verticalLayout")
        self.value_label = QLabel(self.verticalLayoutWidget)
        self.value_label.setObjectName(u"value_label")
        self.value_label.setFont(font2)
        self.value_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.value_verticalLayout.addWidget(self.value_label)

        self.value_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.value_lineEdit.setObjectName(u"value_lineEdit")
        self.value_lineEdit.setFont(font3)
        self.value_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.value_verticalLayout.addWidget(self.value_lineEdit)


        self.verticalLayout.addLayout(self.value_verticalLayout)

        self.method_verticalLayout = QVBoxLayout()
        self.method_verticalLayout.setObjectName(u"method_verticalLayout")
        self.method_label = QLabel(self.verticalLayoutWidget)
        self.method_label.setObjectName(u"method_label")
        self.method_label.setFont(font2)
        self.method_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.method_verticalLayout.addWidget(self.method_label)

        self.method_comboBox = QComboBox(self.verticalLayoutWidget)
        self.method_comboBox.setObjectName(u"method_comboBox")
        self.method_comboBox.setFont(font3)
        self.method_comboBox.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.method_verticalLayout.addWidget(self.method_comboBox)


        self.verticalLayout.addLayout(self.method_verticalLayout)

        self.due_date_verticalLayout = QVBoxLayout()
        self.due_date_verticalLayout.setObjectName(u"due_date_verticalLayout")
        self.due_date_label = QLabel(self.verticalLayoutWidget)
        self.due_date_label.setObjectName(u"due_date_label")
        self.due_date_label.setFont(font2)
        self.due_date_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.due_date_verticalLayout.addWidget(self.due_date_label)

        self.due_date_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.due_date_lineEdit.setObjectName(u"due_date_lineEdit")
        self.due_date_lineEdit.setFont(font3)
        self.due_date_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.due_date_verticalLayout.addWidget(self.due_date_lineEdit)


        self.verticalLayout.addLayout(self.due_date_verticalLayout)

        self.completion_verticalLayout = QVBoxLayout()
        self.completion_verticalLayout.setObjectName(u"completion_verticalLayout")
        self.completion_label = QLabel(self.verticalLayoutWidget)
        self.completion_label.setObjectName(u"completion_label")
        self.completion_label.setFont(font2)
        self.completion_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.completion_verticalLayout.addWidget(self.completion_label)

        self.completion_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.completion_lineEdit.setObjectName(u"completion_lineEdit")
        self.completion_lineEdit.setFont(font3)
        self.completion_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.completion_verticalLayout.addWidget(self.completion_lineEdit)


        self.verticalLayout.addLayout(self.completion_verticalLayout)

        self.pay_day_verticalLayout = QVBoxLayout()
        self.pay_day_verticalLayout.setObjectName(u"pay_day_verticalLayout")
        self.pay_day_label = QLabel(self.verticalLayoutWidget)
        self.pay_day_label.setObjectName(u"pay_day_label")
        self.pay_day_label.setFont(font2)
        self.pay_day_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.pay_day_verticalLayout.addWidget(self.pay_day_label)

        self.pay_day_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.pay_day_lineEdit.setObjectName(u"pay_day_lineEdit")
        self.pay_day_lineEdit.setFont(font3)
        self.pay_day_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.pay_day_verticalLayout.addWidget(self.pay_day_lineEdit)


        self.verticalLayout.addLayout(self.pay_day_verticalLayout)

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
        self.save_pushButton.setAutoDefault(True)

        self.acttions_horizontalLayout.addWidget(self.save_pushButton)


        self.verticalLayout.addLayout(self.acttions_horizontalLayout)

        QWidget.setTabOrder(self.year_spinBox, self.month_spinBox)
        QWidget.setTabOrder(self.month_spinBox, self.value_lineEdit)
        QWidget.setTabOrder(self.value_lineEdit, self.method_comboBox)
        QWidget.setTabOrder(self.method_comboBox, self.due_date_lineEdit)
        QWidget.setTabOrder(self.due_date_lineEdit, self.completion_lineEdit)
        QWidget.setTabOrder(self.completion_lineEdit, self.pay_day_lineEdit)
        QWidget.setTabOrder(self.pay_day_lineEdit, self.save_pushButton)
        QWidget.setTabOrder(self.save_pushButton, self.cancel_pushButton)

        self.retranslateUi(Dialog)
        self.cancel_pushButton.clicked.connect(Dialog.reject)

        self.save_pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cobran\u00e7a", None))
        self.header_title_label.setText(QCoreApplication.translate("Dialog", u"Cadastro de Cobran\u00e7a", None))
        self.bill_title_label.setText(QCoreApplication.translate("Dialog", u"Conta 1", None))
#if QT_CONFIG(tooltip)
        self.ref_title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ref_title_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Ano / M\u00eas </p></body></html>", None))
        self.year_spinBox.setSuffix("")
        self.year_spinBox.setProperty("model_name", QCoreApplication.translate("Dialog", u"reference_year", None))
        self.month_spinBox.setProperty("model_name", QCoreApplication.translate("Dialog", u"reference_month", None))
#if QT_CONFIG(tooltip)
        self.value_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.value_label.setText(QCoreApplication.translate("Dialog", u"Valor", None))
        self.value_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"99999.99", None))
        self.value_lineEdit.setText(QCoreApplication.translate("Dialog", u".", None))
        self.value_lineEdit.setPlaceholderText("")
        self.value_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"value", None))
#if QT_CONFIG(tooltip)
        self.method_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_label.setText(QCoreApplication.translate("Dialog", u"Forma Pagamento", None))
        self.method_comboBox.setProperty("model_name", QCoreApplication.translate("Dialog", u"method", None))
#if QT_CONFIG(tooltip)
        self.due_date_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.due_date_label.setText(QCoreApplication.translate("Dialog", u"Data Vencimento", None))
        self.due_date_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"00/00/0000", None))
        self.due_date_lineEdit.setText(QCoreApplication.translate("Dialog", u"//", None))
        self.due_date_lineEdit.setPlaceholderText("")
        self.due_date_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"due_date", None))
#if QT_CONFIG(tooltip)
        self.completion_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.completion_label.setText(QCoreApplication.translate("Dialog", u"Data Realiza\u00e7\u00e3o", None))
        self.completion_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"00/00/0000", None))
        self.completion_lineEdit.setText(QCoreApplication.translate("Dialog", u"//", None))
        self.completion_lineEdit.setPlaceholderText("")
        self.completion_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"completion_date", None))
#if QT_CONFIG(tooltip)
        self.pay_day_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pay_day_label.setText(QCoreApplication.translate("Dialog", u"Data Pagamento", None))
        self.pay_day_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"00/00/0000", None))
        self.pay_day_lineEdit.setText(QCoreApplication.translate("Dialog", u"//", None))
        self.pay_day_lineEdit.setPlaceholderText("")
        self.pay_day_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"pay_day", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.save_pushButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
    # retranslateUi

