from src.utils.search_keyword import search_keyword
from src.utils.normalize_line import normalize_line
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.parsers.device_info.hotfixes import parse_hotfixes
from src.parsers.device_info.network_cards import parse_nics

BLOCK_PARSERS = {
    "Hotfix(s)": parse_hotfixes,
    "Network Card(s)": parse_nics,
}

def systeminfo(zip_ctx, filename):
    keywords = DATA_TO_COLLECT["device_info"]

    data = {}
    current_block = None
    block_lines = []

    if not zip_ctx.exists(filename):
        return

    with zip_ctx.open(filename) as file:
        for raw_line in file:
            line = raw_line.decode(errors="ignore")

            if current_block:
                if line and line[0].isspace():
                    block_lines.append(line)
                    continue

                data[current_block] = BLOCK_PARSERS[current_block](block_lines)
                current_block = None
                block_lines = []

            for keyword in keywords - data.keys():
                if search_keyword(line, keyword):
                    if keyword in BLOCK_PARSERS:
                        current_block = keyword
                        block_lines = []
                    else:
                        key, value = normalize_line(line)
                        data[key] = value
                    break

    if current_block:
        data[current_block] = BLOCK_PARSERS[current_block](block_lines)

    return data