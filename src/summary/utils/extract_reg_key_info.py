from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def extract_reg_key_info(zip_ctx, files, features):
    suffixes = tuple(features["registry_suffix"])
    expected_values = set(features["values"])

    data = {}

    current_block = None
    block_lines = []

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

            for raw_line in content.splitlines():
                line = raw_line.strip()

                if not line:
                    continue

                # Registry section header
                if line.startswith("[") and line.endswith("]"):
                    stripped = line.strip("[]").strip().lstrip("\ufeff")

                    # Save previous block
                    if current_block and block_lines:
                        data[current_block] = block_lines

                    # Match any configured suffix
                    if stripped.endswith(suffixes):
                        current_block = stripped
                        block_lines = []
                    else:
                        current_block = None
                        block_lines = []

                    continue

                # Registry value
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

            # Save last block in file
            if current_block and block_lines:
                data[current_block] = block_lines

    return data