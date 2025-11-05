from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt, pyqtSignal


class TasksModel(QAbstractListModel):
    __tasks:dict[str,bool]
    modelChanged = pyqtSignal()

    def __init__(self):

        super().__init__()
        self.__tasks={"tache 1":True, "tache 2": False,"autre tache" :False }

    def rowCount(self, parent =QModelIndex()):
        return len(self.__tasks)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        task = list(self.__tasks.keys())[index.row()]  #On cast en list parce que a la base c'est autre chose... pour accéder a un objet
        if role == Qt.ItemDataRole.DisplayRole:
            return task.__str__()
        elif role == Qt.ItemDataRole.UserRole:
            return task
        return None

    def notify_loaded(self):
        self.modelChanged.emit()

    def tasks_count(self):
        total = len(self.__tasks)
        done = sum(1 for done in self.__tasks.values() if done)
        return total, done
