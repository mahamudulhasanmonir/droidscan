from core.runner import adb

def get_logs():
    return {
        "Logcat (Last 200 lines)": adb(["logcat", "-d", "-t", "200"]),
        "Kernel Logs": adb(["shell", "dmesg"]),
    }