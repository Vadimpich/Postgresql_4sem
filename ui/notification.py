# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notification.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_notification(object):
    def setupUi(self, notification):
        if not notification.objectName():
            notification.setObjectName(u"notification")
        notification.resize(900, 150)
        self.verticalLayout = QVBoxLayout(notification)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(notification)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelText = QLabel(self.frame)
        self.labelText.setObjectName(u"labelText")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(16)
        self.labelText.setFont(font1)
        self.labelText.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.labelText)

        self.labelDate = QLabel(self.frame)
        self.labelDate.setObjectName(u"labelDate")
        self.labelDate.setMaximumSize(QSize(16777215, 30))
        self.labelDate.setStyleSheet(u"color: rgb(149, 149, 149)")

        self.verticalLayout_2.addWidget(self.labelDate)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(notification)

        QMetaObject.connectSlotsByName(notification)
    # setupUi

    def retranslateUi(self, notification):
        notification.setWindowTitle(QCoreApplication.translate("notification", u"Form", None))
        self.labelText.setText(QCoreApplication.translate("notification", u"TEXE\n"
"EXEX", None))
        self.labelDate.setText(QCoreApplication.translate("notification", u"hh:mm, dd.MM.yyyy", None))
    # retranslateUi

