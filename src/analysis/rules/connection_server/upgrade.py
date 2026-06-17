from src.analysis.utils.rule_constructor import Rule

UPGRADE_RULES = [
    Rule(
        name= "Horizon Connection Server Upgrade fails with LDAP bind failed (Strong Authentication Required)",
        category= "upgrade",
        match_type="contains",
        patterns= [
            "LDAP bind failed (Strong Authentication Required)",
            "ERROR: Could not acquire schema master lock."
        ],
        source_files=[
            r"vminst.*\.log"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/95186"
        ]
    ),
    Rule(
        name= "Upgrading connection server fails with error code 28018 and error message: AD LDS Setup was cancelled",
        category= "upgrade",
        match_type="contains",
        patterns= [
            "Error 28018. There was an error creating a Microsoft Directory Services instance. 'AD LDS Setup was cancelled.'",
        ],
        source_files=[
            r"vminst.*\.log"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/80464"
        ]
    ),
]