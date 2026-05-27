CERTIFICATE_RULES = [
    {
        "name": "VDPCONNECT_CONNECT_TLS",
        "category": "certificate",
        "patterns": [
            "VDPCONNECT_CONNECT_TLS",
        ],
        "recommendations": [
            "This error typically indicates that a certificate issue is impeding connection",
            "In the Client, try setting the 'Certificate Checking Mode' to 'Do not verify server identity certificates'"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/91018"
        ]
    },
]