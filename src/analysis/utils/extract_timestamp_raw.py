from src.analysis.data.TIMESTAMP_PATTERNS import TIMESTAMP_PATTERNS

def extract_timestamp_raw(line):
    for pattern, _ in TIMESTAMP_PATTERNS:
        match = pattern.match(line)

        if match:
            return match.group(0)

    return None