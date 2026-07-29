from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.summary.utils.get_hostname import get_hostname

def database_file(zip_ctx, filename, component):
    keywords = DATA_TO_COLLECT[component]["configuration"]["database_file"]
    hostname = get_hostname(zip_ctx)

    data = {}

    if not zip_ctx.exists(filename):
        return data

    target_dn_prefix = (
        f"CN={hostname},"
        "OU=Server,OU=Properties,"
    )
    
    inside_target_block = False

    with zip_ctx.open(filename) as file:
        reader = read_file_with_auto_encoding(file)

        for line in reader:
            # New LDAP object
            if line.startswith("dn:"):
                dn = line[3:].strip()

                # Find Connection Server
                if dn.startswith(target_dn_prefix):
                    inside_target_block = True
                    continue

                if inside_target_block:
                    break

                continue

            # Ignore everything before the requested LDAP object
            if not inside_target_block:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            if key in keywords:
                data[key] = value

    return data