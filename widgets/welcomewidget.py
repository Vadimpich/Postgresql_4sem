from PySide6 import QtCore, QtGui, QtWidgets

from ui.widget_welcome import Ui_welcomeWidget
from dialogs import authdialog, registerdialog
from widgets import adminwidget, userwidget, employeewidget
from modules import db


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
        self.next_page(auth)

    def start_register(self):
        register = registerdialog.RegisterDialog()
        self.next_page(register)

    def next_page(self, dialog):
        result = dialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            if dialog.next_tab == 'user':
                user = dialog.user
                self.parent().addWidget(
                    userwidget.UserWidget(user, None)
                )
            elif dialog.next_tab == 'employee':
                user = dialog.user
                self.parent().addWidget(
                    employeewidget.EmployeeWidget(user, None)
                )
            else:
                self.parent().addWidget(adminwidget.AdminWidget())
            self.parent().setCurrentIndex(self.parent().count() - 1)
