def section_title(section):
    content = []

    content.append("=" * 50)
    content.append(section.upper())
    content.append("=" * 50)

    return "\n".join(content)