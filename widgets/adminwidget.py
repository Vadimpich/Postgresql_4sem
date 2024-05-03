from PySide6 import QtCore, QtGui, QtWidgets

from ui.widget_admin import Ui_adminWidget
from dialogs import authdialog, registerdialog


class AdminWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_adminWidget()
        self.ui.setupUi(self)
