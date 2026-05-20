from pathlib import Path
from .NAME_FIXES import KEY_FIXES, FEATURE_FIXES

def save_report(report, component, feature):
    key = KEY_FIXES.get(component, component.title())
    feature_name = FEATURE_FIXES.get(feature)

    base_name = f"Horizon {key} - {feature_name}"
    extension = ".txt"
    file_path = Path(f"{base_name}{extension}")
    counter = 1

    while file_path.exists():
        file_path = Path(f"{base_name} ({counter}){extension}")
        counter += 1

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    return file_path