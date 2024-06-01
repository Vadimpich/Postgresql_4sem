# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_employee.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_employeeWidget(object):
    def setupUi(self, employeeWidget):
        if not employeeWidget.objectName():
            employeeWidget.setObjectName(u"employeeWidget")
        employeeWidget.resize(1000, 600)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(16)
        employeeWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(employeeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(employeeWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(22)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.buttonPassword = QPushButton(employeeWidget)
        self.buttonPassword.setObjectName(u"buttonPassword")
        self.buttonPassword.setMinimumSize(QSize(40, 40))
        icon = QIcon(QIcon.fromTheme(u"mail-message-new"))
        self.buttonPassword.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.buttonPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(18)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(employeeWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 50, -1, 50)
        self.buttonAccept = QPushButton(self.frame)
        self.buttonAccept.setObjectName(u"buttonAccept")
        self.buttonAccept.setEnabled(False)
        self.buttonAccept.setMinimumSize(QSize(208, 0))
        self.buttonAccept.setFont(font)

        self.verticalLayout_5.addWidget(self.buttonAccept)

        self.buttonComplete = QPushButton(self.frame)
        self.buttonComplete.setObjectName(u"buttonComplete")
        self.buttonComplete.setEnabled(False)
        self.buttonComplete.setFont(font)

        self.verticalLayout_5.addWidget(self.buttonComplete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.buttonServices = QPushButton(self.frame)
        self.buttonServices.setObjectName(u"buttonServices")
        self.buttonServices.setMinimumSize(QSize(0, 50))
        self.buttonServices.setFont(font)

        self.verticalLayout_5.addWidget(self.buttonServices)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.tabWidget = QTabWidget(employeeWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.pendingTab = QWidget()
        self.pendingTab.setObjectName(u"pendingTab")
        self.verticalLayout_2 = QVBoxLayout(self.pendingTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pendingTable = QTableWidget(self.pendingTab)
        self.pendingTable.setObjectName(u"pendingTable")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(12)
        self.pendingTable.setFont(font2)

        self.verticalLayout_2.addWidget(self.pendingTable)

        self.tabWidget.addTab(self.pendingTab, "")
        self.completedTab = QWidget()
        self.completedTab.setObjectName(u"completedTab")
        self.verticalLayout_3 = QVBoxLayout(self.completedTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.completedTable = QTableWidget(self.completedTab)
        self.completedTable.setObjectName(u"completedTable")
        self.completedTable.setFont(font2)

        self.verticalLayout_3.addWidget(self.completedTable)

        self.tabWidget.addTab(self.completedTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(employeeWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(employeeWidget)
    # setupUi

    def retranslateUi(self, employeeWidget):
        employeeWidget.setWindowTitle(QCoreApplication.translate("employeeWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("employeeWidget", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0441\u0432\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.buttonPassword.setText("")
        self.buttonAccept.setText(QCoreApplication.translate("employeeWidget", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.buttonComplete.setText(QCoreApplication.translate("employeeWidget", u"\u0417\u0430\u043a\u0430\u0437 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d", None))
        self.buttonServices.setText(QCoreApplication.translate("employeeWidget", u"\u041c\u043e\u0438 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pendingTab), QCoreApplication.translate("employeeWidget", u"\u041d\u043e\u0432\u044b\u0435 \u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.completedTab), QCoreApplication.translate("employeeWidget", u"\u041c\u043e\u0438 \u0437\u0430\u043a\u0430\u0437\u044b", None))
    # retranslateUi

