import re
from datetime import datetime

CURRENT_YEAR = datetime.now().year

TIMESTAMP_PATTERNS = [

    # 2026-06-16T11:38:21.124-07:00
    # 2026-06-16T11:38:21-07:00
    # 2026-06-16T11:38:21.124Z
    (
        re.compile(
            r"^\d{4}-\d{2}-\d{2}"
            r"T\d{2}:\d{2}:\d{2}"
            r"(?:\.\d+)?"
            r"(?:Z|[+-]\d{2}:\d{2})"
        ),
        lambda s: datetime.fromisoformat(
            s.replace("Z", "+00:00")
        )
    ),

    # 2026-06-16T11:38:21.124
    # 2026-06-16T11:38:21
    (
        re.compile(
            r"^\d{4}-\d{2}-\d{2}"
            r"T\d{2}:\d{2}:\d{2}"
            r"(?:\.\d+)?"
        ),
        lambda s: datetime.fromisoformat(s)
    ),

    # 2026-06-16 11:38:21.124
    # 2026-06-16 11:38:21
    (
        re.compile(
            r"^\d{4}-\d{2}-\d{2}"
            r"\s+\d{2}:\d{2}:\d{2}"
            r"(?:\.\d+)?"
        ),
        lambda s: datetime.fromisoformat(s)
    ),

    # [2026-06-16 11:38:21.124]
    # [2026-06-16 11:38:21]
    (
        re.compile(
            r"^\[\d{4}-\d{2}-\d{2}"
            r"\s+\d{2}:\d{2}:\d{2}"
            r"(?:\.\d+)?\]"
        ),
        lambda s: datetime.fromisoformat(
            s.strip("[]")
        )
    ),

    # 06/16 11:38:21,124+0000
    (
        re.compile(
            r"^\d{2}/\d{2}"
            r"\s+\d{2}:\d{2}:\d{2}"
            r",\d+"
            r"\+\d{4}"
        ),
        lambda s: datetime.strptime(
            s,
            "%m/%d %H:%M:%S,%f%z"
        ).replace(year=CURRENT_YEAR)
    ),

    # Jun 16 11:38:21
    (
        re.compile(
            r"^[A-Z][a-z]{2}"
            r"\s+\d{1,2}"
            r"\s+\d{2}:\d{2}:\d{2}"
        ),
        lambda s: datetime.strptime(
            f"{CURRENT_YEAR} {s}",
            "%Y %b %d %H:%M:%S"
        )
    ),

    # 16/Jun/2026:11:38:21 -0700
    (
        re.compile(
            r"^\d{1,2}/[A-Z][a-z]{2}/\d{4}"
            r":\d{2}:\d{2}:\d{2}"
            r"\s+[+-]\d{4}"
        ),
        lambda s: datetime.strptime(
            s,
            "%d/%b/%Y:%H:%M:%S %z"
        )
    ),
]