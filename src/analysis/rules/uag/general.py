GENERAL_RULES = [
    {
        "name": "UAG admin console shows 'Horizon destination server' as down/red",
        "category": "general",
        "patterns": [
            r"javax\.net\.ssl\.SSLHandshakeException: General SSLEngine problem"
        ],
        "recommendations": [
            "Verify if the thumbprint matches with the cert used for the Connection Server URL",
            "Ensure the FQDN used in the UAG configuration matches the Connection Server FQDN",
            "Verify a full certificate chain is present",
            "Verify connectivity between the Connection Server and the UAG",
        ],
        "references": [
            "https://kb.omnissa.com/s/article/57161"
        ]
    },
    {
        "name": "UAG admin account is locked.",
        "category": "general",
        "patterns": [
            r"UAG admin account is locked"
        ],
        "recommendations": [
            "Reset the UAG Admin Password",
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91516"
        ]
    },
]