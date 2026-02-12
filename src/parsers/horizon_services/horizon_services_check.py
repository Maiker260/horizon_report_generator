from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

files = FILES_OF_INTEREST["horizon_services"]
services = DATA_TO_COLLECT["horizon_services"]

def horizon_services_check(zip_ctx):
    data = {service: [] for service in services}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            for raw_line in file:
                line = raw_line.decode(errors="ignore")
                line_lower = line.lower()

                for service in services:

                    if service.lower() in line_lower:
                        data[service].append(line.strip())

    return {key: value for key, value in data.items() if value}