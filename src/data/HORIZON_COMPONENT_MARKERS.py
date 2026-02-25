HORIZON_COMPONENT_MARKERS = {
    "connection_server": {
        "dirs": [
            "horizon-logs/broker",
            "horizon-logs/bsg",
            "horizon-logs/psg",
            "horizon-logs/messagebus",
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
            "horizon-sm-dumps",
            "vmlm-data",
        ],
        "files": [
            "rtav_agent_pcoip_session0.log",
            "vmlm_service.txt",
        ],
        "patterns": [
            r"vmware-vmtoolsd-.*\.log",
            r"horizon-hzAgentMonService-.*\.log",
        ],
        "weight": 4,
    },

    "client": {
        "dirs": [
            "hzn-logs",
            "hzn-config",
            "hzn-event-logs",
        ],
        "files": [
            "Omnissa_Horizon_Client",
        ],
        "patterns": [
            r"Omnissa_Horizon_Client_.*\.log",
            r".*ViewClientx64\.log",
        ],
        "weight": 5,
    }
}