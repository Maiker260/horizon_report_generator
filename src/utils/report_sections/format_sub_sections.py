def format_sub_sections(section, content, max_width):
    
    if isinstance(section, list) and section:
        for server in section:
            content.append(f"    {'':<{max_width}}      {server}")
    else:
        content.append(f"    {'':<{max_width}}      N/A")