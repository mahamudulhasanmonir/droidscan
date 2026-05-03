from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QVBoxLayout, QWidget
from gui.components.card import Card


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(16)

        self.title = QLabel("Scan overview")
        self.title.setObjectName("PageTitle")
        self.layout.addWidget(self.title)

        self.summary = QLabel("Run a scan to populate your device summary.")
        self.summary.setObjectName("HeroSubtitle")
        self.summary.setWordWrap(True)
        self.layout.addWidget(self.summary)

        self.grid = QGridLayout()
        self.grid.setSpacing(14)
        self.layout.addLayout(self.grid)
        self.layout.addStretch()

    def update_data(self, data):
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        device = data.get("Device", {})
        apps = data.get("Apps", {})
        security = data.get("Security", {})
        network = data.get("Network", {})

        cards = [
            ("Model", device.get("Model", "-")),
            ("Android", device.get("Android Version", "-")),
            ("Brand", device.get("Brand", "-")),
            ("Serial", device.get("Serial", "-")),
            ("User Apps", len(apps.get("User Apps", [])) if apps else 0),
            ("SELinux", security.get("SELinux", "-") if security else "-"),
        ]

        if network:
            cards.append(("Network", "Available"))

        for index, (title, value) in enumerate(cards):
            row, column = divmod(index, 3)
            self.grid.addWidget(Card(title, value), row, column)

        mode = "full" if "Security" in data or "Logs" in data else "quick"
        self.summary.setText(
            f"Showing {mode} scan results with {len(data)} sections loaded."
        )
        self.summary.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
