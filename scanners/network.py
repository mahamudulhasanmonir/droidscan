from core.runner import adb

def get_network_info():
    return {
        "IP Address": adb(["shell", "ip", "addr", "show", "wlan0"]),
        "WiFi Info": adb(["shell", "dumpsys", "wifi"]),
        "Mobile Data": adb(["shell", "dumpsys", "telephony.registry"]),
    }