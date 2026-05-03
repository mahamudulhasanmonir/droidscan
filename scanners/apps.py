from core.runner import adb

def parse_packages(raw):
    return [line.replace("package:", "").strip() for line in raw.splitlines() if line.strip()]

def get_apps():
    all_apps = parse_packages(adb(["shell", "pm", "list", "packages"]))
    system_apps = parse_packages(adb(["shell", "pm", "list", "packages", "-s"]))
    user_apps = parse_packages(adb(["shell", "pm", "list", "packages", "-3"]))

    return {
        "Total Apps": len(all_apps),
        "User Apps": user_apps[:100],   # limit
        "System Apps": system_apps[:100]
    }