from src.summary.utils.report_sections.replication.is_replication_successful import is_replication_successful
from src.summary.utils.report_sections.replication.format_context import format_context

REPLICATION_SECTIONS = {
    "inbound": "Inbound",
    "outbound": "Outbound",
}

REPLICATION_LABELS = {
    "transport": "Transport:",
    "kcc_connections": "KCC Connections:",
    "kcc_failures": "KCC Failures:",
    "replication_errors": "Replication Errors:",
}

def replication(data, component, letter):
    replication_data = data.get("replication_status") or {}

    if not replication_data:
        return ""

    partners = replication_data.get("neighbors", [])
    transport = replication_data.get("transport") or "Unknown"
    kcc_connections = replication_data.get("kcc_connections",0)
    kcc_failures = replication_data.get("kcc_failures")
    replication_errors = replication_data.get("replication_errors")

    # Overall status
    overall_status = "HEALTHY"

    for section in REPLICATION_SECTIONS:
        section_data = replication_data.get(section, {})

        for neighbors in section_data.values():
            for neighbor in neighbors:
                if not is_replication_successful(neighbor):
                    overall_status = "FAILED"
                    break

            if overall_status == "FAILED":
                break

        if overall_status == "FAILED":
            break

    if kcc_failures or replication_errors:
        overall_status = "FAILED"

    # Title
    content = [
        f"\n\n\n{letter}. REPLICATION STATUS",
        "-" * 30,
        "",
    ]

    # No neighbors
    if not partners:
        content.append("   * No replication neighbors found.")

        return "\n".join(content).rstrip()

    # Replication summary
    max_width = max(
        len(label)
        for label in REPLICATION_LABELS.values()
    )

    content.append(f"Overall Status:  {overall_status}\n")
    content.append("Replication:")

    content.extend([
        (
            f"   {REPLICATION_LABELS['transport']:<{max_width + 1}} "
            f"{transport}"
        ),
        (
            f"   {REPLICATION_LABELS['kcc_connections']:<{max_width + 1}} "
            f"{kcc_connections}"
        ),
        (
            f"   {REPLICATION_LABELS['kcc_failures']:<{max_width + 1}} "
            f"{kcc_failures or 'None'}"
        ),
        (
            f"   {REPLICATION_LABELS['replication_errors']:<{max_width + 1}} "
            f"{replication_errors or 'None'}"
        ),
    ])

    # Neighbors
    content.append("")
    content.append("Neighbors:")

    content.extend(
        f"   - {partner}"
        for partner in partners
    )

    # Inbound / Outbound
    for section_key, section_title in REPLICATION_SECTIONS.items():

        section_data = replication_data.get(section_key, {})

        if not section_data:
            continue

        naming_context_max_width = max(
            len(naming_context)
            for naming_context in section_data
        )

        content.extend([
            "",
            f"{section_title}:",
        ])

        for naming_context, neighbors in section_data.items():
            if not neighbors:
                continue

            has_failure = any(
                not is_replication_successful(neighbor)
                for neighbor in neighbors
            )

            if has_failure:
                content.append("")

            content.extend(format_context(naming_context, neighbors, naming_context_max_width))

    return "\n".join(content).rstrip()