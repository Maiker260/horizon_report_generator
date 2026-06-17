from src.analysis.utils.rule_constructor import Rule

UPGRADE_RULES = [
    Rule(
        name= "Horizon View Agent uninstall rolls back with a trustedinstaller service error message",
        category= "upgrade",
        match_type="contains",
        patterns= [
            "Failed to get the token for trustedinstaller service"
        ],
        source_files=[
            r"vminst.*\.log"
        ],
        recommendations= [
            "To resolve this issue, verify that the Windows Module Installer is not disabled during the uninstallation of View Agent"
        ],
        references= [
            "https://kb.omnissa.com/s/article/84450"
        ]
    ),
]