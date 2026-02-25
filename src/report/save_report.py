from pathlib import Path

def save_report(report):
    base_name = "Horizon Report"
    extension = ".txt"
    file_path = Path(f"{base_name}{extension}")
    counter = 1

    while file_path.exists():
        file_path = Path(f"{base_name} ({counter}){extension}")
        counter += 1

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)