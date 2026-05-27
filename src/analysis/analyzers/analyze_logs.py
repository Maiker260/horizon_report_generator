from src.analysis.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.analysis.parsers.rule_parser import rule_parser

def analyze_logs(zip_ctx, component):
    files = FILES_OF_INTEREST[component]
    data = []

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
             with zip_ctx.open(matched_file) as file:
                content = read_file_with_auto_encoding(file)

                for line in content.splitlines():
                    line = line.strip()

                    if not line:
                        continue

                    result = rule_parser(line, component, matched_file)

                    if result:
                        data.append(result)

    return data