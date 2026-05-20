def apps_check(line, kwd, app_type):
    parts = line.split(" [", 1)

    data = {
        "app_type": app_type,
        "vendor": None,
        "kwd": kwd,
        "app_name": parts[0].strip(),
        "app_info": {
            "installed": "N/A",
            "version": "N/A"
        }
    }

    if len(parts) > 1:
        inside = parts[1].strip("]")
        pieces = inside.split(",")

        raw_date = pieces[0]
        _, date = raw_date.split(": ")

        version = "N/A"
        if len(pieces) > 1:
            raw_version = pieces[1]
            version = raw_version.strip("v").strip()

        data["app_info"]["installed"] = date
        data["app_info"]["version"] = version

    return data