import sys

from PySide6 import QtWidgets

from ui.auth import Ui_Dialog
from modules.usermanager import UserManager


class AuthDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_controls()
        self.next_tab = 0
        self.user = None

    def init_controls(self):
        self.ui.loginButton.clicked.connect(self.check_login)

    def check_login(self):
        user = self.ui.loginInput.text()
        password = self.ui.passInput.text()
        user_manager = UserManager()
        user = user_manager.login(user, password)
        if user:
            self.next_tab = user[3]
            self.user = user
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(
                self, 'Ошибка', 'Введён неправильный логин или пароль!'
            )
            self.ui.passInput.setText('')
