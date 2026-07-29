import re
from src.summary.parsers.common.device_info.system_info.system_info import system_info
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.common.device_info.ipconfig.ipconfig import ipconfig
from src.summary.parsers.common.device_info.set_file import set_file

parsers = {
    "systeminfo": system_info,
    "ipconfig": ipconfig,
    "set": set_file,
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