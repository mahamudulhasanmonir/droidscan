from core.runner import adb

def get_apps():
    return {
        "All Apps": adb(["shell", "pm", "list", "packages"]),
        "System Apps": adb(["shell", "pm", "list", "packages", "-s"]),
        "User Apps": adb(["shell", "pm", "list", "packages", "-3"]),
    }