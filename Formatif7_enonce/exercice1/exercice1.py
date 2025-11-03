import sys
import traceback

from PyQt6.QtWidgets import QApplication
from controller.controller import TasksController
from view.view import TasksView
from view.readonly_view import TasksReadOnlyView
from model.model import TasksModel

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

if __name__ == "__main__":
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)

    model = TasksModel()
    view = TasksView()
    readonly_view = TasksReadOnlyView()
    controller = TasksController(model, view,readonly_view)

    view.show()
    readonly_view.show()
    sys.exit(app.exec())
