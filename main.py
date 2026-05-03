from core.device import detect_mode
from scanners.device_info import get_device_info
from scanners.bootloader import get_bootloader_info
from scanners.hardware import get_hardware_info
from scanners.partitions import get_partitions
from scanners.apps import get_apps
from scanners.sensors import get_sensors
from scanners.logs import get_logs
from scanners.network import get_network_info
from scanners.security import get_security_info
from utils.formatter import print_section, export_json


def main():
    print("[*] Detecting device...")

    mode = detect_mode()
    print(f"[*] Mode: {mode}")

    if mode == "NO DEVICE":
        print("No device detected.")
        return

    report = {}

    # =========================
    # ADB MODE
    # =========================
    if mode == "ADB":
        print("[*] Scanning ADB device...")

        try:
            report["Device Info"] = get_device_info()
            report["Hardware"] = get_hardware_info()
            report["Partitions"] = get_partitions()
            report["Apps"] = get_apps()
            report["Sensors"] = get_sensors()
            report["Network"] = get_network_info()
            report["Security"] = get_security_info()
            report["Logs"] = get_logs()
        except Exception as e:
            print(f"[!] Error during ADB scan: {e}")

        # Print all sections dynamically
        for section, data in report.items():
            print_section(section, data)

    # =========================
    # FASTBOOT MODE
    # =========================
    elif mode == "FASTBOOT":
        print("[*] Scanning Fastboot device...")

        try:
            report["Bootloader"] = get_bootloader_info()
        except Exception as e:
            print(f"[!] Error during Fastboot scan: {e}")

        print_section("Bootloader", report.get("Bootloader", {}))

    # =========================
    # EXPORT REPORT
    # =========================
    try:
        export_json(report)
        print("\n[*] Report saved as report.json")
    except Exception as e:
        print(f"[!] Failed to save report: {e}")


if __name__ == "__main__":
    main()