import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui.register import Ui_Dialog
from modules.usermanager import UserManager


class RegisterDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_controls()
        self.next_tab = 0
        self.user = None

    def init_controls(self):
        self.ui.regButton.clicked.connect(self.register)

    def register(self):
        user = self.ui.loginInput.text()
        password = self.ui.passInput.text()
        user_manager = UserManager()
        reg = None
        try:
            reg = user_manager.register(user, password, 'user')
        except Exception as e:
            QMessageBox.warning(
                self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
            )
        if reg:
            self.next_tab = 'user'
            self.user = user_manager.login(user, password)
            self.accept()
        else:
            QMessageBox.critical(
                self, 'Ошибка',
                'Ошибка при регистрации, попробуйте ещё раз!',
                QMessageBox.StandardButton.Ok
            )
