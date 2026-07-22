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
    replication = data.get("replication_status") or {}

    if not replication:
        return ""

    partners = replication.get("neighbors", [])
    transport = replication.get("transport") or "Unknown"
    kcc_connections = replication.get("kcc_connections", 0)
    kcc_failures = replication.get("kcc_failures")
    replication_errors = replication.get("replication_errors")

    max_width = max(
        len(label)
        for label in REPLICATION_LABELS.values()
    )

    # Replication status
    overall_status = "HEALTHY"

    for section in REPLICATION_SECTIONS:
        for neighbors in replication.get(section, {}).values():
            for neighbor in neighbors:
                status = neighbor.get("status", "").upper()

                if status not in ("SUCCESS", "SUCCESSFUL"):
                    overall_status = "FAILED"
                    break

            if overall_status == "FAILED":
                break

        if overall_status == "FAILED":
            break

    if kcc_failures or replication_errors:
        overall_status = "FAILED"

    # Report
    content = [
        f"\n\n\n{letter}. REPLICATION STATUS",
        "-" * 30,
        "",
    ]

    if not partners:
        content.append("   * No replication neighbors found. ")
        return "\n".join(content).rstrip()
    
    content.append(f"Overall Status:  {overall_status}\n")

    content.append("Replication:")

    content.extend([
        f"   {REPLICATION_LABELS['transport']:<{max_width + 1}} "
        f"{transport}",
        f"   {REPLICATION_LABELS['kcc_connections']:<{max_width + 1}} "
        f"{kcc_connections}",
        f"   {REPLICATION_LABELS['kcc_failures']:<{max_width + 1}} "
        f"{kcc_failures or 'None'}",
        f"   {REPLICATION_LABELS['replication_errors']:<{max_width + 1}} "
        f"{replication_errors or 'None'}",
    ])

    content.append("")

    if partners:
        content.append("Neighbors:")
        content.extend(
            f"   - {partner}"
            for partner in partners
        )
    else:
        content.append(
            f"{'neighbors: ':<{max_width + 1}} "
            f"Unknown"
        )

    # Replication details
    for section_key, section_title in REPLICATION_SECTIONS.items():
        section_data = replication.get(section_key, {})

        if not section_data:
            continue

        content.extend([
            "",
            f"{section_title}:",
        ])

        sections_labels_max_width = max(
            len(label)
            for label in section_data
        )

        for naming_context, neighbors in section_data.items():
            if not neighbors:
                continue

            # Single neighbor
            if len(neighbors) == 1:
                neighbor = neighbors[0]
                status = neighbor.get("status", "UNKNOWN")
                last_attempt = (neighbor.get("last_attempt")or "Unknown")

                content.append(
                    f"   {naming_context + ':':<{sections_labels_max_width + 1}}  {status} {last_attempt}"
                )

                continue

            # Multiple neighbors
            content.append(f"   {naming_context}:")

            for neighbor in neighbors:
                partner = neighbor.get("neighbor", "Unknown")
                status = neighbor.get("status", "UNKNOWN",)
                last_attempt = (neighbor.get("last_attempt") or "Unknown")

                content.append(
                    f"      - {partner}: "
                    f"{status} ({last_attempt})"
                )

    return "\n".join(content).rstrip()