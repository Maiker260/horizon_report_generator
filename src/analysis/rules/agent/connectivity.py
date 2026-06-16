from src.analysis.utils.rule_constructor import Rule

CONNECTIVITY_RULES = [
    Rule(
        name= "Agent secure pairing fails: No Network Communication between the View Agent and Connection Server",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Message could not be validated: Signature invalid for identity broker/broker",
            "java.lang.Exception: Identity validation failed: UNKNOWN is not known identity for: null"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "For affected customers uninstall Dynatrace OneAgent from the connection server machine",
        ],
        references= [
            "https://kb.omnissa.com/s/article/89582"
        ]
    ),
]