from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget


class ToolsPage(QWidget):
    def __init__(self, trigger_action):
        super().__init__()
        self.trigger_action = trigger_action
        self.buttons = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("Device tools")
        title.setObjectName("PageTitle")
        layout.addWidget(title)

        description = QLabel(
            "Quick device actions for connected phones. Reboot actions require a device in the matching mode."
        )
        description.setObjectName("HeroSubtitle")
        description.setWordWrap(True)
        layout.addWidget(description)

        grid = QGridLayout()
        grid.setSpacing(12)

        actions = [
            ("Refresh Connection", "refresh_mode"),
            ("Read HW Info", "read_hw_info"),
            ("Reboot Normal", "reboot_normal"),
            ("Reboot Fastboot", "reboot_fastboot"),
            ("Reboot to EDL", "reboot_edl"),
        ]

        for index, (label, action) in enumerate(actions):
            button = QPushButton(label)
            button.clicked.connect(lambda _, name=action: self.trigger_action(name))
            grid.addWidget(button, index // 2, index % 2)
            self.buttons[action] = button

        layout.addLayout(grid)

        self.status = QLabel("No tool action started yet.")
        self.status.setObjectName("MutedLabel")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Tool output will appear here.")
        layout.addWidget(self.output)

    def set_busy(self, busy):
        for button in self.buttons.values():
            button.setEnabled(not busy)

    def set_status(self, text):
        self.status.setText(text)

    def show_result(self, title, text):
        self.status.setText(title)
        self.output.setPlainText(text)
