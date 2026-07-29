from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def set_file(zip_ctx, filename, component, current_data):
    keywords = DATA_TO_COLLECT[component]["device_info"]

    if not zip_ctx.exists(filename):
        return

    data = {}

    with zip_ctx.open(filename) as file:
        reader = read_file_with_auto_encoding(file)

        for line in reader:
            line = line.strip()

            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)

            if key in keywords:
                data[key] = value

    return data