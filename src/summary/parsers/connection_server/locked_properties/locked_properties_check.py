from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def locked_properties_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["locked_properties"]
    data = []

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            reader = read_file_with_auto_encoding(file)

            for line in reader:
                line = line.strip()

                if not line:
                    continue

                if line:
                    data.append(line)

    return data