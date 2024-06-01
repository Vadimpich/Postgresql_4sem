from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QPropertyAnimation, QSize
from PySide6.QtGui import QColor

from modules import db
from ui.widget_user import Ui_clientWidget
from widgets import userinfowidget, widgetnewrecord, recordswidget, mailwidget
from dialogs import passworddialog


class UserWidget(QtWidgets.QWidget):
    def __init__(self, user, client):
        super().__init__()
        self.animation = None
        self.ui = Ui_clientWidget()
        self.ui.setupUi(self)
        self.db = db.Database()
        self.user = user
        self.client = client
        self.setup_controls()
        self.update_client()
        self.check_mail()

    def setup_controls(self):
        self.ui.buttonNew.clicked.connect(self.new_record)
        self.ui.buttonRecords.clicked.connect(self.my_records)
        self.ui.buttonInfo.clicked.connect(self.change_info)
        self.ui.buttonPassword.clicked.connect(self.change_password)
        self.ui.buttonMail.clicked.connect(self.show_mail)

    def new_record(self):
        self.parent().addWidget(
            widgetnewrecord.NewRecordWidget(
                self.client, self.parent().currentIndex()
            )
        )
        self.parent().setCurrentIndex(self.parent().count() - 1)

    def my_records(self):
        self.parent().addWidget(
            recordswidget.RecordsWidget(
                self.client, self.parent().currentIndex()
            )
        )
        self.parent().setCurrentIndex(self.parent().count() - 1)

    def change_info(self):
        self.parent().addWidget(
            userinfowidget.UserInfoWidget(
                self.user, self.client, self.parent().currentIndex()
            )
        )
        self.parent().setCurrentIndex(self.parent().count() - 1)

    def update_client(self):
        try:
            self.client = self.db.select(
                f'select * from client where users_id = {self.user[0]};'
            )[0]
        except IndexError:
            print('error')
            self.client = None
        if self.client is not None:
            self.ui.label.setText(f'{self.client[1]} {self.client[2]}')
            self.ui.buttonMail.setEnabled(True)
            self.ui.buttonNew.setEnabled(True)
            self.ui.buttonRecords.setEnabled(True)

    def change_password(self):
        dialog = passworddialog.PasswordDialog(self.user)
        dialog.exec()

    def show_mail(self):
        self.parent().addWidget(
            mailwidget.MailWidget(
                self.client,
                self.parent().currentIndex()
            )
        )
        self.parent().setCurrentIndex(self.parent().count() - 1)

    def check_mail(self):
        if self.client is not None:
            mail = self.db.select(
                f'select * from mail '
                f'where receiver = {self.client[0]} '
                f'and seen = false;'
            )
            print(len(mail))
            # if len(mail) > 0:
            #     self.animation = QPropertyAnimation(
            #         self.ui.buttonMail,
            #         b'color'
            #     )
            #     self.animation.setDuration(2000)
            #     self.animation.setStartValue(self.palette().button().color)
            #     self.animation.setEndValue(QColor(175, 50, 50))
            #     self.animation.setLoopCount(-1)
            #     self.animation.start()
