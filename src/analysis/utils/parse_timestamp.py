from datetime import timezone
from src.analysis.data.TIMESTAMP_PATTERNS import TIMESTAMP_PATTERNS

def parse_timestamp(raw_timestamp):
    if not raw_timestamp:
        return None
    
    for pattern, parser in TIMESTAMP_PATTERNS:
        match = pattern.match(raw_timestamp)

        if not match:
            continue

        try:
            timestamp = parser(match.group(0))

            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)

            return timestamp
        except ValueError:
            continue

    return None