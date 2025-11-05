from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.uic import loadUi


class TasksReadOnlyView(QWidget):
    label: QLabel

    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksReadOnlyView.ui", self)

    def update_summary(self, total, done):
        self.label.setText(f"Nombre de taches : {total} dont {done} sont effectuées")
