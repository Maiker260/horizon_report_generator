import re

def get_uag_section_config(section_name, sections):
    if section_name in sections:
        return sections[section_name]

    # regex
    for pattern, config in sections.items():
        try:
            if re.fullmatch(pattern, section_name):
                return config
        except re.error:
            pass

    return None