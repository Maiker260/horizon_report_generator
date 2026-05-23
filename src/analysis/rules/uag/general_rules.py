GENERAL_RULES = [
    {
        "name": "UAG admin console shows 'Horizon destination server' as down/red",
        "category": "general",
        "patterns": [
            "javax.net.ssl.SSLHandshakeException: General SSLEngine problem"
        ],
        "recommendation": [
            "Verify if the thumbprint matches with the cert used for the connection server URL",
            "Ensure the address used in the UAG configuration matches the connection server certificate and URL",
            "Verify a full certificate chain is present"
            "Check https://kb.omnissa.com/s/article/57161",
        ]
    },
    {
        "name": "UAG admin account is locked.",
        "category": "general",
        "patterns": [
            "UAG admin account is locked"
        ],
        "recommendation": [
            "Reset the UAG Admin Password",
            "Check https://kb.omnissa.com/s/article/91516",
        ]
    },
]