from core.runner import adb

def get_device_info():
    return {
        "Model": adb(["shell", "getprop", "ro.product.model"]),
        "Brand": adb(["shell", "getprop", "ro.product.brand"]),
        "Manufacturer": adb(["shell", "getprop", "ro.product.manufacturer"]),
        "Android Version": adb(["shell", "getprop", "ro.build.version.release"]),
        "SDK": adb(["shell", "getprop", "ro.build.version.sdk"]),
        "Codename": adb(["shell", "getprop", "ro.product.device"]),
        "Serial": adb(["get-serialno"]),
    }