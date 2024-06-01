from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QAbstractItemView, QTableWidgetItem

from modules import db
from ui.widget_employee import Ui_employeeWidget
from dialogs import passworddialog, servicesdialog


class EmployeeWidget(QtWidgets.QWidget):
    def __init__(self, user, employee):
        super().__init__()
        self.ui = Ui_employeeWidget()
        self.ui.setupUi(self)
        self.user = user
        self.employee = employee
        self.selected_table = None
        self.pending = None
        self.completed = None
        self.db = db.Database()
        self.setup_controls()
        self.setup_tables()
        self.update_employee()
        self.update_data()

    def setup_tables(self):
        for table in [self.ui.pendingTable, self.ui.completedTable]:
            table.setColumnCount(6)
            table.setHorizontalHeaderLabels([
                'Клиент', 'Сотрудник', 'Услуга',
                'Дата', 'Отзыв', 'Статус'
            ])
            for i in range(6):
                table.setColumnWidth(
                    i, 700 / 6 - 3
                )
            table.setSelectionMode(
                QAbstractItemView.SelectionMode.SingleSelection
            )
            table.setSelectionBehavior(
                QAbstractItemView.SelectionBehavior.SelectRows
            )

    def setup_controls(self):
        self.ui.buttonAccept.clicked.connect(self.accept)
        self.ui.buttonComplete.clicked.connect(self.complete)
        self.ui.buttonServices.clicked.connect(self.change_services)
        self.ui.buttonPassword.clicked.connect(self.change_password)
        self.ui.pendingTable.cellClicked.connect(self.select_pending)
        self.ui.completedTable.cellClicked.connect(self.select_completed)

    def update_employee(self):
        try:
            self.employee = db.Database().select(
                f'select * from employee where users_id = {self.user[0]};'
            )[0]
        except IndexError:
            self.employee = None
        if self.employee is not None:
            self.ui.label.setText(
                f'Сотрудник {self.employee[1]} {self.employee[2]}'
            )

    def select_pending(self):
        self.selected_table = self.ui.pendingTable
        self.check_state()

    def select_completed(self):
        self.selected_table = self.ui.completedTable
        self.check_state()

    def check_state(self):
        state = self.selected_table.item(
            self.selected_table.currentRow(), 5).text()
        self.ui.buttonAccept.setEnabled(state == 'pending')
        self.ui.buttonComplete.setEnabled(state == 'accepted')

    def update_data(self):
        services = self.db.select(
            f'select name from service '
            f'where service_id in('
            f'select service_id from service_employee '
            f'where employee_id = {self.employee[0]});'
        )
        services = [x[0] for x in services]
        self.pending = self.db.select(
            f'select * from record_view '
            f"where service_name in ('{"', '".join(services)}') "
            f"and status = 'pending';"
        )
        self.completed = self.db.select(
            f'select * from record_view '
            f"where employee_full_name = "
            f"'{self.employee[1]} {self.employee[2]}';"
        )
        for data, table in [(self.pending, self.ui.pendingTable),
                            (self.completed, self.ui.completedTable)]:
            table.setRowCount(len(data))
            for row in range(len(data)):
                for col in range(len(data[row]) - 1):
                    item = QTableWidgetItem(f'{data[row][col + 1]}')
                    item.setFlags(
                        QtCore.Qt.ItemFlag.ItemIsSelectable
                        | QtCore.Qt.ItemFlag.ItemIsEnabled
                    )
                    table.setItem(row, col, item)

    def accept(self):
        row = self.selected_table.currentRow()
        self.db.execute(f'update record set '
                        f"status = 'accepted', "
                        f"employee_id = {self.employee[0]} "
                        f"where record_id = {self.pending[row][0]};")
        client = self.db.select(f'select client_id from record '
                                f'where record_id = {self.pending[row][0]};')
        self.db.execute(
            f"insert into mail(text, receiver)"
            f"values(e'Ваша заявка №{self.pending[row][0]} была принята.\n"
            f"Сотрудник - {self.employee[1]} {self.employee[2]}', "
            f"{client[0][0]})"
        )
        self.update_data()

    def complete(self):
        row = self.selected_table.currentRow()
        self.db.execute(f'update record set '
                        f"status = 'completed' "
                        f"where record_id = {self.completed[row][0]};")
        client = self.db.select(f'select client_id from record '
                                f'where record_id = {self.completed[row][0]};')
        self.db.execute(
            f"insert into mail(text, receiver)"
            f"values(e'Ваша заявка №{self.pending[row][0]} была выполнена.\n"
            f"Сотрудник - {self.employee[1]} {self.employee[2]}', "
            f"{client[0][0]})"
        )
        self.update_data()

    def change_services(self):
        dialog = servicesdialog.ServicesDialog(self.employee)
        result = dialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            self.update_data()

    def change_password(self):
        dialog = passworddialog.PasswordDialog(self.user)
        dialog.exec()

