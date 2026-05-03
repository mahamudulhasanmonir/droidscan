from core.runner import adb

def get_security_info():
    return {
        "SELinux": adb(["shell", "getenforce"]),
        "Verified Boot": adb(["shell", "getprop", "ro.boot.verifiedbootstate"]),
        "Encryption": adb(["shell", "getprop", "ro.crypto.state"]),
    }