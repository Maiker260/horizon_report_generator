import sys
from pathlib import Path
import ctypes

from src.main import main

APP_TITLE = "Horizon Report Generator"


def show_info(message):
    ctypes.windll.user32.MessageBoxW(
        0,
        message,
        APP_TITLE,
        0x40  # MB_ICONINFORMATION
    )


def show_error(message):
    ctypes.windll.user32.MessageBoxW(
        0,
        message,
        APP_TITLE,
        0x10  # MB_ICONERROR
    )


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            show_error("No ZIP file was provided.")
            sys.exit(1)

        zip_path = Path(sys.argv[1])

        if not zip_path.exists():
            show_error("The selected file does not exist.")
            sys.exit(1)

        main(zip_path)

        show_info("Report generated successfully.")

    except Exception as e:
        show_error(f"An unexpected error occurred:\n\n{str(e)}")
        sys.exit(1)