from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from modules import db
from ui.services import Ui_servicesDialog


class ServicesDialog(QtWidgets.QDialog):
    def __init__(self, employee):
        super().__init__()
        self.db = db.Database()
        self.ui = Ui_servicesDialog()
        self.ui.setupUi(self)
        self.employee = employee
        self.services = None
        self.items = []
        self.setup_controls()
        self.update_data()

    def setup_controls(self):
        self.ui.buttonAdd.clicked.connect(self.add)
        self.ui.buttonRemove.clicked.connect(self.remove)
        self.ui.buttonSave.clicked.connect(self.save)

    def update_data(self):
        self.services = self.db.select(
            'select service_id, name from service;'
        )
        my_services = self.db.select(
            f'select service_id, name from service '
            f'where service_id in('
            f'select service_id from service_employee '
            f'where employee_id = {self.employee[0]});'
        )
        for my_service in my_services:
            item = self.new_item()
            item.setCurrentText(my_service[1])
            self.items.append(item)
            self.ui.listBox.addWidget(item)

    def new_item(self):
        item = QtWidgets.QComboBox(self)
        for service in self.services:
            item.addItem(service[1])
        return item

    def add(self):
        item = self.new_item()
        self.items.append(item)
        self.ui.listBox.addWidget(item)

    def remove(self):
        if len(self.items) > 0:
            self.items[-1].hide()
            del self.items[-1]

    def get_id(self, name):
        return self.db.select(
            f'select service_id from service '
            f"where name = '{name}';"
        )[0][0]

    def save(self):
        new_services = set([self.get_id(item.currentText()) for item in self.items])
        self.db.execute(
            f'delete from service_employee '
            f'where employee_id = {self.employee[0]}'
        )
        for service_id in new_services:
            try:
                self.db.execute(
                    f'insert into service_employee '
                    f'(employee_id, service_id) '
                    f'values ({self.employee[0]}, {service_id});'
                )
            except Exception as e:
                QMessageBox.warning(
                    self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
                )
        self.accept()
