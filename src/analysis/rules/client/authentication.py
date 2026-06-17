from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    Rule(
        name='Logging in with Horizon Client for Windows and using the "Log in as current user" option fails soon after the machine account password is changed',
        category="authentication",
        match_type="contains",
        patterns=[
            "[ws_winauth] [GSSApiProcessServerContext]: Negotiate failed. Error 0x8009030C",
            "[ws_winauth] [GSSApiCloseSecurityContext] Failed to locate requested context"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt"
        ],
        recommendations=[
            "This issue can occur when the client machine's computer account password is automatically updated while you are using a Horizon desktop and you try to reconnect using the Horizon Client Log in as current user option"
        ],
        references=[
            "https://kb.omnissa.com/s/article/2130795"
        ]
    ),
]