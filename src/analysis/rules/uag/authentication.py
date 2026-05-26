AUTHENTICATION_RULES = [
    {
        "name": "SAML Validation Failed",
        "category": "authentication",
        "patterns": [
            r"Error on performing SAML validation\: SAML Assertion is valid between NotBefore"
        ],
        "recommendations": [
            "Check that the UAG and Identity Provider time is in sync",
            "Check the UAG's NTP configuration"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91564"
        ]
    },
]