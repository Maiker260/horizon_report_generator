from src.analysis.utils.rule_constructor import Rule

REPLICATION_RULES = [
    Rule(
        name="Insufficient attributes were given to create an object",
        category="replication",
        match_type="contains",
        patterns=[
            "Insufficient attributes where given to create an object. This object may not exist because it may have been deleted and already garbage collected"
        ],
        source_files=[
            "ldap_replica_status.txt"
        ],
        recommendations=[
            "To resolve the issue, uninstall and reinstall the connection server on which replication is failing",
        ],
        references=[
            "https://kb.omnissa.com/s/article/2091974"
        ]
    )
]