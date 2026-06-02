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
]