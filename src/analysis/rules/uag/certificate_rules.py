CERTIFICATE_RULES = [
    {
        "name": "Certificate Upload Issue",
        "category": "certificates",
        "patterns": [
            "Failed to upload ESManager certificate"
        ],
        "recommendation": [
            "Check https://kb.omnissa.com/s/article/91732",
        ]
    },
    {
        "name": "Unexpected thumbprint on a Blast certificate",
        "category": "certificates",
        "patterns": [
            "Expected thumbprint is",
            "Actual thumbprint is",
            "Cannot verify target host"
        ],
        "recommendation": [
            "Check https://kb.omnissa.com/s/article/91732",
        ]
    },
]