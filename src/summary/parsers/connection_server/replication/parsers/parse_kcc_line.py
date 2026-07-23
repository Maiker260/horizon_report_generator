from src.summary.parsers.connection_server.replication.PATTERNS import KCC_CONNECTION_PATTERN

def parse_kcc_line(line, data):
    # Parse KCC connection and failure information.

    # KCC connection
    connection_match = KCC_CONNECTION_PATTERN.match(line)

    if connection_match:

        data["kcc_connections"] += 1

        return

    # No KCC failures
    if line == "No Failures.":

        data["kcc_failures"] = None

        return

    # KCC failures
    line_lower = line.lower()

    if (
        "consecutive failures" in line_lower
        or line_lower.startswith("last error:")
        or "failure" in line_lower
        or "failed" in line_lower
    ):
        data["kcc_failures"] = line