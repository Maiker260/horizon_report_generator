from src.parsers.device_info.device_info import device_info

def gather_data(zip_ctx):
    data = {}

    data["device_info"] = device_info(zip_ctx)

    return data