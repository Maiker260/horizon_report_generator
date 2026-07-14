from src.summary.parsers.common.device_info.device_info_check import device_info_check
from src.summary.parsers.common.horizon_services.horizon_services_check import horizon_services_check
from src.summary.parsers.common.horizon_ports.horizon_ports_check import horizon_ports_check
from src.summary.parsers.common.installed_software.installed_software_check import installed_software_check
from src.summary.parsers.common.log_level_features.log_level_features_check import log_level_features_check
from src.summary.parsers.connection_server.configuration.configuration_check import configuration_check
from src.summary.parsers.connection_server.server_roles.server_roles_check import server_roles_check
from src.summary.parsers.connection_server.certificates.certificates_check import certificates_check
from src.summary.parsers.connection_server.locked_properties.locked_properties_check import locked_properties_check
from src.summary.parsers.agent.horizon_features import horizon_features_check
from src.summary.parsers.enrollment_server.service_keys import service_keys

from src.summary.parsers.uag.uag_info.uag_info_check import uag_info_check
from src.summary.parsers.uag.uag_ports.uag_ports_check import uag_ports_check

COMMON_PARSERS = {
    "device_info": device_info_check,
    "horizon_services": horizon_services_check,
    "horizon_ports": horizon_ports_check,
    "installed_software": installed_software_check,
}

COMPONENT_CHECKS = {
    "enrollment_server": {
        "parsers": {
            **COMMON_PARSERS,
            "configuration": configuration_check,
            "server_roles": server_roles_check,
            "service_keys": service_keys
        }
    },
    "connection_server": {
        "parsers": {
            **COMMON_PARSERS,
            "configuration": configuration_check,
            "server_roles": server_roles_check,
            "certificates": certificates_check,
            "locked_properties": locked_properties_check,
        }
    },
    "agent": {
        "parsers": {
            **COMMON_PARSERS,
            "horizon_features": horizon_features_check,
            "log_level_features": log_level_features_check
        }
    },
    "client": {
        "parsers": {
            **COMMON_PARSERS,
            "log_level_features": log_level_features_check
        }
    },
    "unified_access_gateway": {
        "parsers": {
            "uag_info": uag_info_check,
            "horizon_ports": uag_ports_check,
        }
    }
}