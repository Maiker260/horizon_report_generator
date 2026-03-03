from src.parsers.device_info.device_info_check import device_info_check
from src.parsers.server_roles.server_roles_check import server_roles_check
from src.parsers.horizon_services.horizon_services_check import horizon_services_check
from src.parsers.horizon_ports.horizon_ports_check import horizon_ports_check
from src.parsers.installed_software.installed_software_check import installed_software_check
from src.parsers.certificates.certificates_check import certificates_check
from src.parsers.horizon_features import horizon_features_check
from src.parsers.locked_properties.locked_properties_check import locked_properties_check

COMMON_PARSERS = {
    "device_info": device_info_check,
    "horizon_services": horizon_services_check,
    "horizon_ports": horizon_ports_check,
    "installed_software": installed_software_check,
}

COMPONENT_CHECKS = {
    "connection_server": {
        "parsers": {
            **COMMON_PARSERS,
            "server_roles": server_roles_check,
            "certificates": certificates_check,
            "locked_properties": locked_properties_check,
        }
    },
    "agent": {
        "parsers": {
            **COMMON_PARSERS,
            "horizon_features": horizon_features_check
        }
    },
    "client": {
        "parsers": {
            **COMMON_PARSERS
        }
    },
    "unified_access_gateway": {}
}