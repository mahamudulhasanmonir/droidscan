from PyQt6.QtCore import QThread, pyqtSignal

from scanners.device_info import get_device_info
from scanners.hardware import get_hardware_info
from scanners.partitions import get_partitions
from scanners.apps import get_apps
from scanners.network import get_network_info
from scanners.logs import get_logs
from scanners.security import get_security_info

class ScanWorker(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        report = {}

        report["Device"] = get_device_info()
        report["Hardware"] = get_hardware_info()
        report["Partitions"] = get_partitions()
        report["Apps"] = get_apps()
        report["Network"] = get_network_info()
        report["Security"] = get_security_info()
        report["Logs"] = get_logs()

        self.finished.emit(report)