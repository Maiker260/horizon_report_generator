from src.parsers.device_info.device_info_check import device_info_check
from src.parsers.server_roles.server_roles_check import server_roles_check
from src.parsers.horizon_services.horizon_services_check import horizon_services_check
from src.parsers.horizon_ports.horizon_ports_check import horizon_ports_check
from src.parsers.installed_software.installed_software_check import installed_software_check

parsers = {
    "device_info": device_info_check,
    "server_roles": server_roles_check,
    "horizon_services": horizon_services_check,
    "horizon_ports": horizon_ports_check,
    "installed_software": installed_software_check,
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