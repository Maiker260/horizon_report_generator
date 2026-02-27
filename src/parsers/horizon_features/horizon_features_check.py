from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

def horizon_features_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["horizon_features"]
    features = DATA_TO_COLLECT[component]["horizon_features"]

    suffix = features["registry_suffix"]
    expected_values = set(features["values"])

    data = {}

    current_block = None
    block_lines = []
    
    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            # Registry files are encode in utf-16
            content = file.read().decode("utf-16")

            for raw_line in content.splitlines():
                line = raw_line.strip()
                stripped = line.strip("[]")

                if not line:
                    continue

                if line.startswith("[") and line.endswith("]"):
                    stripped = line.strip("[]").strip().lstrip("\ufeff")

                    if current_block and block_lines:
                        data[current_block] = block_lines

                    if stripped.endswith(suffix):
                        current_block = stripped
                        block_lines = []
                    else:
                        current_block = None

                    continue

                if current_block and line.startswith('"'):
                    parts = line.split("=", 1)
                    if len(parts) != 2:
                        continue

                    key = parts[0].strip().strip('"')
                    value = parts[1].strip().strip('"')

                    if key in expected_values:
                        block_lines.append({
                            "key": key,
                            "value": value
                        })

            if current_block and block_lines:
                data[current_block] = block_lines

    return data