def is_replication_error_line(line):
    # Determine whether a line contains a replication error description.

    line_lower = line.lower()

    if "consecutive failure" in line_lower:
        return False

    if line.startswith("Last success"):
        return False

    return True