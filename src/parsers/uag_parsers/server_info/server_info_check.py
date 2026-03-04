from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def server_info_check(zip_ctx):
    files = FILES_OF_INTEREST["unified_access_gateway"]["server_info"]
    # data = DATA_TO_COLLECT["unified_access_gateway"]["server_info"]

    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

    return data