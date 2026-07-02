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
    ),
    Rule(
        name="Dynamic UDP ports exhaustion on Connection Server",
        is_version_specific= True,
        category="replication",
        match_type="contains",
        patterns=[
            'Exception in thread "dnsjava NIO selector"',
            "java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/97398"
        ]
    ),
    Rule(
        name="Unable to see virtual machines and the desktop configurations in the Horizon administration console after ADAM database maintenance",
        category="replication",
        match_type="contains",
        patterns=[
            "[LDAP: error code 32 - 0000208D: NameErr: DSID-03100288, problem 2001 (NO_OBJECT)",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/88536"
        ]
    ),
]