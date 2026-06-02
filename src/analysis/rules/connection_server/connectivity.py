from src.analysis.utils.rule_constructor import Rule

CONNECTIVITY_RULES = [
    Rule(
        name= "Unexpected Origin Found",
        category= "connectivity",
        match_type="regex",
        patterns= [
            r"ERROR.*Unexpected Origin:",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "Add the CSs, LBs and UAGs FQDNs to the locked.properties file",
        ],
        references= [
            "https://kb.omnissa.com/s/article/85801"
        ]
    ),
]