from src.summary.utils.report_sections.replication.build_replication import build_replication_section

def replication(data, component, letter):
    replication_data = data.get("replication_status")

    if not replication_data:
        return ""

    content = [
        f"\n\n\n{letter}. REPLICATION STATUS",
        "-" * 30,
        "",
    ]

    if replication_data.get("local"):
        content.extend(
            build_replication_section("LOCAL REPLICATION", replication_data["local"])
        )

    if replication_data.get("global"):
        if replication_data.get("local"):
            content.append("")

        content.extend(
            build_replication_section("GLOBAL REPLICATION", replication_data["global"])
        )

    return "\n".join(content).rstrip()