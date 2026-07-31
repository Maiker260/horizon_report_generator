def parse_options(line, data):
    # Parse DSA Options and Site Options from a replication file.

    if line.startswith("DSA Options:"):
        value = line.split(":", 1)[1].strip()
        data["DSA Options"] = None if value == "(none)" else value
        return True

    if line.startswith("Site Options:"):
        value = line.split(":", 1)[1].strip()
        data["Site Options"] = None if value == "(none)" else value
        return True

    return False