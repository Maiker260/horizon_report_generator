import io

def read_file_with_auto_encoding(file):
    raw = file.read(4096)

    encoding = "utf-8"

    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        encoding = "utf-16"

    elif raw.startswith(b"\xef\xbb\xbf"):
        encoding = "utf-8-sig"

    file.seek(0)

    return io.TextIOWrapper(
        file,
        encoding=encoding,
        errors="ignore"
    )