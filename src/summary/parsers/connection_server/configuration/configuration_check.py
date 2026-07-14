import re
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.common.device_info.reg_keys import reg_keys
from src.summary.parsers.connection_server.configuration.config_file import config_file

parsers = {
    "omnissa": reg_keys,
    "vmware": reg_keys,
    "config": config_file
}

def configuration_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["configuration"]
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
                if component == "connection_server":
                    data[file] = parsers[file](zip_ctx, filename, component)

    return {key: value for key, value in data.items() if value}