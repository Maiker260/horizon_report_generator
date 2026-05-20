def normalize_line(line):
    key, value = line.split(":", 1)
    return key.strip(), value.strip()