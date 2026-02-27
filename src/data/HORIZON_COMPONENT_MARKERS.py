HORIZON_COMPONENT_MARKERS = {
    "connection_server": {
        "dirs": [
            r".*-logs/broker",
            r".*-logs/bsg",
            r".*-logs/psg",
            r".*-logs/messagebus",
        ],
        "files": [
            "adam.ldif",
            "adam-schema.ldif",
            "config.properties",
        ],
        "patterns": [
            r"SecurityGateway_.*\.log",
            r"catalina\..*\.log",
        ],
        "weight": 5,
    },

    "agent": {
        "dirs": [
            "blast-logs",
            r".*-sm-dumps",
            "vmlm-data",
            "v4v-agent-logs",
        ],
        "files": [
            "rtav_agent_pcoip_session0.log",
            "vmlm_service.txt",
        ],
        "patterns": [
            r"vmware-vmtoolsd-.*\.log",
            r".*-hzAgentMonService-.*\.log",
        ],
        "weight": 4,
    },

    "client": {
        # "dirs": [
        #     r".*-Print-Registry-Data",
        #     r".*-USB-Registry-Data",
        # ],
        "files": [
            r".*_Horizon_Client",
        ],
        "patterns": [
            r".*_Horizon_Client_.*\.log",
            r".*ViewClientx64\.log",
            r".*_HTML5MMRx64.log",
        ],
        "weight": 5,
    }
}