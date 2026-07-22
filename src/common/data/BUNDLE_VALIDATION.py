BUNDLE_VALIDATION = {
    "enrollment_server": {
        "required": [
            "systeminfo.txt",
            "ipconfig-all.txt",
            "net-start.txt",
            "netstat-abov.txt",
            "installed_software.txt",
        ],
        "structural": [
            r"wsnm_starts\.txt",
        ],
    },

    "connection_server": {
        "required": [
            "systeminfo.txt",
            "ipconfig-all.txt",
            "net-start.txt",
            "netstat-abov.txt",
            "installed_software.txt",
        ],
        "structural": [
            r".*-logs/broker",
            r"adam.*\.ldif",
        ],
    },

    "agent": {
        "required": [
            "systeminfo.txt",
            "ipconfig-all.txt",
            "net-start.txt",
            "installed_software.txt",
        ],
        "structural": [
            "vmlm-data",
            "v4v-agent-logs",
        ],
    },

    "client": {
        "required": [
            "systeminfo.txt",
            "ipconfig-all.txt",
        ],
        "structural": [
            r".*_Horizon_Client",
            r".*-horizon-viewclient-.*\.txt",
        ],
    },

    "unified_access_gateway": {
        "required": [
            "uag_config.ini",
            "version.info",
        ],
        "structural": [
            r"esmanager.*\.log",
        ],
    },
}