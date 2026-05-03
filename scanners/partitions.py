from core.runner import adb

def get_partitions():
    return adb(["shell", "ls", "-l", "/dev/block/by-name"])