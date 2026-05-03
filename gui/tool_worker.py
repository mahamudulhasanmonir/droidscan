from PyQt6.QtCore import QThread, pyqtSignal

from core.device import detect_mode
from core.runner import adb, fastboot
from scanners.device_info import get_device_info
from scanners.hardware import get_hardware_info
from scanners.security import get_security_info


class ToolWorker(QThread):
    finished = pyqtSignal(str, str)
    error = pyqtSignal(str)

    def __init__(self, action):
        super().__init__()
        self.action = action

    def run(self):
        try:
            mode = detect_mode()

            if self.action == "refresh_mode":
                result = f"Current mode: {mode}"
            elif self.action == "reboot_normal":
                result = self._reboot_normal(mode)
            elif self.action == "reboot_fastboot":
                result = self._reboot_fastboot(mode)
            elif self.action == "reboot_edl":
                result = self._reboot_edl(mode)
            elif self.action == "read_hw_info":
                result = self._read_hw_info(mode)
            else:
                raise ValueError(f"Unknown action: {self.action}")

            self.finished.emit(self.action, result)
        except Exception as exc:
            self.error.emit(str(exc))

    def _reboot_normal(self, mode):
        if mode == "ADB":
            adb(["reboot"])
            return "Reboot command sent through ADB."
        if mode == "FASTBOOT":
            fastboot(["reboot"])
            return "Reboot command sent through Fastboot."
        raise RuntimeError("No connected device found.")

    def _reboot_fastboot(self, mode):
        if mode == "ADB":
            adb(["reboot", "bootloader"])
            return "Rebooting device into Fastboot mode."
        if mode == "FASTBOOT":
            return "Device is already in Fastboot mode."
        raise RuntimeError("ADB device is required to enter Fastboot mode.")

    def _reboot_edl(self, mode):
        if mode == "ADB":
            adb(["reboot", "edl"])
            return "Rebooting device into EDL mode."
        raise RuntimeError("ADB mode is required to enter EDL from this tool.")

    def _read_hw_info(self, mode):
        if mode != "ADB":
            raise RuntimeError("ADB mode is required to read hardware information.")

        device = get_device_info()
        security = get_security_info()
        hardware = get_hardware_info()

        parts = [
            "=== Device ===",
            "\n".join(f"{key}: {value}" for key, value in device.items()),
            "",
            "=== Security ===",
            "\n".join(f"{key}: {value}" for key, value in security.items()),
            "",
            "=== Hardware ===",
            "\n".join(f"{key}: {value}" for key, value in hardware.items()),
        ]
        return "\n".join(parts)
