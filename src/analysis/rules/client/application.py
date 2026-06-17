from src.analysis.utils.rule_constructor import Rule

APPLICATION_RULES = [
    Rule(
        name="Windows Omnissa Horizon Client crashes upon startup due to downgrade of Microsoft library",
        category="application",
        match_type="contains",
        patterns=[
            "rmksProbeMgrTimer ExceptionAddress 0x7ff8906eb93c eflags 0x00010286",
            "rmksProbeMgrTimer ----Win32 exception detected, exceptionCode 0xc0000005 (access violation)----"
        ],
        source_files=[
            r"horizon-crtbora.*\.log"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/6000987"
        ]
    ),
]