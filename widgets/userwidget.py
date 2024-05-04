from PySide6 import QtWidgets

from modules import db
from ui.widget_user import Ui_clientWidget
from widgets import userinfowidget, widgetnewrecord, recordswidget


class UserWidget(QtWidgets.QWidget):
    def __init__(self, user, client):
        super().__init__()
        self.ui = Ui_clientWidget()
        self.ui.setupUi(self)
        self.user = user
        self.client = client
        self.setup_controls()
        self.update_client()

    def setup_controls(self):
        self.ui.buttonNew.clicked.connect(self.new_record)
        self.ui.buttonRecords.clicked.connect(self.my_records)
        self.ui.buttonInfo.clicked.connect(self.change_info)
        self.ui.buttonPassword.clicked.connect(self.change_password)

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
            self.client = db.Database().select(
                f'select * from client where user_id = {self.user[0]};'
            )[0]
        except IndexError:
            print('error')
            self.client = None
        if self.client is not None:
            self.ui.label.setText(f'{self.client[1]} {self.client[2]}')
            self.ui.buttonNew.setEnabled(True)
            self.ui.buttonRecords.setEnabled(True)

    def change_password(self):
        pass
