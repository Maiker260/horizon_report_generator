import re

def compile_rules(rules):
    for rule in rules:
        rule["compiled_patterns"] = [
            re.compile(pattern, re.IGNORECASE) for pattern in rule["patterns"]
        ]

    return rules