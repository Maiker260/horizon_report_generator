import datetime

def update_findings(findings, result, line, timestamp):
    key = (result["rule_name"], result["category"])

    finding = findings.get(key)

    if finding is None:
        findings[key] = {
            "rule_name": result["rule_name"],
            "source_files": {result["source_file"]},
            "category": result["category"],
            "recommendations": result["recommendations"],
            "references": result["references"],
            "occurrences": 1,
            "first_line": timestamp,
            "last_line": timestamp,
            "samples": [(timestamp, line)]
            # "samples": [line]
        }
    else:
        finding["occurrences"] += 1
        finding["source_files"].add(result["source_file"])

        if timestamp is not None:
            if finding["first_line"] is None or timestamp < finding["first_line"]:
                finding["first_line"] = timestamp

            if finding["last_line"] is None or timestamp > finding["last_line"]:
                finding["last_line"] = timestamp

        finding["samples"].append((timestamp, line))
        finding["samples"].sort(key=lambda x: x[0] or datetime.min)
        finding["samples"] = finding["samples"][-3:]