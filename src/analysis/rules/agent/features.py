from src.analysis.utils.rule_constructor import Rule

FEATURES_RULES = [
    Rule(
        name= 'Error: "USB redirection is not available for this desktop" on a Horizon View desktop when logon time exceeds 60 seconds',
        category= "features",
        match_type="contains",
        patterns= [
            "Can't get a valid sessionId within 60 seconds for channel"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/74931"
        ]
    ),
    Rule(
        name= "RDSH Apps do not redirect/map Printers with Omnissa Integrated Printing",
        category= "features",
        match_type="regex",
        patterns= [
            r'AddPort: OpenPrinter\(\) failed for .* \(err=1801\)'
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/94372"
        ]
    ),
]