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
    Rule(
        name='Error: "USB redirection is not available for this desktop" on a Horizon View desktop',
        category="feature",
        match_type="contains",
        patterns=[
            "because the USB component is not available in the agent.",
        ],
        source_files=[
            r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/93745"
        ]
    ),
    Rule(
        name="Printers not mapping on the first attempt when logging into a Horizon desktop",
        category="feature",
        match_type="contains",
        patterns=[
            "UemState not DONE within 120 seconds",
        ],
        source_files=[
            r"print_service_.*\.log",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/89172"
        ]
    ),
    Rule(
        name="Omnissa Integrated Printing PrintUtils::GetDeviceCapabilities failed",
        category="feature",
        match_type="contains",
        patterns=[
            "PrintUtils::GetDeviceCapabilities failed",
        ],
        source_files=[
            r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/92339"
        ]
    ),
]