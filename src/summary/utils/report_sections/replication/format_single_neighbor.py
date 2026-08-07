from .format_result import format_result
from .is_replication_successful import is_replication_successful

def format_single_neighbor(naming_context, neighbor, naming_context_max_width, sub_content_indent):
    # Format a naming context with a single replication neighbor.

    # Successful:
    #     Configuration: SUCCESSFUL (2026-07-15 15:53:19)

    # Failed:
    #     Configuration: FAILED
    #        Last Attempt: 2026-07-15 15:53:19
    #        Result: 8456 (0x2108)
    #        Error: The source server is currently rejecting replication requests.

    content = []

    status = neighbor.get("status", "UNKNOWN").upper()
    last_attempt = neighbor.get("last_attempt","Unknown")

    # Successful replication
    if is_replication_successful(neighbor):
        content.append(f"{sub_content_indent}{naming_context + ':':<{naming_context_max_width + 1}}  {status} ({last_attempt})")

        return content

    # Failed replication
    content.append(f"{sub_content_indent}{naming_context}: {status}")

    content.extend(format_result(neighbor, indent=f"{sub_content_indent}   ",))

    return content