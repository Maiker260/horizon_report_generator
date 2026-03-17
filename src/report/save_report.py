from pathlib import Path

KEY_FIXES = {
    "connection_server": "CS",
    "unified_access_gateway": "UAG",
}

def save_report(report, component):
    key = KEY_FIXES.get(component, component.title())

    base_name = f"Horizon {key} Report"
    extension = ".txt"
    file_path = Path(f"{base_name}{extension}")
    counter = 1

    while file_path.exists():
        file_path = Path(f"{base_name} ({counter}){extension}")
        counter += 1

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    return file_path