from core.runner import adb


def get_device_info():
    return {
        "Model": adb(["shell", "getprop", "ro.product.model"]),
        "Brand": adb(["shell", "getprop", "ro.product.brand"]),
        "Manufacturer": adb(["shell", "getprop", "ro.product.manufacturer"]),
        "Android Version": adb(["shell", "getprop", "ro.build.version.release"]),
        "SDK": adb(["shell", "getprop", "ro.build.version.sdk"]),
        "Security Patch": adb(["shell", "getprop", "ro.build.version.security_patch"]),
        "Build Fingerprint": adb(["shell", "getprop", "ro.build.fingerprint"]),
        "Build Type": adb(["shell", "getprop", "ro.build.type"]),
        "Kernel": adb(["shell", "uname", "-r"]),
        "CPU ABI": adb(["shell", "getprop", "ro.product.cpu.abi"]),
        "Codename": adb(["shell", "getprop", "ro.product.device"]),
        "Serial": adb(["get-serialno"]),
    }
