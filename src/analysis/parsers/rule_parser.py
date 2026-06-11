from src.analysis.rulesets.uag_ruleset import UAG_RULESET
from src.analysis.rulesets.cs_ruleset import CONNECTION_SERVER_RULESET
from src.analysis.rulesets.agent_ruleset import AGENT_RULESET
from src.analysis.rulesets.client_ruleset import CLIENT_RULESET
from src.analysis.utils.build_parser_result import build_parser_result

rulesets = {
    "unified_access_gateway": UAG_RULESET,
    "connection_server": CONNECTION_SERVER_RULESET,
    "agent": AGENT_RULESET,
    "client": CLIENT_RULESET,
}

def rule_parser(line, rules, filename):
    line_lower = line.lower()

    for rule in rules:
        if rule.match_type == "contains":
            for pattern in rule.lower_patterns:
                if pattern in line_lower:
                    return build_parser_result(rule, line, filename)

        elif rule.match_type == "regex":
            for pattern in rule.compiled_patterns:
                if pattern.search(line):
                    return build_parser_result(rule, line, filename)

    return None