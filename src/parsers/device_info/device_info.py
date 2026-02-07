from src.parsers.device_info.systeminfo import systeminfo
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
import re

def testi(zip_ctx, files):
    print("ipconfig")

files = FILES_OF_INTEREST["device_info"]
parsers = {
    "systeminfo": systeminfo,
    "ipconfig": testi
}

def device_info(zip_ctx):
    data = {}

    for filename in files:
        match = re.match(r"^[A-Za-z0-9]+", filename)

        if not match:
            continue

        file = match.group()

        if file in parsers:
            data[file] = parsers[file](zip_ctx, filename)

    return data