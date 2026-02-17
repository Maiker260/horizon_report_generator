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

            # Check Data
            for section, content in data.items():
                if content:
                    print(f"{section}:\n")
                    for k, v in content.items():
                        print(f"   {k}: {v}\n")
                else:
                    print(f"{section}:\n")
                    print("   None\n")
            
            # Generate Report
            generate_report(data)

    except Exception as e:
        print("Error:", e)