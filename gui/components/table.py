from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem

class AppsTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(1)
        self.setHorizontalHeaderLabels(["Package Name"])
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def load_data(self, apps):
        self.setRowCount(len(apps))
        for i, app in enumerate(apps):
            self.setItem(i, 0, QTableWidgetItem(app))
