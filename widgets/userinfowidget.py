from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui.widget_userinfo import Ui_userInfoWidget
from modules.db import Database


class UserInfoWidget(QtWidgets.QWidget):
    def __init__(self, user, client, prev_index):
        super().__init__()
        self.ui = Ui_userInfoWidget()
        self.ui.setupUi(self)
        self.user = user
        self.client = client
        self.prev_index = prev_index
        self.db = Database()
        self.setup_controls()

    def setup_controls(self):
        self.ui.buttonSave.clicked.connect(self.save_user)

    def save_user(self):
        try:
            if self.client is not None:
                self.db.insert(
                    f"update client set "
                    f"first_name = '{self.ui.nameField.text()}', "
                    f"last_name = '{self.ui.surnameField.text()}', "
                    f"phone_number = '{self.ui.phoneField.text()}', "
                    f"address = '{self.ui.addressField.text()}' "
                    f"where client_id = {self.client[0]};"
                )
            else:
                self.db.insert(
                    f"insert into client "
                    f"(first_name, last_name, phone_number, address, user_id)"
                    f"values ('{self.ui.nameField.text()}', "
                    f"'{self.ui.surnameField.text()}', "
                    f"'{self.ui.phoneField.text()}', "
                    f"'{self.ui.addressField.text()}', "
                    f"'{self.user[0]}');"
                )
        except Exception as e:
            QMessageBox.warning(
                self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
            )
        self.parent().setCurrentIndex(self.prev_index)
        self.parent().removeWidget(self)
        self.parent().widget(self.prev_index).update_client()
        del self


