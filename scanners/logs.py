from core.runner import adb

def get_logs():
    return {
        "Logcat": adb(["logcat", "-d", "-t", "100"]),
    }