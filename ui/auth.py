# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
        Dialog.resize(600, 400)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        Dialog.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"user-available"))
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(22)
        self.nameLabel.setFont(font1)
        self.nameLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.nameLabel)

        self.loginInput = QLineEdit(self.widget)
        self.loginInput.setObjectName(u"loginInput")
        self.loginInput.setMinimumSize(QSize(350, 0))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(16)
        self.loginInput.setFont(font2)

        self.verticalLayout.addWidget(self.loginInput)

        self.passInput = QLineEdit(self.widget)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setFont(font2)
        self.passInput.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.passInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passInput)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFont(font2)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setFlat(False)

        self.verticalLayout.addWidget(self.loginButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.loginInput.setInputMask("")
        self.loginInput.setText("")
        self.loginInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi
