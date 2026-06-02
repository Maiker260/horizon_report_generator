from src.analysis.utils.rule_constructor import Rule

CERTIFICATE_RULES = [
    Rule(
        name="Certificate Upload Issue",
        category="certificate",
        match_type="contains",
        patterns=[
            "Failed to upload ESManager certificate"
        ],
        source_files=[
            "admin.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/91732"
        ]
    ),
    Rule(
        name="Unexpected thumbprint on a Blast certificate",
        category="certificate",
        patterns=[
            "Expected thumbprint is",
            "Actual thumbprint is",
            "Cannot verify target host"
        ],
        source_files=[
            "bsg.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/91732"
        ]
    ),
]