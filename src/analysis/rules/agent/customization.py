from src.analysis.utils.rule_constructor import Rule

CUSTOMIZATION_RULES = [
    Rule(
        name="Appx packages are  not provisioned for all users",
        category="customization",
        match_type="contains",
        patterns=[
            "was installed for a user, but not provisioned for all users. This package will not function properly in the sysprep image"
        ],
        source_files=[
            "setuperr.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/83985",
            "https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/sysprep-fails-remove-or-update-store-apps"
        ]
    ),
    Rule(
        name="Pending Windows updates",
        category="customization",
        match_type="contains",
        patterns=[
            "Error SYSPRP Sysprep_Clean_Validate_Opk: Audit mode can't be turned on if there is an active scenario",
            "Audit mode cannot be turned on if reserved storage is in use. An update or servicing operation may be using reserved storage"
        ],
        source_files=[
            "setuperr.log"
        ],
        recommendations=[
            "Run the Windows update on the parent VM and consider disabling Windows update service for Instant Clones"
        ],
        references=[
            "https://kb.omnissa.com/s/article/83985",
        ]
    ),
    Rule(
        name="AGENT_CUSTOMIZATION_FAULT - Internal template vm-XXXX customization failed Error Rename Failed In NGA Instant Clone Creation Error",
        category="customization",
        match_type="contains",
        patterns=[
            "customization failed. Rename Failed In NGA",
            "customization failed. Failed to set computer name in NGA",
            "Rename Failed In NGA. Cannot Continue",
            "Set guestinfo.it.CustomizationErrorDesc to Rename Failed In NGA"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90782",
        ]
    ),
    Rule(
        name="AGENT_CUSTOMIZATION_FAULT - Internal template vm-XXXX customization failed Error description not set by agent Instant Clone Creation Error",
        category="customization",
        match_type="contains",
        patterns=[
            "customization failed. Error description not set by agent"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90781",
        ]
    ),
    Rule(
        name="Instant Clone provisioning fails intermittently with: Agent Initialization state error(26):Failed to verify domain trust(waited 45 seconds)",
        category="customization",
        match_type="contains",
        patterns=[
            "not found in current site.Skipping trust verify with preferred dc"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/93066",
        ]
    ),
    Rule(
        name='[Nutanix]Horizon Agent Installation on Golden Image Fails with "Authentication (AuthSSPI) AcceptSecurityContext Failed" During Registration',
        is_version_specific= True,
        category="customization",
        match_type="contains",
        patterns=[
            "authentication failed, reason=authChannelDown"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/6001394",
        ]
    ),
]