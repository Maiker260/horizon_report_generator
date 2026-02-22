def format_sub_sections(section, content):
    
    if isinstance(section, list) and section:
        for server in section:
            content.append(f"      - {server}")
    else:
        content.append("      - N/A")