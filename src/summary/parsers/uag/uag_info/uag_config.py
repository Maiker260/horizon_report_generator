from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.summary.utils.get_uag_section_config import get_uag_section_config

def uag_config(zip_ctx, filename):
    sections = DATA_TO_COLLECT["unified_access_gateway"]["uag_info"]

    data = {}
    to_parse_sections = []

    with zip_ctx.open(filename) as file:
            reader = read_file_with_auto_encoding(file)

            current_section = None
            sub_lines = []

            for line in reader:
                line = line.strip()

                if not line:
                    continue

                if line.startswith("["):
                    stripped = line.strip("[]")

                    if current_section:
                        to_parse_sections.append({
                            "name": current_section,
                            "lines": sub_lines
                        })
                        sub_lines = []

                    if get_uag_section_config(stripped, sections):
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

        section_config = get_uag_section_config(name, sections)

        for config_line in lines:
            if "=" not in config_line:
                continue

            key, value = config_line.split("=", 1)

            key = key.strip()
            value = value.strip()

            if key in section_config:
                if key == "origin":
                    data.setdefault("origins", []).append(value)
                else:
                    data[key] = value

    return data