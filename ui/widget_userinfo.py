# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_userinfo.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_userInfoWidget(object):
    def setupUi(self, userInfoWidget):
        if not userInfoWidget.objectName():
            userInfoWidget.setObjectName(u"userInfoWidget")
        userInfoWidget.resize(1000, 601)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        userInfoWidget.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(userInfoWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(userInfoWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, 50)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setVerticalSpacing(18)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nameField = QLineEdit(self.frame)
        self.nameField.setObjectName(u"nameField")
        self.nameField.setMinimumSize(QSize(300, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameField)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.surnameField = QLineEdit(self.frame)
        self.surnameField.setObjectName(u"surnameField")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.surnameField)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.phoneField = QLineEdit(self.frame)
        self.phoneField.setObjectName(u"phoneField")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.phoneField)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.addressField = QLineEdit(self.frame)
        self.addressField.setObjectName(u"addressField")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.addressField)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.buttonSave = QPushButton(self.frame)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.buttonSave)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.retranslateUi(userInfoWidget)

        QMetaObject.connectSlotsByName(userInfoWidget)
    # setupUi

    def retranslateUi(self, userInfoWidget):
        userInfoWidget.setWindowTitle(QCoreApplication.translate("userInfoWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("userInfoWidget", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("userInfoWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("userInfoWidget", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("userInfoWidget", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.buttonSave.setText(QCoreApplication.translate("userInfoWidget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

