# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_user.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_clientWidget(object):
    def setupUi(self, clientWidget):
        if not clientWidget.objectName():
            clientWidget.setObjectName(u"clientWidget")
        clientWidget.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        clientWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(clientWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(clientWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(22)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.buttonPassword = QPushButton(clientWidget)
        self.buttonPassword.setObjectName(u"buttonPassword")
        self.buttonPassword.setMinimumSize(QSize(40, 40))
        icon = QIcon(QIcon.fromTheme(u"mail-message-new"))
        self.buttonPassword.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.buttonPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(18)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame = QFrame(clientWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 50, -1, 50)
        self.buttonNew = QPushButton(self.frame)
        self.buttonNew.setObjectName(u"buttonNew")
        self.buttonNew.setEnabled(False)
        self.buttonNew.setMinimumSize(QSize(300, 0))

        self.verticalLayout_5.addWidget(self.buttonNew)

        self.buttonRecords = QPushButton(self.frame)
        self.buttonRecords.setObjectName(u"buttonRecords")
        self.buttonRecords.setEnabled(False)

        self.verticalLayout_5.addWidget(self.buttonRecords)

        self.buttonInfo = QPushButton(self.frame)
        self.buttonInfo.setObjectName(u"buttonInfo")

        self.verticalLayout_5.addWidget(self.buttonInfo)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(clientWidget)

        QMetaObject.connectSlotsByName(clientWidget)
    # setupUi

    def retranslateUi(self, clientWidget):
        clientWidget.setWindowTitle(QCoreApplication.translate("clientWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("clientWidget", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0441\u0432\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.buttonPassword.setText("")
        self.buttonNew.setText(QCoreApplication.translate("clientWidget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonRecords.setText(QCoreApplication.translate("clientWidget", u"\u041c\u043e\u0438 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.buttonInfo.setText(QCoreApplication.translate("clientWidget", u"\u041c\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

