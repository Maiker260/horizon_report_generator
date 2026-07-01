from src.analysis.utils.rule_constructor import Rule

CLOUD_POD_RULES = [
    Rule(
        name='Logs contain "Failed to obtain UPN for user" error when the Cloud Pod Architecture feature is enabled',
        category="cpa",
        match_type="contains",
        patterns=[
            "Error while obtaining token groups: Failed to obtain UPN for user",
            "Error while obtaining token groups: Failed to get login token"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/2111547"
        ]
    ),
    Rule(
        name='Unable to launch desktop from another pod after upgrading a pod to 2306 or 2309, getting error "This desktop is currently not available."',
        is_version_specific= True,
        category="cpa",
        match_type="contains",
        patterns=[
            "unsuccessful, will continue trying. Launch error: null",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/96153"
        ]
    ),
    Rule(
        name='Global Entitlements: When end users log in to a Cloud Pod Architecture enabled environment, some or all of their global entitlements are missing',
        is_version_specific= True,
        category="cpa",
        match_type="regex",
        patterns=[
            r"LMV: Can't broker .* as it is restricted by tag policy",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/6000943"
        ]
    ),
]