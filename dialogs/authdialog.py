import sys

from PySide6 import QtWidgets

from ui.auth import Ui_Dialog
from modules.usermanager import UserManager


def msgbox(text):
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.exec()


class AuthDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_controls()
        self.next_tab = 0

    def init_controls(self):
        self.ui.loginButton.clicked.connect(self.check_login)

    def check_login(self):
        # user = self.ui.loginInput.text()
        # password = self.ui.passInput.text()
        #
        # user_manager = UserManager()
        #
        # if user_manager.login(user, password):
        #     msgbox('Login successful')
        # else:
        #     msgbox('Login failed')
        self.next_tab = 1
        self.close()
