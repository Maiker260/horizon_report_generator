from src.analysis.utils.build_parser_result import build_parser_result

def rule_parser(line, automaton, regex_rules, filename):
    line_lower = line.lower() if automaton else line

    for _, (rule, _) in automaton.iter(line_lower):
        return build_parser_result(
            rule,
            line,
            filename
        )

    for rule in regex_rules:
        for pattern in rule.compiled_patterns:
            if pattern.search(line):
                return build_parser_result(
                    rule,
                    line,
                    filename
                )
    return None