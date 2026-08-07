from .format_result import format_result
from .is_replication_successful import is_replication_successful

def format_multiple_neighbors(naming_context, neighbors, naming_context_max_width, sub_content_indent):
    # Format a naming context with multiple replication neighbors.

    # Example:
    #     Configuration:
    #        - SERVER01: SUCCESSFUL (2026-07-15 15:53:19)
    #        - SERVER02: FAILED
    #           Last Attempt: 2026-07-15 15:53:19
    #           Result: 8456 (0x2108)
    #           Error: The source server is currently rejecting replication requests.


    # Count successful neighbors
    successful = sum(
        is_replication_successful(neighbor)
        for neighbor in neighbors
    )

    total = len(neighbors)
    has_failures = successful != total

    status = "SUCCESSFUL" if not has_failures else ""

    context = (
        f"{naming_context + ':':<{naming_context_max_width + 1}}"
        if not has_failures
        else f"{naming_context}:"
    )

    status_count = f" ({successful}/{total})" if not has_failures else ""

    content = [
        f"{sub_content_indent}{context}  {status}{status_count}"
    ]

    # Nothing else to show if everything succeeded
    if not has_failures:
        return content

    # content.append("")

    sorted_neighbors = sorted(
        neighbors,
        key=lambda n: (
            0 if is_replication_successful(n) else 1,
            n.get("neighbor", ""),
        )
    )

    for neighbor in sorted_neighbors:
        partner = neighbor.get("neighbor", "Unknown")
        state = neighbor.get("status", "UNKNOWN").upper()
        last_attempt = neighbor.get("last_attempt", "Unknown")

        if partner != "Unknown":
            partner = partner.split("$")[0]

        if is_replication_successful(neighbor):
            content.append(
                f"{sub_content_indent}   - "
                f"{partner}: {state} ({last_attempt})"
            )
        else:
            content.append(
                f"{sub_content_indent}   - "
                f"{partner}: {state}"
            )

            content.extend(
                format_result(neighbor, indent=f"{sub_content_indent}      ")
            )

    return content