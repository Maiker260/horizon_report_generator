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
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[
            "This issue can occur when the client machine's computer account password is automatically updated while you are using a Horizon desktop and you try to reconnect using the Horizon Client Log in as current user option"
        ],
        references=[
            "https://kb.omnissa.com/s/article/2130795"
        ]
    ),
    Rule(
        name='Connecting to View Connection Server with SmartCard authentication enabled fails with the error: Smart Card or Certificate authentication is required',
        category="authentication",
        match_type="contains",
        patterns=[
            "IsValidCertificate: Cert didn't match a valid issuer. Skipping cert",
            "The View Connection Server connection failed. Smart Card or Certificate authentication is required"
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/2013044"
        ]
    ),
    Rule(
        name='TrueSSO - Public Key Infrastructure: Windows 11 Client Error "cannot utilize the smartcard subsystem" with Windows Hello for Business',
        category="authentication",
        match_type="contains",
        patterns=[
            "Failed to find a valid Whfb certificate",
        ],
        source_files=[
            r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt", r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90720"
        ]
    ),
]