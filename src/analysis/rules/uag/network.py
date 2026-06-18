from src.analysis.utils.rule_constructor import Rule

NETWORK_RULES = [
    Rule(
        name="Unable to resolve the Connection Server FQDN",
        category="network",
        match_type="regex",
        patterns=[
            r"java.net.UnknownHostException.*Name or service not known"
        ],
        source_files=[
            "esmanager.log"
        ],
        recommendations=[
            "Check your IP, subnet, gateway and DNS settings are configured correctly or as you would expect",
            "Check basic device interconnectivity utilizing ping or curl on the UAG console to the Connection Server",
        ],
        references=[
            "https://kb.omnissa.com/s/article/57161"
        ]
    ),
    Rule(
        name="Failed to resolve proxying route for request",
        category="network",
        match_type="regex",
        patterns=[
            r"Added route .* to target .*\|8443"
        ],
        source_files=[
            "bsg.log"
        ],
        recommendations=[
            "Disable the use of the Blast Secure Gateway or Select 'Use Blast Secure Gateway for only HTML Access Blast connections to machine' in the CS configuration",
        ],
        references=[
            "https://kb.omnissa.com/s/article/90155"
        ]
    ),
    Rule(
        name="UAG 2312 admin UI reports HTTP ERROR 400 Bad Request",
        category="network",
        match_type="contains",
        patterns=[
            "Sending bad request. Incoming request does not have valid host header:"
        ],
        source_files=[
            "esmanager.log"
        ],
        recommendations=[
            "Ensure all Host header values traversing through UAG is allowed in either Allow Host Header or Auto-Allow Host Header section under System Configuration"
        ],
        references=[
            "https://kb.omnissa.com/s/article/97414"
        ]
    ),
    Rule(
        name='Unified Access Gateway (UAG): Horizon users are intermittently disconnected while in session with error "Logout requested by system"',
        category="network",
        match_type="contains",
        patterns=[
            "Too many connections opened for session:"
        ],
        source_files=[
            "esmanager.log"
        ],
        recommendations=[
            "Disable multiplexing or any applicable feature on the load balancer appliance that reuses sessions that are presented to the UAG appliances",
            "Please consult your load balancer or network appliance vendor for guidance on what features would reuse sessions in this manner"
        ],
        references=[
            "https://kb.omnissa.com/s/article/87822"
        ]
    ),
]