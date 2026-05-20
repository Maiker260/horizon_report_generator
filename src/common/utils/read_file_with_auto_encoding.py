def read_file_with_auto_encoding(file):
    raw = file.read()

    # UTF-16 BOM
    if raw.startswith(b'\xff\xfe') or raw.startswith(b'\xfe\xff'):
        return raw.decode("utf-16")

    # UTF-8 BOM
    if raw.startswith(b'\xef\xbb\xbf'):
        return raw.decode("utf-8-sig")

    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1", errors="ignore")