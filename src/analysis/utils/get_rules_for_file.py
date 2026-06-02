import re

from src.analysis.parsers.rule_parser import rulesets

def get_rules_for_file(component, filename):
    rules = rulesets[component]

    active_rules = []

    for rule in rules:
        for source_file in rule.source_files:

            if source_file == filename:
                active_rules.append(rule)
                break

            if re.match(source_file, filename):
                active_rules.append(rule)
                break

    return active_rules