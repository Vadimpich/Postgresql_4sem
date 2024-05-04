# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_records.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_recordsWidget(object):
    def setupUi(self, recordsWidget):
        if not recordsWidget.objectName():
            recordsWidget.setObjectName(u"recordsWidget")
        recordsWidget.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        recordsWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(recordsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBack = QPushButton(recordsWidget)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(40, 40))
        self.buttonBack.setMaximumSize(QSize(40, 16777214))
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.buttonBack.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonBack)

        self.label = QLabel(recordsWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(recordsWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchBox = QComboBox(self.frame)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(12)
        self.searchBox.setFont(font2)

        self.horizontalLayout_3.addWidget(self.searchBox)

        self.searchField = QLineEdit(self.frame)
        self.searchField.setObjectName(u"searchField")

        self.horizontalLayout_3.addWidget(self.searchField)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.dataTable = QTableWidget(self.frame)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setMinimumSize(QSize(600, 0))
        self.dataTable.setLineWidth(1)

        self.verticalLayout_2.addWidget(self.dataTable)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(recordsWidget)

        QMetaObject.connectSlotsByName(recordsWidget)
    # setupUi

    def retranslateUi(self, recordsWidget):
        recordsWidget.setWindowTitle(QCoreApplication.translate("recordsWidget", u"Form", None))
        self.buttonBack.setText("")
        self.label.setText(QCoreApplication.translate("recordsWidget", u"\u041c\u043e\u0438 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.searchBox.setPlaceholderText(QCoreApplication.translate("recordsWidget", u"\u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
    # retranslateUi

