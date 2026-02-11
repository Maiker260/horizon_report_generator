import zipfile
from src.reader.file_reader import ZipContext
from src.processing.gather_data import gather_data

def main(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            ctx = ZipContext(zip_file)
            data = {}

            data = gather_data(ctx)

            # Check Data
            for section, content in data.items():
                if content:
                    print(f"{section}:\n")
                    for k, v in content.items():
                        print(f"   {k}: {v}\n")
                else:
                    print(f"{section}:\n")
                    print("   None")

    except Exception as e:
        print("Error:", e)