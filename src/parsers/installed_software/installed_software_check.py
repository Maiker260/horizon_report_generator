import re
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.data.ANTIVIRUS_LIST import ANTIVIRUS_LIST
from src.parsers.installed_software.apps_check import apps_check

files = FILES_OF_INTEREST["installed_software"]
PARSERS = {
    "horizon_apps": {
        "keywords": [kwd.lower() for kwd in DATA_TO_COLLECT["installed_software"]],
    },
    "antivirus": {
        "keywords": [kwd.lower() for kwd in ANTIVIRUS_LIST],
    }
}

def installed_software_check(zip_ctx):
    data = {name: [] for name in PARSERS}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            for raw_line in file:
                line = raw_line.decode(errors="ignore").strip()
                lower_line = line.lower()

                for name, config in PARSERS.items():
                    for kwd in config["keywords"]:
                        if re.search(rf"\b{re.escape(kwd)}\b", lower_line):
                            parsed = apps_check(line, kwd)
                            data[name].append(parsed)
                            break

    return data