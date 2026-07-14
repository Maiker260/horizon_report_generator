from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def config_file(zip_ctx, filename, component):
    keywords = DATA_TO_COLLECT[component]["configuration"]

    data = {}

    if not zip_ctx.exists(filename):
        return

    with zip_ctx.open(filename) as file:
        reader = read_file_with_auto_encoding(file)

        for line in reader:
            for keyword in keywords - data.keys():
                if line.startswith(f"{keyword}="):
                    key, value = line.split("=")
                    data[key] = value.strip()

    return data