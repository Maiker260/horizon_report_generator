from src.analysis.utils.rule_constructor import Rule

CERTIFICATE_RULES = [
    Rule(
        name="VDPCONNECT_CONNECT_TLS",
        category="certificate",
        match_type="contains",
        patterns=[
            "VDPCONNECT_CONNECT_TLS",
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This error typically indicates that a certificate issue is impeding connection",
            "In the Client, try setting the 'Certificate Checking Mode' to 'Do not verify server identity certificates'"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91018"
        ]
    ),
]