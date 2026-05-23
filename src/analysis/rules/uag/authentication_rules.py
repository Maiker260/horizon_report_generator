AUTHENTICATION_RULES = [
    {
        "name": "SAML Validation Failed",
        "category": "authentication",
        "patterns": [
            "Error on performing SAML validation: SAML Assertion is valid between NotBefore"
        ],
        "recommendation": [
            "Check that UAG and Identity Provider time is in sync",
            "SAML assertion validity set in Identity Provider is enough to account for clock skew"
        ]
    },
]