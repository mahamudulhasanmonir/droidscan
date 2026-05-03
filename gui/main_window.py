import json
import os

from PyQt6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from gui.sidebar import Sidebar
from gui.pages.dashboard import DashboardPage
from gui.pages.details import KeyValuePage, TextDumpPage
from gui.pages.apps import AppsPage
from gui.pages.tools import ToolsPage
from gui.tool_worker import ToolWorker
from gui.worker import ScanWorker


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DroidScan")
        self.resize(1280, 800)

        self.report = {}
        self.worker = None

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        self.sidebar = Sidebar(self.switch_page)
        main_layout.addWidget(self.sidebar)

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(16)

        header_card = QFrame()
        header_card.setObjectName("TopBarCard")
        top = QHBoxLayout(header_card)
        top.setContentsMargins(20, 18, 20, 18)
        top.setSpacing(14)

        self.status = QLabel("Ready")
        self.status.setObjectName("StatusLabel")
        self.progress_label = QLabel("Idle")
        self.progress_label.setObjectName("MutedLabel")
        title = QLabel("Android Device Scanner")
        title.setObjectName("HeroTitle")
        subtitle = QLabel("Run a quick overview or full forensic-style scan from one dashboard.")
        subtitle.setObjectName("HeroSubtitle")

        title_stack = QVBoxLayout()
        title_stack.setContentsMargins(0, 0, 0, 0)
        title_stack.setSpacing(2)
        title_stack.addWidget(title)
        title_stack.addWidget(subtitle)

        self.quick_btn = QPushButton("Quick Scan")
        self.full_btn = QPushButton("Full Scan")
        self.export_btn = QPushButton("Export")
        self.export_btn.setObjectName("GhostButton")
        self.export_btn.setEnabled(False)

        top.addLayout(title_stack, 1)
        top.addWidget(self.status)
        top.addWidget(self.progress_label)
        top.addStretch()
        top.addWidget(self.quick_btn)
        top.addWidget(self.full_btn)
        top.addWidget(self.export_btn)

        right_layout.addWidget(header_card)

        self.quick_btn.clicked.connect(lambda: self.start_scan("quick"))
        self.full_btn.clicked.connect(lambda: self.start_scan("full"))
        self.export_btn.clicked.connect(self.export_report)

        self.pages = QStackedWidget()
        self.pages.setObjectName("ContentStack")

        self.dashboard = DashboardPage()
        self.device_page = KeyValuePage("Device details", empty_message="Run a scan to load device properties.")
        self.hardware_page = TextDumpPage("Hardware details", empty_message="Run a scan to inspect CPU, memory, and battery output.")
        self.apps = AppsPage()
        self.network_page = TextDumpPage("Network details", empty_message="Full scan data will appear here.")
        self.security_page = KeyValuePage("Security details", empty_message="Full scan data will appear here.")
        self.logs_page = TextDumpPage("Logs", empty_message="Full scan data will appear here.", monospace=True)
        self.tools_page = ToolsPage(self.run_tool_action)

        self.page_map = {
            "Dashboard": self.dashboard,
            "Device": self.device_page,
            "Hardware": self.hardware_page,
            "Apps": self.apps,
            "Network": self.network_page,
            "Security": self.security_page,
            "Logs": self.logs_page,
            "Tools": self.tools_page,
        }

        for page in self.page_map.values():
            self.pages.addWidget(page)

        right_layout.addWidget(self.pages)
        right_layout.setStretchFactor(self.pages, 1)

        main_layout.addLayout(right_layout)
        main_layout.setStretchFactor(right_layout, 1)
        self.setLayout(main_layout)

        self.switch_page("Dashboard")
        self.load_cached_report()

    def switch_page(self, name):
        page = self.page_map.get(name, self.dashboard)
        self.pages.setCurrentWidget(page)
        self.sidebar.set_active(name)

    def start_scan(self, mode):
        if self.worker and self.worker.isRunning():
            return

        self.quick_btn.setEnabled(False)
        self.full_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.status.setText("Scanning...")
        self.progress_label.setText("Starting...")

        self.worker = ScanWorker(mode)
        self.worker.finished.connect(self.update_ui)
        self.worker.progress.connect(self.update_progress)
        self.worker.error.connect(self.handle_scan_error)
        self.worker.start()

    def update_progress(self, text):
        self.progress_label.setText(f"Scanning: {text}")

    def update_ui(self, data):
        self.report = data
        self.status.setText("Done")
        self.progress_label.setText("Completed")
        self.quick_btn.setEnabled(True)
        self.full_btn.setEnabled(True)
        self.export_btn.setEnabled(True)

        self.dashboard.update_data(data)
        self.device_page.update_data(data.get("Device", {}))
        self.hardware_page.update_data(data.get("Hardware", {}))
        self.apps.update_data(data)
        self.network_page.update_data(data.get("Network", {}))
        self.security_page.update_data(data.get("Security", {}))
        self.logs_page.update_data(data.get("Logs", {}))
        self.tools_page.set_status("Scan complete. Tools are ready.")

    def export_report(self):
        if not self.report:
            self.status.setText("No data to export")
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Export report",
            os.path.abspath("report.json"),
            "JSON Files (*.json)",
        )
        if not path:
            self.status.setText("Export cancelled")
            return

        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.report, f, indent=4)

        txt_path = os.path.splitext(path)[0] + ".txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            for section, data in self.report.items():
                f.write(f"=== {section} ===\n{data}\n\n")

        self.status.setText("Exported JSON + TXT")

    def handle_scan_error(self, message):
        self.status.setText("Scan failed")
        self.progress_label.setText(message)
        self.quick_btn.setEnabled(True)
        self.full_btn.setEnabled(True)
        self.export_btn.setEnabled(bool(self.report))

    def load_cached_report(self):
        report_path = os.path.abspath("report.json")
        if not os.path.exists(report_path):
            return

        try:
            with open(report_path, "r", encoding="utf-8") as f:
                cached = json.load(f)
        except (OSError, json.JSONDecodeError):
            return

        self.report = cached
        self.status.setText("Loaded report")
        self.progress_label.setText("Showing cached data")
        self.export_btn.setEnabled(True)
        self.dashboard.update_data(cached)
        self.device_page.update_data(cached.get("Device", {}))
        self.hardware_page.update_data(cached.get("Hardware", {}))
        self.apps.update_data(cached)
        self.network_page.update_data(cached.get("Network", {}))
        self.security_page.update_data(cached.get("Security", {}))
        self.logs_page.update_data(cached.get("Logs", {}))
        self.tools_page.set_status("Cached report loaded. Tools are ready.")

    def run_tool_action(self, action):
        if hasattr(self, "tool_worker") and self.tool_worker and self.tool_worker.isRunning():
            return

        self.status.setText("Running tool...")
        self.progress_label.setText(action.replace("_", " ").title())
        self.tools_page.set_busy(True)
        self.tools_page.set_status("Running selected tool...")

        self.tool_worker = ToolWorker(action)
        self.tool_worker.finished.connect(self.handle_tool_result)
        self.tool_worker.error.connect(self.handle_tool_error)
        self.tool_worker.start()

    def handle_tool_result(self, action, result):
        self.status.setText("Tool completed")
        self.progress_label.setText("Idle")
        self.tools_page.set_busy(False)
        self.tools_page.show_result(action.replace("_", " ").title(), result)

    def handle_tool_error(self, message):
        self.status.setText("Tool failed")
        self.progress_label.setText("Idle")
        self.tools_page.set_busy(False)
        self.tools_page.show_result("Tool error", message)
