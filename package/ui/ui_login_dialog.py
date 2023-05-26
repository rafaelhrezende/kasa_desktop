# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 261)
        Dialog.setMinimumSize(QSize(400, 261))
        Dialog.setMaximumSize(QSize(400, 261))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 140, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 377, 96))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setMinimumSize(QSize(300, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.userNameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passwordLineEdit)

        self.userNameLabel = QLabel(self.formLayoutWidget)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.userNameLabel)

        self.messageLabel = QLabel(Dialog)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setGeometry(QRect(10, 200, 381, 20))
        self.messageLabel.setScaledContents(False)
        self.messageLabel.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.userNameLineEdit, self.passwordLineEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Autentica\u00e7\u00e3o", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.userNameLabel.setText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.messageLabel.setText("")
    # retranslateUi

