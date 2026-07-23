from src.summary.parsers.connection_server.replication.PATTERNS import SUCCESSFUL_ATTEMPT_PATTERN, FAILED_ATTEMPT_PATTERN
from src.summary.parsers.connection_server.replication.parsers.is_replication_error_line import is_replication_error_line

def parse_replication_attempt(line, current_section, current_nc, current_partner, current_attempt, data):
    # Parse successful and failed replication attempts.

    if not current_nc or not current_partner:
        return current_attempt

    # Successful attempt
    success_match = SUCCESSFUL_ATTEMPT_PATTERN.search(line)

    if success_match:

        timestamp = success_match.group(1)

        data[current_section][current_nc].append({
            "neighbor": current_partner,
            "status": "SUCCESSFUL",
            "last_attempt": timestamp,
            "result": None,
            "error": None,
        })

        return None

    # Failed attempt
    failed_match = FAILED_ATTEMPT_PATTERN.search(line)

    if failed_match:

        data["replication_errors"] = True

        return {
            "neighbor": current_partner,
            "status": "FAILED",
            "last_attempt": failed_match.group(1),
            "result": int(failed_match.group(2)),
            "result_hex": failed_match.group(3),
            "error": None,
        }

    # Failed attempt error description
    if current_attempt:

        if is_replication_error_line(line):

            current_attempt["error"] = line

            data[current_section][current_nc].append(
                current_attempt
            )

            return None

    return current_attempt