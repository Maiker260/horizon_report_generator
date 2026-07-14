import re
from src.summary.parsers.common.device_info.systeminfo import systeminfo
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.common.device_info.ipconfig.ipconfig import ipconfig

parsers = {
    "systeminfo": systeminfo,
    "ipconfig": ipconfig,
}

def device_info_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["device_info"]
    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue
        
        match = re.match(r"^[A-Za-z0-9]+", filename)

        if not match:
            continue

        file = match.group()

        if file in parsers:
            data[file] = parsers[file](zip_ctx, filename, component, data)

    return {key: value for key, value in data.items() if value}