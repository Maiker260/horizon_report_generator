from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    Rule(
        name="SAML Validation Failed",
        category="authentication",
        match_type="contains",
        patterns=[
            "Error on performing SAML validation: SAML Assertion is valid between NotBefore"
        ],
        source_files=[
            "esmanager.log"
        ],
        recommendations=[
            "Check that the UAG and Identity Provider time is in sync",
            "Check the UAG's NTP configuration"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91564"
        ]
    ),
    Rule(
        name="Radius Server timeout cannot be set longer than 120 seconds",
        category="authentication",
        match_type="contains",
        patterns=[
            "Message: radius-auth:The value of (Number of Attempts"
        ],
        source_files=[
            "admin.log"
        ],
        recommendations=[
            "The timeout value should be set within 120 seconds"
        ],
        references=[
            "https://kb.omnissa.com/s/article/93056"
        ]
    ),
    Rule(
        name="Unified Access Gateway (UAG): “Authentication method could not be configured” error when configuring RSA SecurID settings on UAG",
        category="authentication",
        match_type="contains",
        patterns=[
            "ERROR utils.SecurIDRestClient: Connection refused by server"
        ],
        source_files=[
            "authbroker.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/88003"
        ]
    ),
    Rule(
        name="Unified Access Gateway(UAG): Access Denied with RADIUS authentication and ERROR_AUTHENTICATOR logline",
        category="authentication",
        match_type="contains",
        patterns=[
            "impl.RadiusClientImpl: Login for username failed (received a bad packet from the RADIUS server) Error code = 5 Error message = ERROR_AUTHENTICATOR"
        ],
        source_files=[
            "authbroker.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/87337"
        ]
    ),
]