import datetime

from PySide6 import QtCore, QtGui, QtWidgets

from ui.notification import Ui_notification


class NotificationWidget(QtWidgets.QWidget):
    def __init__(self, notification=None):
        super().__init__()
        self.ui = Ui_notification()
        self.ui.setupUi(self)
        self.ui.labelText.setText(notification[1])
        self.ui.labelDate.setText(notification[3].strftime('%d.%m.%Y %H:%M'))
