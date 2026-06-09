from src.analysis.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.analysis.parsers.rule_parser import rule_parser
from src.analysis.utils.get_rules_for_file import get_rules_for_file

# Test
# import time

def analyze_logs(zip_ctx, component):
    files = FILES_OF_INTEREST[component]

    findings = {}
    MAX_SAMPLES = 3

    # Test
    # total_read_time = 0
    # total_regex_time = 0
    # total_lines = 0
    # total_matches = 0

    for filename in files:
        is_pattern = any(char in filename for char in "^$.*+?[](){}|\\")

        if is_pattern:
            matched_files = zip_ctx.find_pattern(filename)

            if not matched_files:
                continue

        else:
            if not zip_ctx.exists(filename):
                continue

            matched_files = [filename]

        for matched_file in matched_files:

            active_rules = get_rules_for_file(
                component,
                matched_file
            )

            # Test
            # print(
            #     f"{matched_file}: "
            #     f"{len(active_rules)} active rules"
            # )

            with zip_ctx.open(matched_file) as file:

                # Test
                # t0 = time.perf_counter()

                content = read_file_with_auto_encoding(file)

                # Test
                # total_read_time += time.perf_counter() - t0

                for line in content.splitlines():
                    line = line.strip()

                    if not line:
                        continue

                    # Test
                    # t0 = time.perf_counter()

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

                    # Test
                    # total_regex_time += time.perf_counter() - t0
                    # total_lines += 1
    
    # Test
    # print(f"Lines processed: {total_lines}")
    # print(f"Matches found: {total_matches}")
    # print(f"Read time: {total_read_time:.3f}s")
    # print(f"Regex time: {total_regex_time:.3f}s")

    return [
        {
            **finding,
            "source_files": sorted(
                finding["source_files"]
            )
        }
        for finding in findings.values()
    ]