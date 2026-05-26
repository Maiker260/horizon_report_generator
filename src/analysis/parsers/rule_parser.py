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

def rule_parser(line, component, filename):
    rules = rulesets[component]

    for rule in rules:
        for pattern in rule["compiled_patterns"]:
            if pattern.search(line):
                return {
                    "line_found": line,
                    "source_file": filename,
                    "rule_name": rule["name"],
                    "category": rule["category"],
                    "recommendations": rule.get("recommendations", []),
                    "references": rule.get("references", [])
                }
    
    return None