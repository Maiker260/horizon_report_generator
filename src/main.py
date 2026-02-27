import zipfile
from pathlib import Path
from src.reader.file_reader import ZipContext
from src.processing.gather_data import gather_data
from src.report.generate_report import generate_report
from src.processing.detect_component import detect_component
from src.report.save_report import save_report
from src.report.save_error_log import save_error_log

def main(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            zip_ctx = ZipContext(zip_file)

            component = detect_component(zip_ctx)
            data = gather_data(zip_ctx, component)

            report = generate_report(data, zip_path, component)

            # print(report)
            save_report(report)

    except Exception as e:
        save_error_log(e)
        raise