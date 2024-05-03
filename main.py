import sys

from PySide6 import QtWidgets

from ui.form import Ui_MainWindow
from widgets import welcomewidget, adminwidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_controls()
        self.setup_wigdets()

    def setup_controls(self):
        self.actionExit.triggered.connect(self.close)

    def setup_wigdets(self):
        self.stackedWidget.addWidget(welcomewidget.WelcomeWidget())
        self.stackedWidget.addWidget(adminwidget.AdminWidget())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
