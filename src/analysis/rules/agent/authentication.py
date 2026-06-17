from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    Rule(
        name= "Certain Smartcards do not function due to an incompatibility with newer windows crypto modules in Horizon 8.4 and later",
        category= "authentication",
        match_type="contains",
        patterns= [
            "Error code is 0xc0000225. Is the card inserted?",
            "is reporting that it has no card present"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90634"
        ]
    ),
]