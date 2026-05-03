from core.runner import adb


def get_security_info():
    return {
        "SELinux": adb(["shell", "getenforce"]),
        "Bootloader State": adb(["shell", "getprop", "ro.boot.vbmeta.device_state"]),
        "Flash Lock": adb(["shell", "getprop", "ro.boot.flash.locked"]),
        "OEM Unlock Supported": adb(["shell", "getprop", "ro.oem_unlock_supported"]),
        "OEM Unlock Allowed": adb(["shell", "getprop", "sys.oem_unlock_allowed"]),
        "Verified Boot": adb(["shell", "getprop", "ro.boot.verifiedbootstate"]),
        "Encryption": adb(["shell", "getprop", "ro.crypto.state"]),
    }
