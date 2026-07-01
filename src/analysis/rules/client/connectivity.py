from src.analysis.utils.rule_constructor import Rule

CONNECTIVITY_RULES = [
    Rule(
        name="VDPCONNECT_HOST_UNREACHABLE",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_HOST_UNREACHABLE"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically indicates that a socket connection attempt has failed because the host is unreachable"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91015"
        ]
    ),
    Rule(
        name="VDPCONNECT_HOSTNAME_NOT_RESOLVABLE",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_HOSTNAME_NOT_RESOLVABLE"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "The client is unable to translate a given hostname into an IP address",
            "This error can happen due to various reasons such as incorrect DNS settings, network connectivity issues, or an incorrect hostname"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91028"
        ]
    ),
    Rule(
        name="VDPCONNECT_NETWORK_UNREACHABLE",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_NETWORK_UNREACHABLE"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically indicates that a socket connection attempt has failed because the network is unreachable"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91029"
        ]
    ),
    Rule(
        name="VDPCONNECT_CONN_TIMEDOUT",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONN_TIMEDOUT"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically indicates that a socket connection attempt has failed because the network is unreachable"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91019"
        ]
    ),
    Rule(
        name="VDPCONNECT_CONN_REFUSED",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONN_REFUSED"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically indicates that a socket connection attempt has failed because the service is not available on the target device",
            "Check that the protocol service port is not blocked by a firewall"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91020"
        ]
    ),
    Rule(
        name="VDPCONNECT_CONN_ACCESS_DENIED",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONN_ACCESS_DENIED"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically seen when the Horizon agent software returns an error forbidden when establishing a connection to network concerns"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91030"
        ]
    ),
    Rule(
        name="VDPCONNECT_CONN_TERMINATED",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONN_TERMINATED"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically seen when the Horizon Client software initiates the termination of an established connection to network concerns"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91031"
        ]
    ),
    Rule(
        name="VDPCONNECT_CONN_RESET",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONN_RESET"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error occurs when the remote server or network suddenly resets your horizon client connection without adequately notifying your computer"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91179"
        ]
    ),
    Rule(
        name="VDPCONNECT_REJECTED",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_REJECTED"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "The client computer is unable to establish a connection with another device or server",
            "This error can be caused by a variety of factors, such as network issues, firewall settings, or incorrect connection parameters"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91182"
        ]
    ),
    Rule(
        name="VDPCONNECT_GATEWAY_ERROR",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_GATEWAY_ERROR"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically encountered when the Blast Secure Gateway (BSG ) encounters a response where it is unable to connect to the agent",
            "It will be triggered if BSG does not receive ICMP host/port unreachable or TCP RST when the agent is unreachable/down or a firewall blocks the port"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91017"
        ]
    ),
    Rule(
        name="VDPCONNECT_GATEWAY_TIMEOUT",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_GATEWAY_TIMEOUT"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically encountered when the Blast Secure Gateway (BSG ) encounters a response where it cannot find the route to the host or it encounters a lack of availability of service",
            "Typically a received ICMP host/port unreachable or TCP RST when attempting to connect to the agent"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91016"
        ]
    ),
    Rule(
        name="VDPCONNECT_PEER_UNAVAILABLE",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_PEER_UNAVAILABLE"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error message indicates that the connection encountered an unavailable peer, which could be due to network issues, firewalls, or proxies that are temporarily blocking the connection",
            "Typically a received ICMP host/port unreachable or TCP RST when attempting to connect to the agent"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91180"
        ]
    ),
    Rule(
        name="VDPCONNECT_PEER_ERROR",
        category="connectivity",
        match_type="contains",
        patterns=[
            "VDPCONNECT_PEER_ERROR"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/91181"
        ]
    ),
    Rule(
        name='Connecting to Omnissa Horizon View desktops with a Horizon Client fails with the error: "An SSL error Occurred"',
        category="connectivity",
        match_type="contains",
        patterns=[
            "TLS alert, decrypt error"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/78372"
        ]
    ),
]