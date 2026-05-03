from PyQt6.QtCore import QThread, pyqtSignal

# ✅ IMPORT SCANNERS
from scanners.device_info import get_device_info
from scanners.hardware import get_hardware_info
from scanners.apps import get_apps
from scanners.network import get_network_info
from scanners.security import get_security_info
from scanners.logs import get_logs


class ScanWorker(QThread):
    finished = pyqtSignal(dict)
    progress = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, mode="quick"):
        super().__init__()
        self.mode = mode

    def run(self):
        report = {}
        try:
            self.progress.emit("Device Info")
            report["Device"] = get_device_info()

            self.progress.emit("Hardware")
            report["Hardware"] = get_hardware_info()

            if self.mode == "full":
                self.progress.emit("Apps")
                report["Apps"] = get_apps()

                self.progress.emit("Network")
                report["Network"] = get_network_info()

                self.progress.emit("Security")
                report["Security"] = get_security_info()

                self.progress.emit("Logs")
                report["Logs"] = get_logs()

            self.progress.emit("Completed")
            self.finished.emit(report)
        except Exception as exc:
            self.error.emit(f"Scan error: {exc}")
