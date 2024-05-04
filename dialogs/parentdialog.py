from PySide6 import QtCore, QtGui, QtWidgets

from ui.parent import Ui_parentDialog


class ParentDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_parentDialog()
        self.ui.setupUi(self)
        self.ui.box.addWidget(parent)
