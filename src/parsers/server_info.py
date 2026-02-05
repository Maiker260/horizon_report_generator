from src.utils.search_keyword import search_keyword
from src.utils.normalize_line import normalize_line
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

def server_info(zip_ctx):
    keywords = DATA_TO_COLLECT["server_info"]
    data = {}

    for name in FILES_OF_INTEREST:
        if not zip_ctx.exists(name):
            continue

        with zip_ctx.open(name) as f:
            for raw_line in f:
                line = raw_line.decode(errors="ignore")

                for word in keywords:
                    if word in data:
                        continue

                    if search_keyword(line, word):
                        key, value = normalize_line(line)
                        data[key] = value

                if len(data) == len(keywords):
                    return data

    return data