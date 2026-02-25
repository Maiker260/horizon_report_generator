from pathlib import Path
import traceback

def save_error_log(exception: Exception):
    base_name = "Horizon Report ERROR"
    extension = ".txt"
    file_path = Path(f"{base_name}{extension}")
    counter = 1

    while file_path.exists():
        file_path = Path(f"{base_name} ({counter}){extension}")
        counter += 1

    error_content = (
        "REPORT GENERATION FAILED\n"
        + "=" * 60
        + "\n\n"
        + traceback.format_exc()
    )

    file_path.write_text(error_content, encoding="utf-8")