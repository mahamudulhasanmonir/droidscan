from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

class Sidebar(QWidget):
    def __init__(self, switch_page):
        super().__init__()
        self.buttons = {}
        self.setObjectName("Sidebar")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 22, 18, 22)
        layout.setSpacing(10)

        brand = QLabel("DroidScan")
        brand.setObjectName("SidebarTitle")
        layout.addWidget(brand)

        subtitle = QLabel("Navigation")
        subtitle.setObjectName("SidebarSubtitle")
        layout.addWidget(subtitle)

        buttons = [
            "Dashboard",
            "Device",
            "Hardware",
            "Apps",
            "Network",
            "Security",
            "Logs",
            "Tools",
        ]

        for name in buttons:
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.setObjectName("SidebarButton")
            btn.clicked.connect(lambda _, n=name: switch_page(n))
            layout.addWidget(btn)
            self.buttons[name] = btn

        layout.addStretch()

    def set_active(self, name):
        for page_name, button in self.buttons.items():
            button.setChecked(page_name == name)
