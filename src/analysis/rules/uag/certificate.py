CERTIFICATE_RULES = [
    {
        "name": "Certificate Upload Issue",
        "category": "certificate",
        "patterns": [
            "Failed to upload ESManager certificate"
        ],
        "recommendations": [],
        "references": [
            "https://kb.omnissa.com/s/article/91732"
        ]
    },
    {
        "name": "Unexpected thumbprint on a Blast certificate",
        "category": "certificate",
        "patterns": [
            "Expected thumbprint is",
            "Actual thumbprint is",
            "Cannot verify target host"
        ],
        "recommendations": [],
        "references": [
            "https://kb.omnissa.com/s/article/91732"
        ]
    },
]