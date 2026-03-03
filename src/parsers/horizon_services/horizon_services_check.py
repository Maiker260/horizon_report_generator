from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def horizon_services_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["horizon_services"]
    services = DATA_TO_COLLECT[component]["horizon_services"]
    data = {service: [] for service in services}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

            for line in content.splitlines():
                line = line.strip()
                line_lower = line.lower()

                for service in services:

                    if service.lower() in line_lower:
                        data[service].append(line.strip())

    return {key: value for key, value in data.items() if value}