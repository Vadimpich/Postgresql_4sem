from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox

from modules.db import Database
from ui.widget_new_record import Ui_newRecordWidget


class NewRecordWidget(QtWidgets.QWidget):
    def __init__(self, client, prev_index):
        super().__init__()
        self.ui = Ui_newRecordWidget()
        self.ui.setupUi(self)
        self.client = client
        self.prev_index = prev_index
        self.db = Database()
        self.setup_controls()
        self.setup_form()

    def setup_controls(self):
        self.ui.buttonSave.clicked.connect(self.save_record)

    def setup_form(self):
        for service in self.db.select('select name from service'):
            self.ui.serviceBox.addItem(service[0])
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    def save_record(self):
        try:
            self.db.execute(
                f"insert into record (client_id, service_id, date) "
                f"values ("
                f"{self.client[0]}, "
                f"{self.service_id()}, "
                f"'{self.ui.dateEdit.date().toString('dd-MM-yyyy')}');"

            )
        except Exception as e:
            QMessageBox.warning(
                self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
            )
        self.parent().setCurrentIndex(self.prev_index)
        self.parent().removeWidget(self)
        self.parent().widget(self.prev_index).update_client()
        del self

    def service_id(self):
        return self.db.select(
            f"select service_id from service "
            f"where name = '{self.ui.serviceBox.currentText()}'"
        )[0][0]
