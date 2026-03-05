from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

def uag_config(zip_ctx, filename):
    sections = DATA_TO_COLLECT["unified_access_gateway"]["uag_info"]

    data = {}
    to_parse_sections = []

    with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

            current_section = None
            sub_lines = []

            for line in content.splitlines():
                if line.startswith("["):
                    stripped = line.strip("[]")

                    if current_section:
                        to_parse_sections.append({
                            "name": current_section,
                            "lines": sub_lines
                        })
                        sub_lines = []

                    if stripped in sections:
                        current_section = stripped
                    else:
                        current_section = None

                    continue

                if current_section:
                    sub_lines.append(line)

            if current_section:
                to_parse_sections.append({
                    "name": current_section,
                    "lines": sub_lines
                })

    for entry in to_parse_sections:
        name = entry["name"]
        lines = entry["lines"]

        for config_line in lines:
            if "=" not in config_line:
                continue

            key, value = config_line.split("=", 1)

            if key.strip() in sections[name]:
                data[key.strip()] = value.strip()

    return data