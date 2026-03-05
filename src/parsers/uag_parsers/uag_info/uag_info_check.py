import re
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.parsers.uag_parsers.uag_info.uag_config import uag_config
from src.parsers.uag_parsers.uag_info.version_check import version_check

parsers = {
    "uag_config": uag_config,
    "version": version_check,
}

def uag_info_check(zip_ctx):
    files = FILES_OF_INTEREST["unified_access_gateway"]["uag_info"]

    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        match = re.match(r"^[A-Za-z0-9_]+", filename)

        if not match:
            continue

        file = match.group()

        if file in parsers:
            result = parsers[file](zip_ctx, filename)
            data.update(result)

    return data