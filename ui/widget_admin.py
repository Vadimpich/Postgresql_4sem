# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_admin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_adminWidget(object):
    def setupUi(self, adminWidget):
        if not adminWidget.objectName():
            adminWidget.setObjectName(u"adminWidget")
        adminWidget.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        adminWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(adminWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(adminWidget)
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

        self.verticalSpacer_7 = QSpacerItem(20, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.frame = QFrame(adminWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton_6, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_6 = QSpacerItem(20, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.retranslateUi(adminWidget)

        QMetaObject.connectSlotsByName(adminWidget)
    # setupUi

    def retranslateUi(self, adminWidget):
        adminWidget.setWindowTitle(QCoreApplication.translate("adminWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("adminWidget", u"\u041c\u0435\u043d\u044e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.pushButton_4.setText(QCoreApplication.translate("adminWidget", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("adminWidget", u"\u0410\u043a\u0446\u0438\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("adminWidget", u"\u0417\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("adminWidget", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.pushButton_6.setText(QCoreApplication.translate("adminWidget", u"\u0423\u0447\u0451\u0442\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("adminWidget", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
    # retranslateUi

