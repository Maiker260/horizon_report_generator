from src.summary.utils.report_sections.replication.is_replication_successful import is_replication_successful
from src.summary.utils.report_sections.replication.format_context import format_context
from src.summary.utils.report_sections.replication.normalize_partner import normalize_partner

REPLICATION_SECTIONS = {
    "inbound": "Inbound",
    "outbound": "Outbound",
}

REPLICATION_LABELS = {
    "DSA Options": "DSA Options",
    "Site Options": "Site Options",
}

def build_replication_section(title, replication_data):
    partners = replication_data.get("neighbors", [])
    dsa_options = replication_data.get("DSA Options")
    site_options = replication_data.get("Site Options")

    title_indent = "   "
    sub_content_indent = "     "

    # Overall status
    overall_status = "HEALTHY"

    if dsa_options not in (None, "None") or site_options not in (None, "None"):
        overall_status = "REPLICATION DISABLED"

    elif (
        any(
            not is_replication_successful(neighbor)
            for section in REPLICATION_SECTIONS
            for neighbors in replication_data.get(section, {}).values()
            for neighbor in neighbors
        )
    ):
        overall_status = "FAILED"

    content = [
        title,
        "-" * len(title),
        "",
    ]

    # No neighbors
    if not partners:
        content.append("   * No replication neighbors found.")

        return content

    # Title
    content.extend([
        f"{title_indent}Overall Status:  {overall_status}",
        "",
    ])

    # Replication summary
    max_width = max(
        len(label)
        for label in REPLICATION_LABELS.values()
    )

    content.append(f"{title_indent}Replication:")

    content.extend([
        (
            f"{sub_content_indent}{REPLICATION_LABELS['DSA Options'] + ":":<{max_width + 1}} "
            f"{dsa_options}"
        ),
        (
            f"{sub_content_indent}{REPLICATION_LABELS['Site Options'] + ":":<{max_width + 1}} "
            f"{site_options}"
        ),
        "",
        f"{title_indent}Neighbors ({len(partners)}):",
    ])

    # Normalize Neighbor's Name
    content.extend(
        f"{sub_content_indent}- {normalize_partner(partner)}"
        for partner in partners
    )

    # Inbound / Outbound
    for section_key, section_title in REPLICATION_SECTIONS.items():
        section_data = replication_data.get(section_key, {})

        if not section_data:
            continue

        naming_context_max_width = max(
            len(name)
            for name in section_data
        )

        content.append("")
        content.append(f"{title_indent}{section_title}:")

        for naming_context, neighbors in section_data.items():
            if not neighbors:
                continue

            has_failure = any(
                not is_replication_successful(neighbor)
                for neighbor in neighbors
            )

            content.extend(
                format_context(naming_context, neighbors, naming_context_max_width, sub_content_indent)
            )

            if has_failure and naming_context != list(section_data.keys())[-1]:
                            content.append("")

    return content