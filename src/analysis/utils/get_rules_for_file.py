import re
from src.analysis.rulesets.uag_ruleset import UAG_RULESET
from src.analysis.rulesets.cs_ruleset import CONNECTION_SERVER_RULESET
from src.analysis.rulesets.agent_ruleset import AGENT_RULESET
from src.analysis.rulesets.client_ruleset import CLIENT_RULESET

rulesets = {
    "unified_access_gateway": UAG_RULESET,
    "connection_server": CONNECTION_SERVER_RULESET,
    "agent": AGENT_RULESET,
    "client": CLIENT_RULESET,
}

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