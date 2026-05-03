import json

def print_section(title, data):
    print(f"\n=== {title} ===")
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"{k}: {v}")
    else:
        print(data)


def export_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)