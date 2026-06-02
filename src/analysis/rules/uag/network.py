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
]