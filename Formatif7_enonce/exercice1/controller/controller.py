from PyQt6.QtCore import pyqtSignal, QObject


class TasksController(QObject):
    modelSet = pyqtSignal(object)

    def __init__(self, model, view,readonly_view):
        super().__init__()
        self.model = model
        self.view = view
        self.read_view = readonly_view

        self.view.tasksListView.setModel(self.model)
        self.view.itemClicked.connect(self.clicked)
        self.model.modelChanged.connect(self.update_read_view)

    def clicked(self, task_name):
        print("saafdasf ->", task_name)

    def update_read_view(self):
        total, done = self.model.tasks_count()
        self.read_view.update_summary(total, done)
