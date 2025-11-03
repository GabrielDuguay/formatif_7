from asyncio import tasks

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QMainWindow, QListView
from PyQt6.uic import loadUi


class TasksView(QMainWindow):
    tasksListView:QListView
    itemClicked: pyqtSignal(str)

    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksView.ui", self)
        self.tasksListView.clicked.connect(self._relay_click)

    def _relay_click(self, index):
        value = index.data(Qt.ItemDataRole.UserRole)
        self.itemClicked.emit(value)