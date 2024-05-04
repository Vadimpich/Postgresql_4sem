from PySide6 import QtCore, QtGui, QtWidgets

from ui.widget_admin import Ui_adminWidget
from widgets import tablewidget
from modules.models import *


class AdminWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_adminWidget()
        self.ui.setupUi(self)
        self.setup_controls()

    def setup_controls(self):
        self.ui.buttonService.clicked.connect(lambda: self.open_table(Service))
        self.ui.buttonProm.clicked.connect(lambda: self.open_table(Promotion))
        self.ui.buttonClient.clicked.connect(lambda: self.open_table(Client))
        self.ui.buttonEmp.clicked.connect(lambda: self.open_table(Employee))
        self.ui.buttonRecord.clicked.connect(lambda: self.open_table(Record))
        self.ui.buttonUser.clicked.connect(lambda: self.open_table(Users))

    def open_table(self, model):
        self.parent().addWidget(
            tablewidget.TableWidget(model, self.parent().currentIndex()))
        self.parent().setCurrentIndex(self.parent().count() - 1)

