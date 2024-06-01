# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'services.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_servicesDialog(object):
    def setupUi(self, servicesDialog):
        if not servicesDialog.objectName():
            servicesDialog.setObjectName(u"servicesDialog")
        servicesDialog.resize(600, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        servicesDialog.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"mail-message-new"))
        servicesDialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(servicesDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lisstFrame = QFrame(servicesDialog)
        self.lisstFrame.setObjectName(u"lisstFrame")
        self.lisstFrame.setMinimumSize(QSize(420, 0))
        self.lisstFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lisstFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lisstFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listBox = QVBoxLayout()
        self.listBox.setObjectName(u"listBox")

        self.verticalLayout_3.addLayout(self.listBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.lisstFrame)

        self.frame = QFrame(servicesDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonAdd = QPushButton(self.frame)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setMinimumSize(QSize(40, 40))
        icon1 = QIcon(QIcon.fromTheme(u"list-add"))
        self.buttonAdd.setIcon(icon1)

        self.verticalLayout.addWidget(self.buttonAdd)

        self.buttonRemove = QPushButton(self.frame)
        self.buttonRemove.setObjectName(u"buttonRemove")
        self.buttonRemove.setMinimumSize(QSize(40, 40))
        icon2 = QIcon(QIcon.fromTheme(u"list-remove"))
        self.buttonRemove.setIcon(icon2)

        self.verticalLayout.addWidget(self.buttonRemove)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonSave = QPushButton(self.frame)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setMinimumSize(QSize(130, 40))

        self.verticalLayout.addWidget(self.buttonSave)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(servicesDialog)

        QMetaObject.connectSlotsByName(servicesDialog)
    # setupUi

    def retranslateUi(self, servicesDialog):
        servicesDialog.setWindowTitle(QCoreApplication.translate("servicesDialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.buttonAdd.setText("")
        self.buttonRemove.setText("")
        self.buttonSave.setText(QCoreApplication.translate("servicesDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

