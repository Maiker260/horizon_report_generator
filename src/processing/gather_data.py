from src.parsers.device_info.device_info_check import device_info_check
from src.parsers.server_roles_check import server_roles_check

parsers = {
    "device_info": device_info_check,
    "server_roles": server_roles_check,
}

def gather_data(zip_ctx):
    data = {}

    for name, parser_func in parsers.items():
        try:
            data[name] = parser_func(zip_ctx)
        except Exception as e:
            data[name] = {
                "error": str(e)
            }

    return data