import sys

from PySide6 import QtWidgets

from ui.register import Ui_Dialog
from modules.usermanager import UserManager


def msgbox(text):
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.exec()


class RegisterDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_controls()
        self.next_tab = 0

    def init_controls(self):
        self.ui.regButton.clicked.connect(self.check_login)

    def check_login(self):
        user = self.ui.loginInput.text()
        password = self.ui.passInput.text()
        user_manager = UserManager()

        if user_manager.login(user, password):
            msgbox('Login successful')
        else:
            msgbox('Login failed')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = RegisterDialog()
    dialog.show()
    sys.exit(app.exec())
