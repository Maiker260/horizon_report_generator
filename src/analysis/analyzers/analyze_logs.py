from src.analysis.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.analysis.parsers.rule_parser import rule_parser
from src.analysis.utils.parse_timestamp import parse_timestamp
from src.analysis.utils.extract_timestamp_raw import extract_timestamp_raw
from .resolve_files import resolve_files
from .build_engine import build_engine
from .update_findings import update_findings

def analyze_logs(zip_ctx, component, progress_callback=None):
    files = FILES_OF_INTEREST[component]
    all_matched_files = resolve_files(zip_ctx, files)

    automaton, regex_rules = build_engine(component)

    findings = {}

    for index, matched_file in enumerate(all_matched_files, start=1):
        if progress_callback:
            progress_callback(index, len(all_matched_files), matched_file)

        with zip_ctx.open(matched_file) as file:
            reader = read_file_with_auto_encoding(file)

            last_timestamp_raw = None
            last_timestamp = None

            for line in reader:
                line = line.strip()
                if not line:
                    continue

                first = line[0]
                if first in "0123456789[":
                    raw = extract_timestamp_raw(line)
                else:
                    raw = None

                if raw and raw != last_timestamp_raw:
                    last_timestamp_raw = raw
                    last_timestamp = parse_timestamp(raw)

                result = rule_parser(
                    line,
                    automaton,
                    regex_rules,
                    matched_file
                )
                
                if result:
                    update_findings(
                        findings,
                        result,
                        line,
                        last_timestamp
                    )

    return [
        {
            **f,
            "source_files": sorted(f["source_files"])
        }
        for f in findings.values()
    ]