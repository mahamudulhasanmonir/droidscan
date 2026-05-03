from core.runner import adb

def get_hardware_info():
    return {
        "CPU Info": adb(["shell", "cat", "/proc/cpuinfo"]),
        "Memory Info": adb(["shell", "cat", "/proc/meminfo"]),
        "Battery": adb(["shell", "dumpsys", "battery"]),
    }