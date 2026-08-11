from src.analysis.utils.rule_constructor import Rule

FEATURES_RULES = [
    Rule(
        name='Horizon Client USB redirection fails with "Unexpected certificate thumbprint algorithm SHA-512"',
        category="feature",
        match_type="contains",
        patterns=[
            "Unexpected certificate thumbprint algorithm 'SHA-512'",
        ],
        source_files=[
            r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "Upgrade the Horizon Client version to 2111 or later or alternatively",
            "Enable USB over a virtual channel if you cannot upgrade the client."
        ],
        references=[
            "https://kb.omnissa.com/s/article/90330"
        ]
    ),
]