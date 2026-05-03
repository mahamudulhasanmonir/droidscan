from core.runner import adb

def get_network_info():
    return {
        "IP": adb(["shell", "ip", "addr", "show", "wlan0"]),
    }