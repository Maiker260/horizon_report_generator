from .format_result import format_result
from .is_replication_successful import is_replication_successful

def format_multiple_neighbors(naming_context, neighbors, naming_context_max_width):
    # Format a naming context with multiple replication neighbors.

    # Example:
    #     Configuration:
    #        - SERVER01: SUCCESSFUL (2026-07-15 15:53:19)
    #        - SERVER02: FAILED
    #           Last Attempt: 2026-07-15 15:53:19
    #           Result: 8456 (0x2108)
    #           Error: The source server is currently rejecting replication requests.

    indent = "   "
    content = [f"{indent}{naming_context}:"]

    for neighbor in neighbors:
        partner = neighbor.get("neighbor", "Unknown")
        status = neighbor.get("status", "UNKNOWN").upper()
        last_attempt = neighbor.get("last_attempt", "Unknown")

        # Successful replication
        if is_replication_successful(neighbor):
            content.append(
                f"{indent}   - {partner}: "
                f"{status} ({last_attempt})"
            )

            continue

        # Failed replication
        content.append(f"{indent}   - {partner}: {status}")

        content.extend(format_result(neighbor, indent=f"{indent}      "))

    return content