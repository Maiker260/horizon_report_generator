from src.analysis.utils.rule_constructor import Rule

MS_TEAMS_RULES = [
    Rule(
        name="Hosts file is missing 'view-localhost'",
        category="ms_teams",
        match_type="contains",
        patterns=[
            "getaddrinfo failed for host view-localhost: No such host is known"
        ],
        source_files=[
            r".*-html5Server-.*\.log"
        ],
        recommendations=[
            "The entry '127.0.0.1 view-localhost' is missing from your hosts file"
        ],
        references=[
            "https://techzone.omnissa.com/resource/microsoft-teams-optimization-horizon#conflicting-agent-installation:~:text=reinstall%20Microsoft%20Teams.-,Virtual%20desktop%20hosts%20file%20is%20missing%20%E2%80%9Cview%2Dlocalhost%E2%80%9D,-During%20Horizon%20Agent"
        ]
    ),
    Rule(
        name="Microsoft Teams is running in fallback mode",
        category="ms_teams",
        match_type="regex",
        patterns=[
            r"HTML5Server::OnAcceptWebSocketConn.*rejected due to different session"
        ],
        source_files=[
            r".*-html5Server-.*\.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/92620"
        ]
    ),
]