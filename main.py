from core.device import detect_mode
from scanners.device_info import get_device_info
from scanners.bootloader import get_bootloader_info
from scanners.hardware import get_hardware_info
from scanners.partitions import get_partitions
from utils.formatter import print_section, export_json

def main():
    print("[*] Detecting device...")

    mode = detect_mode()
    print(f"[*] Mode: {mode}")

    if mode == "NO DEVICE":
        print("No device detected.")
        return

    report = {}

    if mode == "ADB":
        print("[*] Scanning ADB device...")

        report["Device Info"] = get_device_info()
        report["Hardware"] = get_hardware_info()
        report["Partitions"] = get_partitions()

        print_section("Device Info", report["Device Info"])
        print_section("Hardware", report["Hardware"])
        print_section("Partitions", report["Partitions"])

    elif mode == "FASTBOOT":
        print("[*] Scanning Fastboot device...")

        report["Bootloader"] = get_bootloader_info()
        print_section("Bootloader", report["Bootloader"])

    export_json(report)
    print("\n[*] Report saved as report.json")


if __name__ == "__main__":
    main()