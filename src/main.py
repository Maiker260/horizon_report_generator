import zipfile
from src.reader.file_reader import ZipContext
from src.processing.gather_data import gather_data
from src.report.generate_report import generate_report

def main(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            data = {}
            zip_ctx = ZipContext(zip_file)

            data = gather_data(zip_ctx)

            # NEED TO CHECK WHAT REPORT SHOULD RETURN (CS, AGENT, CLIENT, UAG)

            # Generate Report
            generate_report(data, zip_path)

    except Exception as e:
        print("Error:", e)

        # Will create a .txt file with the errors