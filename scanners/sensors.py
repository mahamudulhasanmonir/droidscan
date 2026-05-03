from core.runner import adb

def get_sensors():
    return adb(["shell", "dumpsys", "sensorservice"])