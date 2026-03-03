from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def fips_check(zip_ctx, filename, component, current_data):
    data = {}

    if not zip_ctx.exists(filename):
        return

    with zip_ctx.open(filename) as file:
        # Registry files are encode in utf-16
        content = read_file_with_auto_encoding(file)

        for line in content.splitlines():
            line = line.strip()

            if line.strip().startswith('"FipsMode"'):
                key, value = line.split("=", 1)
                value = value.strip().strip('"')

                data[key.strip('"')] = int(value) == 1

    return data