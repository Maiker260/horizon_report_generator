from src.summary.data.data_to_collect.enrollment_server.DEVICE_INFO import ES_DEVICE_INFO
from src.summary.data.data_to_collect.enrollment_server.PORTS import ES_PORTS
from src.summary.data.data_to_collect.enrollment_server.SERVICE_KEYS import ES_SERVICE_KEYS

from src.summary.data.data_to_collect.connection_server.CONFIGURATION import CS_CONFIGURATION
from src.summary.data.data_to_collect.connection_server.DEVICE_INFO import CS_DEVICE_INFO
from src.summary.data.data_to_collect.connection_server.CERTIFICATES import CS_CERTIFICATES
from src.summary.data.data_to_collect.connection_server.PORTS import CS_PORTS

from src.summary.data.data_to_collect.agent.DEVICE_INFO import AGENT_DEVICE_INFO
from src.summary.data.data_to_collect.agent.PORTS import AGENT_PORTS
from src.summary.data.data_to_collect.agent.HORIZON_FEATURES import AGENT_HORIZON_FEATURES
from src.summary.data.data_to_collect.agent.LOG_LEVEL_FEATURES import AGENT_LOG_LEVEL_FEATURES

from src.summary.data.data_to_collect.client.LOG_LEVEL_FEATURES import CLIENT_LOG_LEVEL_FEATURES
from src.summary.data.data_to_collect.client.PORTS import CLIENT_PORTS

from src.summary.data.data_to_collect.uag.UAG_INFO import UAG_INFO
from src.summary.data.data_to_collect.uag.PORTS import UAG_PORTS

from src.summary.data.data_to_collect.COMMON_DATA_TO_COLLECT import COMMON_DATA_TO_COLLECT

DATA_TO_COLLECT = {
    "enrollment_server": {
        "device_info": ES_DEVICE_INFO,
        "server_roles": [],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": ES_PORTS,
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
        "service_keys": ES_SERVICE_KEYS
    },

    "connection_server": {
        "device_info": CS_DEVICE_INFO,
        "configuration": CS_CONFIGURATION,
        "replication": [],
        "server_roles": [],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": CS_PORTS,
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "certificates": CS_CERTIFICATES,
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
    },

    "agent": {
        "device_info": AGENT_DEVICE_INFO,
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": AGENT_PORTS,
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "horizon_features": AGENT_HORIZON_FEATURES,
        "log_level_features": AGENT_LOG_LEVEL_FEATURES,
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
    },

    "client": {
        "device_info": COMMON_DATA_TO_COLLECT["device_info"],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": CLIENT_PORTS,
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "log_level_features": CLIENT_LOG_LEVEL_FEATURES,
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
    },

    "unified_access_gateway": {
        "uag_info": UAG_INFO,
        "horizon_ports": UAG_PORTS
    },
}