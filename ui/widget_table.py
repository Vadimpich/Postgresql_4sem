# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_table.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_tableWidget(object):
    def setupUi(self, tableWidget):
        if not tableWidget.objectName():
            tableWidget.setObjectName(u"tableWidget")
        tableWidget.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        tableWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(tableWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonBack = QPushButton(tableWidget)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setMinimumSize(QSize(40, 40))
        self.buttonBack.setMaximumSize(QSize(40, 16777215))
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.buttonBack.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.buttonBack)

        self.tableName = QLabel(tableWidget)
        self.tableName.setObjectName(u"tableName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableName.sizePolicy().hasHeightForWidth())
        self.tableName.setSizePolicy(sizePolicy)
        self.tableName.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(28)
        self.tableName.setFont(font1)
        self.tableName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.tableName)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(tableWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)

        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonAdd = QPushButton(self.frame)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setMinimumSize(QSize(40, 40))
        icon1 = QIcon(QIcon.fromTheme(u"list-add"))
        self.buttonAdd.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.buttonAdd)

        self.buttonEdit = QPushButton(self.frame)
        self.buttonEdit.setObjectName(u"buttonEdit")
        self.buttonEdit.setEnabled(False)
        self.buttonEdit.setMinimumSize(QSize(40, 40))
        icon2 = QIcon(QIcon.fromTheme(u"mail-message-new"))
        self.buttonEdit.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.buttonEdit)

        self.buttonDelete = QPushButton(self.frame)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setEnabled(False)
        self.buttonDelete.setMinimumSize(QSize(40, 40))
        icon3 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.buttonDelete.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.buttonDelete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(tableWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchBox = QComboBox(self.frame_2)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMinimumSize(QSize(200, 0))
        self.searchBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.searchBox)

        self.searchField = QLineEdit(self.frame_2)
        self.searchField.setObjectName(u"searchField")

        self.horizontalLayout_3.addWidget(self.searchField)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dataTable = QTableWidget(self.frame_3)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setMinimumSize(QSize(600, 0))
        self.dataTable.setLineWidth(1)

        self.verticalLayout_4.addWidget(self.dataTable)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.saveButton = QPushButton(self.frame_2)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(40, 40))
        icon4 = QIcon(QIcon.fromTheme(u"document-save"))
        self.saveButton.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.saveButton)

        self.printButton = QPushButton(self.frame_2)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setMinimumSize(QSize(40, 40))
        icon5 = QIcon(QIcon.fromTheme(u"document-print"))
        self.printButton.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.printButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(tableWidget)

        QMetaObject.connectSlotsByName(tableWidget)
    # setupUi

    def retranslateUi(self, tableWidget):
        tableWidget.setWindowTitle(QCoreApplication.translate("tableWidget", u"Form", None))
        self.buttonBack.setText("")
        self.tableName.setText(QCoreApplication.translate("tableWidget", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.buttonAdd.setText("")
        self.buttonEdit.setText("")
        self.buttonDelete.setText("")
        self.searchBox.setPlaceholderText(QCoreApplication.translate("tableWidget", u"\u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.saveButton.setText("")
        self.printButton.setText("")
    # retranslateUi

