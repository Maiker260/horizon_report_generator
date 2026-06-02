from src.analysis.utils.rule_constructor import Rule

GENERAL_RULES = [
    Rule(
        name="UAG admin console shows 'Horizon destination server' as down/red",
        category="general",
        match_type="contains",
        patterns=[
            "javax.net.ssl.SSLHandshakeException: General SSLEngine problem"
        ],
        source_files=[
            "esmanager.log"
        ],
        recommendations=[
            "Verify if the thumbprint matches with the cert used for the Connection Server URL",
            "Ensure the FQDN used in the UAG configuration matches the Connection Server FQDN",
            "Verify a full certificate chain is present",
            "Verify connectivity between the Connection Server and the UAG",
        ],
        references=[
            "https://kb.omnissa.com/s/article/57161"
        ]
    ),
    Rule(
        name="UAG admin account is locked.",
        category="general",
        match_type="contains",
        patterns=[
            "UAG admin account is locked"
        ],
        source_files=[
            "admin.log"
        ],
        recommendations=[
            "Reset the UAG Admin Password",
        ],
        references=[
            "https://kb.omnissa.com/s/article/91516"
        ]
    ),
]