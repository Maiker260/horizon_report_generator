import re

def compile_rules(rules):
    for rule in rules:
        if rule.match_type == "regex":
            rule.compiled_patterns = [
                re.compile(pattern, re.IGNORECASE)
                for pattern in rule.patterns
            ]
        
        elif rule.match_type == "contains":
            rule.lower_patterns = [
                pattern.lower()
                for pattern in rule.patterns
            ]

    return rules