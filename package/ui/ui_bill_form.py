# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bill_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 632)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 401, 611))
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

        self.title_verticalLayout = QVBoxLayout()
        self.title_verticalLayout.setObjectName(u"title_verticalLayout")
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.title_label.setFont(font2)
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.title_verticalLayout.addWidget(self.title_label)

        self.title_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.title_lineEdit.setObjectName(u"title_lineEdit")

        self.title_verticalLayout.addWidget(self.title_lineEdit)


        self.verticalLayout.addLayout(self.title_verticalLayout)

        self.desc_verticalLayout = QVBoxLayout()
        self.desc_verticalLayout.setObjectName(u"desc_verticalLayout")
        self.desc_label = QLabel(self.verticalLayoutWidget)
        self.desc_label.setObjectName(u"desc_label")
        self.desc_label.setFont(font2)
        self.desc_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.desc_verticalLayout.addWidget(self.desc_label)

        self.desc_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.desc_lineEdit.setObjectName(u"desc_lineEdit")

        self.desc_verticalLayout.addWidget(self.desc_lineEdit)


        self.verticalLayout.addLayout(self.desc_verticalLayout)

        self.category_verticalLayout = QVBoxLayout()
        self.category_verticalLayout.setObjectName(u"category_verticalLayout")
        self.category_label = QLabel(self.verticalLayoutWidget)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setFont(font2)
        self.category_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.category_verticalLayout.addWidget(self.category_label)

        self.category_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.category_lineEdit.setObjectName(u"category_lineEdit")

        self.category_verticalLayout.addWidget(self.category_lineEdit)


        self.verticalLayout.addLayout(self.category_verticalLayout)

        self.pay_day_verticalLayout = QVBoxLayout()
        self.pay_day_verticalLayout.setObjectName(u"pay_day_verticalLayout")
        self.pay_day_label = QLabel(self.verticalLayoutWidget)
        self.pay_day_label.setObjectName(u"pay_day_label")
        self.pay_day_label.setFont(font2)
        self.pay_day_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.pay_day_verticalLayout.addWidget(self.pay_day_label)

        self.pay_day_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.pay_day_spinBox.setObjectName(u"pay_day_spinBox")
        self.pay_day_spinBox.setMinimum(1)
        self.pay_day_spinBox.setMaximum(31)

        self.pay_day_verticalLayout.addWidget(self.pay_day_spinBox)


        self.verticalLayout.addLayout(self.pay_day_verticalLayout)

        self.initial_value_verticalLayout = QVBoxLayout()
        self.initial_value_verticalLayout.setObjectName(u"initial_value_verticalLayout")
        self.initial_valuecompletion_label = QLabel(self.verticalLayoutWidget)
        self.initial_valuecompletion_label.setObjectName(u"initial_valuecompletion_label")
        self.initial_valuecompletion_label.setFont(font2)
        self.initial_valuecompletion_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.initial_value_verticalLayout.addWidget(self.initial_valuecompletion_label)

        self.initial_value_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.initial_value_lineEdit.setObjectName(u"initial_value_lineEdit")
        font3 = QFont()
        font3.setPointSize(12)
        self.initial_value_lineEdit.setFont(font3)
        self.initial_value_lineEdit.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.initial_value_verticalLayout.addWidget(self.initial_value_lineEdit)


        self.verticalLayout.addLayout(self.initial_value_verticalLayout)

        self.activated_verticalLayout = QVBoxLayout()
        self.activated_verticalLayout.setObjectName(u"activated_verticalLayout")
        self.activated_label = QLabel(self.verticalLayoutWidget)
        self.activated_label.setObjectName(u"activated_label")
        self.activated_label.setFont(font2)
        self.activated_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.activated_verticalLayout.addWidget(self.activated_label)

        self.activated_buttons_horizontalLayout = QHBoxLayout()
        self.activated_buttons_horizontalLayout.setObjectName(u"activated_buttons_horizontalLayout")
        self.activated_true_radioButton = QRadioButton(self.verticalLayoutWidget)
        self.activated_true_radioButton.setObjectName(u"activated_true_radioButton")
        self.activated_true_radioButton.setFont(font3)
        self.activated_true_radioButton.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.activated_true_radioButton.setChecked(True)

        self.activated_buttons_horizontalLayout.addWidget(self.activated_true_radioButton)

        self.activated_false_radioButton = QRadioButton(self.verticalLayoutWidget)
        self.activated_false_radioButton.setObjectName(u"activated_false_radioButton")
        self.activated_false_radioButton.setFont(font3)
        self.activated_false_radioButton.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.activated_buttons_horizontalLayout.addWidget(self.activated_false_radioButton)


        self.activated_verticalLayout.addLayout(self.activated_buttons_horizontalLayout)


        self.verticalLayout.addLayout(self.activated_verticalLayout)

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

        QWidget.setTabOrder(self.title_lineEdit, self.desc_lineEdit)
        QWidget.setTabOrder(self.desc_lineEdit, self.category_lineEdit)
        QWidget.setTabOrder(self.category_lineEdit, self.pay_day_spinBox)
        QWidget.setTabOrder(self.pay_day_spinBox, self.initial_value_lineEdit)
        QWidget.setTabOrder(self.initial_value_lineEdit, self.activated_true_radioButton)
        QWidget.setTabOrder(self.activated_true_radioButton, self.activated_false_radioButton)
        QWidget.setTabOrder(self.activated_false_radioButton, self.save_pushButton)
        QWidget.setTabOrder(self.save_pushButton, self.cancel_pushButton)

        self.retranslateUi(Dialog)

        self.save_pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Conta", None))
        self.header_title_label.setText(QCoreApplication.translate("Dialog", u"Cadastro de Conta", None))
        self.bill_title_label.setText("")
#if QT_CONFIG(tooltip)
        self.title_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.title_label.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo", None))
        self.title_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"title", None))
#if QT_CONFIG(tooltip)
        self.desc_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.desc_label.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o", None))
        self.desc_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"description", None))
#if QT_CONFIG(tooltip)
        self.category_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.category_label.setText(QCoreApplication.translate("Dialog", u"Categoria", None))
        self.category_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"category", None))
#if QT_CONFIG(tooltip)
        self.pay_day_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pay_day_label.setText(QCoreApplication.translate("Dialog", u"Dia de Pagamento", None))
        self.pay_day_spinBox.setProperty("model_name", QCoreApplication.translate("Dialog", u"payment_day", None))
#if QT_CONFIG(tooltip)
        self.initial_valuecompletion_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.initial_valuecompletion_label.setText(QCoreApplication.translate("Dialog", u"Valor Inicial", None))
        self.initial_value_lineEdit.setInputMask(QCoreApplication.translate("Dialog", u"99999.99", None))
        self.initial_value_lineEdit.setText(QCoreApplication.translate("Dialog", u".", None))
        self.initial_value_lineEdit.setPlaceholderText("")
        self.initial_value_lineEdit.setProperty("model_name", QCoreApplication.translate("Dialog", u"initial_value", None))
#if QT_CONFIG(tooltip)
        self.activated_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Sum of invoices's values</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.activated_label.setText(QCoreApplication.translate("Dialog", u"Situa\u00e7\u00e3o", None))
        self.activated_true_radioButton.setText(QCoreApplication.translate("Dialog", u"Ativo", None))
        self.activated_false_radioButton.setText(QCoreApplication.translate("Dialog", u"Inativo", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.save_pushButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
    # retranslateUi

