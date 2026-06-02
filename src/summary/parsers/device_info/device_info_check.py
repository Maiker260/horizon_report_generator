import re
from src.summary.parsers.device_info.systeminfo import systeminfo
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.device_info.ipconfig.ipconfig import ipconfig
from src.summary.parsers.device_info.reg_keys import reg_keys

parsers = {
    "systeminfo": systeminfo,
    "ipconfig": ipconfig,
    "omnissa": reg_keys,
    "vmware": reg_keys,
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
            if file == "omnissa" or file == "vmware":
                if not data.get("horizon_reg"):
                    data["horizon_reg"] = parsers[file](zip_ctx, filename, component)
            else:
                data[file] = parsers[file](zip_ctx, filename, component, data)

    return {key: value for key, value in data.items() if value}