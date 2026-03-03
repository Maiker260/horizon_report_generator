def apps_check(line, kwd, app_type):
    parts = line.split(" [", 1)

    data = {
        "app_type": app_type,
        "kwd": kwd,
        "app_name": parts[0]
    }

    
    if len(parts) > 1:
        inside = parts[1].strip("]")
        pieces = inside.split(",")

        raw_date = pieces[0]
        word, date = raw_date.split(": ")

        version = "N/A"
        if len(pieces) > 1:
            raw_version = pieces[1]
            version = raw_version.strip("v")

        data["app_info"] = {
            "installed": date,
            "version": version,
        }

    return data