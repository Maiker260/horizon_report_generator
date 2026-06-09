COMMON_FILES_OF_INTEREST = {
    "device_info": [
        "systeminfo.txt", 
        "ipconfig-all.txt", 
        "omnissa-reg.txt", 
        "vmware-reg.txt"
    ],
    "horizon_services": ["net-start.txt"],
    "horizon_ports": ["netstat-abov.txt"],
    "installed_software": ["installed_software.txt"],
}

FILES_OF_INTEREST = {
    "connection_server": {
        "device_info": COMMON_FILES_OF_INTEREST["device_info"],
        "server_roles": [
            "tasklist-svc.txt", 
            "net-start.txt"
        ],
        "horizon_services": COMMON_FILES_OF_INTEREST["horizon_services"],
        "horizon_ports": COMMON_FILES_OF_INTEREST["horizon_ports"],
        "installed_software": COMMON_FILES_OF_INTEREST["installed_software"],
        "certificates": ["cert-store.txt"],
        "locked_properties": ["locked.properties"]
    },
    "agent": {
        "device_info": COMMON_FILES_OF_INTEREST["device_info"],
        "horizon_services": COMMON_FILES_OF_INTEREST["horizon_services"],
        "horizon_ports": COMMON_FILES_OF_INTEREST["horizon_ports"],
        "installed_software": COMMON_FILES_OF_INTEREST["installed_software"],
        "horizon_features": [
            "omnissa-reg.txt", 
            "vmware-reg.txt", 
            "policies-reg.txt"
        ],
        "log_level_features": [
            "omnissa-reg.txt", 
            "vmware-reg.txt"
        ],
    },
    "client": {
        "device_info": COMMON_FILES_OF_INTEREST["device_info"],
        "horizon_services": COMMON_FILES_OF_INTEREST["horizon_services"],
        "horizon_ports": COMMON_FILES_OF_INTEREST["horizon_ports"],
        "installed_software": COMMON_FILES_OF_INTEREST["installed_software"],
        "horizon_features": [
            "omnissa-reg.txt", 
            "vmware-reg.txt", 
            "policies-reg.txt"
        ],
        "log_level_features": [
            "omnissa-reg.txt", 
            "vmware-reg.txt"
        ],
    },
    "unified_access_gateway": {
        "uag_info": [
            "uag_config.ini", 
            "version.info"
        ],
        "horizon_ports": ["netstat.log"]
    },
}