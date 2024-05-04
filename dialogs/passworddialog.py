from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from modules.usermanager import UserManager
from ui.password import Ui_Dialog


class PasswordDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_controls()
        self.next_tab = 0
        self.user = user

    def init_controls(self):
        self.ui.editButton.clicked.connect(self.change_passsword)

    def change_passsword(self):
        user_manager = UserManager()
        password = self.ui.passInput.text()
        if password == self.ui.confirmInput.text():
            try:
                user_manager.change_password(self.user[1], password)
            except Exception as e:
                QMessageBox.warning(
                    self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
                )
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Ошибка',
                'Пароли не совпадают!',
                QMessageBox.StandardButton.Ok
            )

