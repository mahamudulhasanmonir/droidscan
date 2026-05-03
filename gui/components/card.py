from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout

class Card(QFrame):
    def __init__(self, title, value):
        super().__init__()
        self.setObjectName("SummaryCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 16, 18, 16)
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")

        value_label = QLabel(str(value).strip() or "-")
        value_label.setObjectName("CardValue")
        value_label.setWordWrap(True)
        value_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
