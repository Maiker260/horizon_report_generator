CONNECTION_SERVER_RULES = [
    {
        "name": "Insufficient attributes were given to create an object",
        "category": "replication",
        "patterns": [
            "Insufficient attributes where given to create an object. This object may not exist because it may have been deleted and already garbage collected"
        ],
        "recommendation": [
            "To resolve the issue, uninstall and reinstall the connection server on which replication is failing",
            "Check: https://kb.omnissa.com/s/article/2091974",
        ]
    },
    {
        "name": "Unexpected Origin Found",
        "category": "connectivity",
        "patterns": [
            "Unexpected Origin",
        ],
        "recommendation": [
            "Add the CSs, LBs and UAGs FQDNs to the locked.properties file",
            "Check: https://kb.omnissa.com/s/article/85801",
        ]
    },
]

