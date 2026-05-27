CUSTOMIZATION_RULES = [
    {
        "name": "Appx packages are  not provisioned for all users",
        "category": "customization",
        "patterns": [
            r"was installed for a user, but not provisioned for all users\. This package will not function properly in the sysprep image"
        ],
        "recommendations": [],
        "references": [
            "https://kb.omnissa.com/s/article/83985",
            "https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/sysprep-fails-remove-or-update-store-apps"
        ]
    },
    {
        "name": "Pending Windows updates",
        "category": "customization",
        "patterns": [
            r"Error SYSPRP Sysprep_Clean_Validate_Opk: Audit mode can\'t be turned on if there is an active scenario",
            r"Audit mode cannot be turned on if reserved storage is in use\. An update or servicing operation may be using reserved storage"
        ],
        "recommendations": [
            "Run the Windows update on the parent VM and consider disabling Windows update service for Instant Clones"
        ],
        "references": [
            "https://kb.omnissa.com/s/article/83985",
        ]
    },
]