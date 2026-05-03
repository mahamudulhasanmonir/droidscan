from core.runner import adb, fastboot

def detect_mode():
    adb_out = adb(["devices"])
    if "device" in adb_out and "List of devices" in adb_out:
        return "ADB"

    fb_out = fastboot(["devices"])
    if fb_out.strip():
        return "FASTBOOT"

    return "NO DEVICE"