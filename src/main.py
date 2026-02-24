import zipfile
from pathlib import Path
from src.reader.file_reader import ZipContext
from src.processing.gather_data import gather_data
from src.report.generate_report import generate_report

def main(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            data = {}
            zip_ctx = ZipContext(zip_file)

            data = gather_data(zip_ctx)

            # Generate Report
            generate_report(data, zip_path)

    except Exception as e:
        # print("Error:", e)

        # Will create a .txt file with the errors
        base_name = "Horizon Report ERRORS"
        extension = ".txt"
        file_path = Path(f"{base_name}{extension}")
        counter = 1

        while file_path.exists():
            file_path = Path(f"{base_name} ({counter}){extension}")
            counter += 1

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(e)