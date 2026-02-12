import re
from src.parsers.device_info.systeminfo import systeminfo
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.parsers.device_info.ipconfig.ipconfig import ipconfig
from src.parsers.device_info.fips_check import fips_check

files = FILES_OF_INTEREST["device_info"]
parsers = {
    "systeminfo": systeminfo,
    "ipconfig": ipconfig,
    "omnissa": fips_check,
    "vmware": fips_check
}

def device_info_check(zip_ctx):
    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue
        
        match = re.match(r"^[A-Za-z0-9]+", filename)

        if not match:
            continue

        file = match.group()

        if file in parsers:
            if file == "omnissa" or file == "vmware":
                if not data.get("horizon-reg"):
                    data["horizon-reg"] = parsers[file](zip_ctx, filename, data)
            else:
                data[file] = parsers[file](zip_ctx, filename, data)

    return data