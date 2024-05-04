from PySide6 import QtCore, QtWidgets
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import (
    QAbstractItemView, QTableWidgetItem, QFileDialog, QMessageBox
)

from modules.db import Database
from ui.widget_records import Ui_recordsWidget
from modules.models import Record

STATUSES = {
    'pending': 'Отправлена',
    'accepted': 'Принята',
    'completed': 'Выполнена',
}


class RecordsWidget(QtWidgets.QWidget):
    def __init__(self, client, prev_index):
        super().__init__()
        self.ui = Ui_recordsWidget()
        self.ui.setupUi(self)
        self.db = Database()
        self.client = client
        self.model = Record
        self.prev_index = prev_index
        self.setup_table()
        self.update_table()
        self.setup_controls()

    def setup_table(self):
        self.ui.dataTable.setColumnCount(5)
        self.ui.dataTable.setHorizontalHeaderLabels(
            ['Услуга', 'Сотрудник', 'Дата', 'Статус', 'Отзыв']
        )
        for i in range(5):
            self.ui.dataTable.setColumnWidth(i, 900/5)
        self.ui.dataTable.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.ui.dataTable.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectItems
        )
        for field in self.model.fields:
            if field.verbose != 'Клиент':
                self.ui.searchBox.addItem(field.verbose)

    def setup_controls(self):
        self.ui.dataTable.cellDoubleClicked.connect(self.add_review)
        self.ui.searchField.textChanged.connect(self.search)
        if self.prev_index is not None:
            self.ui.buttonBack.clicked.connect(self.back)
        else:
            self.ui.buttonBack.hide()

    def add_review(self):
        pass

    def update_table(self, search=None):
        try:
            if not search:
                data = self.db.select(
                    f'select * from {self.model.view_name} '
                    f"where client_full_name = "
                    f"'{f'{self.client[1]} {self.client[2]}'}'"
                )
            else:
                field = self.model.view_fields[
                    self.ui.searchBox.currentIndex() + 1]
                data = self.db.select(
                    f'select * from {self.model.view_name} '
                    f"where client_full_name = "
                    f"'{f'{self.client[1]} {self.client[2]}'}' "
                    f'and CAST({field} AS VARCHAR) '
                    f"like '{search}%';"
                )
        except Exception as e:
            QMessageBox.warning(
                self, 'Ошибка', str(e), QMessageBox.StandardButton.Ok
            )
        print(data)
        self.ui.dataTable.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QTableWidgetItem(f'{data[row][col]}')
                item.setFlags(
                    QtCore.Qt.ItemFlag.ItemIsSelectable
                    | QtCore.Qt.ItemFlag.ItemIsEnabled
                )
                self.ui.dataTable.setItem(row, col, item)

    def search(self):
        if self.ui.searchBox.currentIndex() >= 0:
            self.update_table(self.ui.searchField.text())

    def back(self):
        self.parent().setCurrentIndex(self.prev_index)
        self.parent().removeWidget(self)
        del self