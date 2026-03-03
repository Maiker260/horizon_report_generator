import sys
import ctypes
from pathlib import Path
from src.main import main
from src.exceptions import UnsupportedComponentError

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

        if zip_path.suffix.lower() != ".zip":
            show_error("Only ZIP files are supported.")
            sys.exit(1)

        report_path = main(zip_path)

        show_info(
            f"Report generated successfully.\n\nLocation:\n{report_path.resolve()}"
        )

    except UnsupportedComponentError as e:
        show_error(str(e))
        sys.exit(1)

    except Exception as e:
        show_error(f"An unexpected error occurred:\n\n{str(e)}")
        sys.exit(1)