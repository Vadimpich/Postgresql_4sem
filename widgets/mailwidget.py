from PySide6 import QtWidgets

from modules import db
from ui.widget_mail import Ui_mailWidget
from widgets.notificationwidget import NotificationWidget


class MailWidget(QtWidgets.QWidget):
    def __init__(self, client, prev_index):
        super().__init__()
        self.ui = Ui_mailWidget()
        self.ui.setupUi(self)
        self.db = db.Database()
        self.client = client
        self.prev_index = prev_index
        self.update_mail()
        self.ui.buttonBack.clicked.connect(self.back)

    def update_mail(self):
        mail = self.db.select(
            f'select * from mail '
            f'where receiver = {self.client[0]} '
            f'order by date desc'
        )
        for notification in mail:
            widget = NotificationWidget(notification)
            self.ui.mailBox.addWidget(widget)
        self.db.execute(
            f'update mail set seen = true where receiver = {self.client[0]};',
        )

    def back(self):
        self.parent().setCurrentIndex(self.prev_index)
        self.parent().removeWidget(self)
        del self
