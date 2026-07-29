from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def get_hostname(zip_ctx):
    systeminfo_filename = "systeminfo.txt"

    if not zip_ctx.exists(systeminfo_filename):
        return None

    with zip_ctx.open(systeminfo_filename) as file:
        reader = read_file_with_auto_encoding(file)

        for line in reader:
            if line.startswith("Host Name:"):
                return line.split(":", 1)[1].strip()

    return None