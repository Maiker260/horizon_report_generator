from src.analysis.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.analysis.parsers.rule_parser import rule_parser
from src.analysis.utils.get_rules_for_file import get_rules_for_file

def analyze_logs(zip_ctx, component, progress_callback=None):
    files = FILES_OF_INTEREST[component]

    findings = {}
    MAX_SAMPLES = 3

    # File list for progress tracking
    all_matched_files = []

    for filename in files:
        is_pattern = any(
            char in filename
            for char in "^$.*+?[](){}|\\"
        )

        if is_pattern:
            all_matched_files.extend(
                zip_ctx.find_pattern(filename)
            )

        elif zip_ctx.exists(filename):
            all_matched_files.append(filename)

    total_files = len(all_matched_files)

    for index, matched_file in enumerate(
        all_matched_files,
        start=1
    ):
        if progress_callback:
            progress_callback(
                current=index,
                total=total_files,
                filename=matched_file
            )

        active_rules = get_rules_for_file(
            component,
            matched_file
        )

        with zip_ctx.open(matched_file) as file:
            reader = read_file_with_auto_encoding(file)

            for line in reader:
                line = line.strip()

                if not line:
                    continue

                result = rule_parser(line, active_rules, matched_file)

                if not result:
                    continue

                key = (
                    result["rule_name"],
                    result["category"]
                )

                timestamp = line.split()[0]

                if key not in findings:
                    findings[key] = {
                        "rule_name": result["rule_name"],
                        "source_files": {
                            result["source_file"]
                        },
                        "category": result["category"],
                        "recommendations": result["recommendations"],
                        "references": result["references"],
                        "occurrences": 1,
                        "first_line": timestamp,
                        "last_line": timestamp,
                        "samples": [line]
                    }

                else:
                    findings[key]["occurrences"] += 1

                    findings[key]["source_files"].add(
                        result["source_file"]
                    )

                    # Order Timestamps
                    if timestamp < findings[key]["first_line"]:
                        findings[key]["first_line"] = timestamp

                    if timestamp > findings[key]["last_line"]:
                        findings[key]["last_line"] = timestamp

                    # Group Samples
                    samples = findings[key]["samples"]

                    samples.append(line)

                    if len(samples) > MAX_SAMPLES:
                        samples.pop(0)

    return [
        {
            **finding,
            "source_files": sorted(
                finding["source_files"]
            )
        }
        for finding in findings.values()
    ]