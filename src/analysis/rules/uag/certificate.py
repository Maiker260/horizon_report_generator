CERTIFICATE_RULES = [
    {
        "name": "Certificate Upload Issue",
        "category": "certificate",
        "patterns": [
            r"Failed to upload ESManager certificate"
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
            r"Expected thumbprint is",
            r"Actual thumbprint is",
            r"Cannot verify target host"
        ],
        "recommendations": [],
        "references": [
            "https://kb.omnissa.com/s/article/91732"
        ]
    },
]