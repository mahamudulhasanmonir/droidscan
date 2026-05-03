from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QTabWidget, QLabel, QHBoxLayout, QApplication
)
from PyQt6.QtCore import Qt
import json

from core.device import detect_mode
from gui.worker import ScanWorker

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DroidScan")
        self.resize(900, 600)

        layout = QVBoxLayout()

        # Top Bar
        top_bar = QHBoxLayout()
        self.status_label = QLabel("Status: Not Connected")
        self.scan_btn = QPushButton("Scan Device")

        top_bar.addWidget(self.status_label)
        top_bar.addStretch()
        top_bar.addWidget(self.scan_btn)

        layout.addLayout(top_bar)

        # Tabs
        self.tabs = QTabWidget()
        self.text_areas = {}

        for tab in ["Device", "Hardware", "Apps", "Network", "Security", "Logs"]:
            text = QTextEdit()
            text.setReadOnly(True)
            self.tabs.addTab(text, tab)
            self.text_areas[tab] = text

        layout.addWidget(self.tabs)

        # Bottom Buttons
        bottom_bar = QHBoxLayout()
        self.export_btn = QPushButton("Export JSON")
        self.clear_btn = QPushButton("Clear")

        bottom_bar.addWidget(self.export_btn)
        bottom_bar.addWidget(self.clear_btn)

        layout.addLayout(bottom_bar)

        self.setLayout(layout)

        # Events
        self.scan_btn.clicked.connect(self.scan_device)
        self.clear_btn.clicked.connect(self.clear_output)
        self.export_btn.clicked.connect(self.export_json)

        self.report = {}

        self.check_device()

    def check_device(self):
        mode = detect_mode()
        self.status_label.setText(f"Status: {mode}")

    def scan_device(self):
        self.status_label.setText("Scanning...")
        self.worker = ScanWorker()
        self.worker.finished.connect(self.display_data)
        self.worker.start()

    def display_data(self, data):
        self.report = data
        self.status_label.setText("Scan Complete")

        for key, value in data.items():
            if key in self.text_areas:
                formatted = json.dumps(value, indent=2)
                self.text_areas[key].setText(formatted)

    def clear_output(self):
        for text in self.text_areas.values():
            text.clear()

    def export_json(self):
        with open("report.json", "w") as f:
            json.dump(self.report, f, indent=4)