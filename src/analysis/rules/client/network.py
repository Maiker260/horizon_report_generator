NETWORK_RULES = [
    {
        "name": "VDPCONNECT_HOST_UNREACHABLE",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_HOST_UNREACHABLE",
        ],
        "recommendations": [
            "This error typically indicates that a socket connection attempt has failed because the host is unreachable"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91015"
        ]
    },
    {
        "name": "VDPCONNECT_HOSTNAME_NOT_RESOLVABLE",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_HOSTNAME_NOT_RESOLVABLE",
        ],
        "recommendations": [
            "The client is unable to translate a given hostname into an IP address",
            "This error can happen due to various reasons such as incorrect DNS settings, network connectivity issues, or an incorrect hostname"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91028"
        ]
    },
    {
        "name": "VDPCONNECT_NETWORK_UNREACHABLE",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_NETWORK_UNREACHABLE",
        ],
        "recommendations": [
            "This error typically indicates that a socket connection attempt has failed because the network is unreachable"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91029"
        ]
    },
    {
        "name": "VDPCONNECT_CONN_TIMEDOUT",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_CONN_TIMEDOUT",
        ],
        "recommendations": [
            "This error typically indicates that a socket connection attempt has failed because the network is unreachable"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91019"
        ]
    },
    {
        "name": "VDPCONNECT_CONN_REFUSED",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_CONN_REFUSED",
        ],
        "recommendations": [
            "This error typically indicates that a socket connection attempt has failed because the service is not available on the target device",
            "Check that the protocol service port is not blocked by a firewall"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91020"
        ]
    },
    {
        "name": "VDPCONNECT_CONN_ACCESS_DENIED",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_CONN_ACCESS_DENIED",
        ],
        "recommendations": [
            "This error typically seen when the Horizon agent software returns an error forbidden when establishing a connection to network concerns"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91030"
        ]
    },
    {
        "name": "VDPCONNECT_CONN_TERMINATED",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_CONN_TERMINATED",
        ],
        "recommendations": [
            "This error typically seen when the Horizon Client software initiates the termination of an established connection to network concerns"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91031"
        ]
    },
    {
        "name": "VDPCONNECT_CONN_RESET",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_CONN_RESET",
        ],
        "recommendations": [
            "This error occurs when the remote server or network suddenly resets your horizon client connection without adequately notifying your computer"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91179"
        ]
    },
    {
        "name": "VDPCONNECT_REJECTED",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_REJECTED",
        ],
        "recommendations": [
            "The client computer is unable to establish a connection with another device or server",
            "This error can be caused by a variety of factors, such as network issues, firewall settings, or incorrect connection parameters"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91182"
        ]
    },
    {
        "name": "VDPCONNECT_GATEWAY_ERROR",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_GATEWAY_ERROR",
        ],
        "recommendations": [
            "This error typically encountered when the Blast Secure Gateway (BSG ) encounters a response where it is unable to connect to the agent",
            "It will be triggered if BSG does not receive ICMP host/port unreachable or TCP RST when the agent is unreachable/down or a firewall blocks the port"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91017"
        ]
    },
    {
        "name": "VDPCONNECT_GATEWAY_TIMEOUT",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_GATEWAY_TIMEOUT",
        ],
        "recommendations": [
            "This error typically encountered when the Blast Secure Gateway (BSG ) encounters a response where it cannot find the route to the host  or it encounters a lack of availability of service",
            "Typically a received ICMP host/port unreachable or TCP RST when attempting to connect to the agent"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91016"
        ]
    },
    {
        "name": "VDPCONNECT_PEER_UNAVAILABLE",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_PEER_UNAVAILABLE",
        ],
        "recommendations": [
            "This error message indicates that the connection encountered an unavailable peer, which could be due to network issues, firewalls, or proxies that are temporarily blocking the connection",
            "Typically a received ICMP host/port unreachable or TCP RST when attempting to connect to the agent"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91180"
        ]
    },
    {
        "name": "VDPCONNECT_PEER_ERROR",
        "category": "network",
        "patterns": [
            r"VDPCONNECT_PEER_ERROR",
        ],
        "recommendations": [],
        "references": [
            "https://kb.omnissa.com/s/article/91181"
        ]
    },
]