from PySide6 import QtCore, QtGui, QtWidgets

from ui.wigdet_welcome import Ui_welcomeWidget
from dialogs import authdialog, registerdialog


class WelcomeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_welcomeWidget()
        self.ui.setupUi(self)
        self.setup_controls()

    def setup_controls(self):
        self.ui.registerButton.clicked.connect(self.start_register)
        self.ui.loginButton.clicked.connect(self.start_auth)

    def start_auth(self):
        auth = authdialog.AuthDialog()
        auth.exec()
        self.parent().setCurrentIndex(auth.next_tab)

    def start_register(self):
        register = registerdialog.RegisterDialog()
        register.exec()
        self.parent().setCurrentIndex(register.next_tab)

