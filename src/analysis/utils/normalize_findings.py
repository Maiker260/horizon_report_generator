def normalize_findings(data):
    normalized_data = {}

    for finding in data:
        rule_name = finding["rule_name"]

        if rule_name not in normalized_data:
            normalized_data[rule_name] = {
                **finding,
                "occurrences": 1
            }

        else:
            normalized_data[rule_name]["occurrences"] += 1

    return list(normalized_data.values())