from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def version_check(zip_ctx, filename):
    data = {
        "uag_version": None
    }

    with zip_ctx.open(filename) as file:
        reader = read_file_with_auto_encoding(file)

        for line in reader:
            line = line.strip()
            
            if not line:
                continue

            if line.startswith("euc-unified-access-gateway"):
                parts = line.split("-v", 1)

                data["uag_version"] = parts[1]

    return data