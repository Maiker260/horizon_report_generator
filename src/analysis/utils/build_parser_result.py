def build_parser_result(rule, line, filename):
    return {
        "line_found": line,
        "source_file": filename,
        "rule_name": rule.name,
        "category": rule.category,
        "recommendations": rule.recommendations,
        "references": rule.references
    }