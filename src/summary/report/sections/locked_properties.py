def locked_properties(data, component, letter):
    file_entries = data["locked_properties"]

    content = []
    content.append(f"\n\n\n{letter}. LOCKED.PROPERTIES FILE:")
    content.append("-" * 30)
    content.append("")

    if not file_entries:
        content.append(
            "   Locked.properties file not found or no relevant entries were detected."
        )

    for line in file_entries:
        content.append(f"   - {line}")

    return "\n".join(content)