import re
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.common.device_info.reg_keys import reg_keys
from src.summary.parsers.connection_server.configuration.config_file import config_file
from src.summary.parsers.connection_server.configuration.database_file import database_file

common = {
    "omnissa": reg_keys,
    "vmware": reg_keys,
}

parsers = {
    "common": common,
    "connection_server": {
        **common,
        "config": config_file,
        "database": database_file,
    },
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
        file = "database" if file == "adam" else file

        parsers_list = parsers.get(component, parsers["common"])

        if file in parsers_list:
            key = "horizon_reg" if file in ("omnissa", "vmware") else file

            if key not in data:
                data[key] = parsers_list[file](zip_ctx, filename, component)

    return {key: value for key, value in data.items() if value}