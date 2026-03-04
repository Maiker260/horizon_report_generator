from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.data.SOFTWARE_RULES import SOFTWARE_RULES
from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.parsers.installed_software.apps_check import apps_check
from src.utils.build_detection_index import build_detection_index

def installed_software_check(zip_ctx, component):
    SECURITY_INDEX = build_detection_index(SOFTWARE_RULES)
    HORIZON_INDEX = build_detection_index(DATA_TO_COLLECT[component]["installed_software"])
    files = FILES_OF_INTEREST[component]["installed_software"]

    data = {
        "horizon_apps": [],
        "security_software": []
    }

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

            for line in content.splitlines():
                stripped = line.strip()

                detected = False

                for entry in SECURITY_INDEX:
                    if entry["pattern"].search(stripped):
                        parsed = apps_check(line, entry["alias"], entry["category"])

                        parsed["vendor"] = entry["vendor"]
                        data["security_software"].append(parsed)

                        detected = True
                        break

                if detected:
                    continue

                for entry in HORIZON_INDEX:
                    if entry["pattern"].search(stripped):
                        parsed = apps_check(line, entry["alias"], entry["category"])
                        
                        parsed["vendor"] = entry["vendor"]
                        data["horizon_apps"].append(parsed)

                        break

    return data