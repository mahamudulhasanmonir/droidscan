from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class _BaseScrollPage(QWidget):
    def __init__(self, title, empty_message):
        super().__init__()
        self.empty_message = empty_message

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(14)

        self.title = QLabel(title)
        self.title.setObjectName("PageTitle")
        self.content_layout.addWidget(self.title)

        self.empty_label = QLabel(empty_message)
        self.empty_label.setObjectName("EmptyState")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setWordWrap(True)
        self.empty_label.setMinimumHeight(220)
        self.content_layout.addWidget(self.empty_label)
        self.body = QVBoxLayout()
        self.body.setContentsMargins(0, 0, 0, 0)
        self.body.setSpacing(14)
        self.content_layout.addLayout(self.body)
        self.content_layout.addStretch()
        scroll.setWidget(self.content)
        root.addWidget(scroll)

    def clear_content(self):
        while self.body.count():
            item = self.body.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def set_empty(self, visible):
        self.empty_label.setVisible(visible)


class KeyValuePage(_BaseScrollPage):
    def __init__(self, title, empty_message="No data available."):
        super().__init__(title, empty_message)

    def update_data(self, data):
        self.clear_content()
        if not data:
            self.set_empty(True)
            return

        self.set_empty(False)
        for key, value in data.items():
            card = QFrame()
            card.setObjectName("InfoCard")
            layout = QHBoxLayout(card)
            layout.setContentsMargins(18, 16, 18, 16)
            layout.setSpacing(16)

            key_label = QLabel(str(key))
            key_label.setObjectName("CardTitle")
            key_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)

            value_label = QLabel(str(value).strip() or "-")
            value_label.setObjectName("CardValue")
            value_label.setWordWrap(True)
            value_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

            layout.addWidget(key_label)
            layout.addWidget(value_label, 1)
            self.body.addWidget(card)


class TextDumpPage(_BaseScrollPage):
    def __init__(self, title, empty_message="No data available.", monospace=False):
        super().__init__(title, empty_message)
        self.monospace = monospace

    def update_data(self, data):
        self.clear_content()
        if not data:
            self.set_empty(True)
            return

        self.set_empty(False)
        for key, value in data.items():
            block = QFrame()
            block.setObjectName("InfoCard")
            layout = QVBoxLayout(block)
            layout.setContentsMargins(18, 16, 18, 16)
            layout.setSpacing(10)

            title = QLabel(str(key))
            title.setObjectName("CardTitle")

            editor = QTextEdit()
            editor.setReadOnly(True)
            editor.setPlainText(str(value).strip() or "-")
            editor.setMinimumHeight(170)
            if self.monospace:
                font = QFont("Consolas")
                font.setStyleHint(QFont.StyleHint.Monospace)
                editor.setFont(font)

            layout.addWidget(title)
            layout.addWidget(editor)
            self.body.addWidget(block)
