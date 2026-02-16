import re
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.data.SOFTWARE_RULES import SOFTWARE_RULES
from src.parsers.installed_software.apps_check import apps_check

files = FILES_OF_INTEREST["installed_software"]
PARSERS = {
    "horizon_apps": {
        "keywords": DATA_TO_COLLECT["installed_software"],
    },
    "security_software": {
        "keywords": SOFTWARE_RULES,
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

                for pars_name, config in PARSERS.items():
                    for app_type, kwds in config["keywords"].items():
                        for raw_kwd in kwds:
                            kwd = raw_kwd.lower()

                            if re.search(rf"\b{re.escape(kwd)}\b", lower_line):
                                parsed = apps_check(line, kwd, app_type)
                                data[pars_name].append(parsed)
                                break
                            
    return data