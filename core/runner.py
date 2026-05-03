import subprocess
import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADB = os.path.join(BASE_DIR, "platform-tools", "adb")
FASTBOOT = os.path.join(BASE_DIR, "platform-tools", "fastboot")

if platform.system() == "Windows":
    ADB += ".exe"
    FASTBOOT += ".exe"


def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return result.decode().strip()
    except Exception as e:
        return f"Error: {str(e)}"


def adb(cmd):
    return run_cmd([ADB] + cmd)


def fastboot(cmd):
    return run_cmd([FASTBOOT] + cmd)