from PyQt6.QtWidgets import QLabel, QTabWidget, QVBoxLayout, QWidget
from gui.components.table import AppsTable


class AppsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(16)

        self.title = QLabel("Installed applications")
        self.title.setObjectName("PageTitle")
        self.layout.addWidget(self.title)

        self.summary = QLabel("A full scan is needed to list installed apps.")
        self.summary.setObjectName("HeroSubtitle")
        self.summary.setWordWrap(True)
        self.layout.addWidget(self.summary)

        self.tabs = QTabWidget()
        self.tabs.setObjectName("DataTabs")
        self.user_table = AppsTable()
        self.system_table = AppsTable()
        self.tabs.addTab(self.user_table, "User Apps")
        self.tabs.addTab(self.system_table, "System Apps")
        self.layout.addWidget(self.tabs)

    def update_data(self, data):
        apps_data = data.get("Apps", {})
        user_apps = apps_data.get("User Apps", [])
        system_apps = apps_data.get("System Apps", [])

        self.user_table.load_data(user_apps)
        self.system_table.load_data(system_apps)

        total = apps_data.get("Total Apps", len(user_apps) + len(system_apps))
        if apps_data:
            self.summary.setText(
                f"Showing {len(user_apps)} user apps and {len(system_apps)} system apps from {total} detected packages."
            )
        else:
            self.summary.setText("A quick scan does not collect app packages. Run a full scan to populate this page.")
