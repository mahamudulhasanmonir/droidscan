from core.runner import fastboot

def get_bootloader_info():
    return {
        "Unlocked": fastboot(["getvar", "unlocked"]),
        "Secure": fastboot(["getvar", "secure"]),
        "Product": fastboot(["getvar", "product"]),
    }