# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parent.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_parentDialog(object):
    def setupUi(self, parentDialog):
        if not parentDialog.objectName():
            parentDialog.setObjectName(u"parentDialog")
        parentDialog.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        parentDialog.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"computer"))
        parentDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(parentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.box = QVBoxLayout()
        self.box.setObjectName(u"box")

        self.verticalLayout.addLayout(self.box)


        self.retranslateUi(parentDialog)

        QMetaObject.connectSlotsByName(parentDialog)
    # setupUi

    def retranslateUi(self, parentDialog):
        parentDialog.setWindowTitle(QCoreApplication.translate("parentDialog", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
    # retranslateUi

