from src.parsers.server_info.server_info import server_info

def gather_data(zip_ctx):
    data = {}

    data["server_info"] = server_info(zip_ctx)

    return data