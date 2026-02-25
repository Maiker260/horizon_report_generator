from src.parsers.device_info.device_info_check import device_info_check
from src.parsers.server_roles.server_roles_check import server_roles_check
from src.parsers.horizon_services.horizon_services_check import horizon_services_check
from src.parsers.horizon_ports.horizon_ports_check import horizon_ports_check
from src.parsers.installed_software.installed_software_check import installed_software_check
from src.parsers.certificates.certificates_check import certificates_check

COMPONENT_CHECKS = {
    "connection_server": {
        "parsers": {
            "device_info": device_info_check,
            "server_roles": server_roles_check,
            "horizon_services": horizon_services_check,
            "horizon_ports": horizon_ports_check,
            "installed_software": installed_software_check,
            "certificates": certificates_check,
        }
    },
    "agent": {
        "parsers": {
            "device_info": device_info_check,
            "horizon_services": horizon_services_check,
            "horizon_ports": horizon_ports_check,
            "installed_software": installed_software_check,
        }
    },
    "client": {
        "parsers": {
            "device_info": device_info_check,
            "horizon_services": horizon_services_check,
            "horizon_ports": horizon_ports_check,
            "installed_software": installed_software_check,
        }
    },
    "unified_access_gateway": {}
}