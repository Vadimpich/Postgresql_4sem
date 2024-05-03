# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wigdet_welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_welcomeWidget(object):
    def setupUi(self, welcomeWidget):
        if not welcomeWidget.objectName():
            welcomeWidget.setObjectName(u"welcomeWidget")
        welcomeWidget.resize(1006, 633)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        welcomeWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(welcomeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(welcomeWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_7 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(welcomeWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.registerButton = QPushButton(self.frame_2)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(200, 70))

        self.gridLayout_6.addWidget(self.registerButton, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))

        self.gridLayout_6.addWidget(self.label_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(welcomeWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(101, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.label_3, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(200, 70))

        self.gridLayout_5.addWidget(self.loginButton, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.retranslateUi(welcomeWidget)

        QMetaObject.connectSlotsByName(welcomeWidget)
    # setupUi

    def retranslateUi(self, welcomeWidget):
        welcomeWidget.setWindowTitle(QCoreApplication.translate("welcomeWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("welcomeWidget", u"\u0421\u0430\u043b\u043e\u043d \u0443\u0441\u043b\u0443\u0433", None))
        self.registerButton.setText(QCoreApplication.translate("welcomeWidget", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("welcomeWidget", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c?", None))
        self.label_3.setText(QCoreApplication.translate("welcomeWidget", u"\u0423\u0436\u0435 \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u044b?", None))
        self.loginButton.setText(QCoreApplication.translate("welcomeWidget", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

