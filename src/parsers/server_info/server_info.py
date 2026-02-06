from src.utils.search_keyword import search_keyword
from src.utils.normalize_line import normalize_line
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.utils.collect_block_lines import collect_block_lines
from src.parsers.server_info.hotfixes import parse_hotfixes
from src.parsers.server_info.network_cards import parse_nics

BLOCK_PARSERS = {
    "Hotfix(s)": parse_hotfixes,
    "Network Card(s)": parse_nics,
}

def server_info(zip_ctx):
    keywords = DATA_TO_COLLECT["server_info"]
    files = FILES_OF_INTEREST["server_info"]
    data = {}

    for name in files:
        if not zip_ctx.exists(name):
            continue

        # If the block parsing parsed a line but didnt match the pattern, then it is a Pending Line
        pending_line = None

        with zip_ctx.open(name) as file:
            for raw_line in file:
                line = pending_line or raw_line.decode(errors="ignore")
                pending_line = None

                # For each word in keywords except the ones in data.keys
                for keyword in keywords - data.keys():
                    if not search_keyword(line, keyword):
                        continue

                    if keyword in BLOCK_PARSERS:
                        block_lines, pending_line = collect_block_lines(file)
                        data[keyword] = BLOCK_PARSERS[keyword](block_lines)
                    else:
                        key, value = normalize_line(line)
                        data[key] = value

                    break

                if len(data) == len(keywords):
                    return data

    return data