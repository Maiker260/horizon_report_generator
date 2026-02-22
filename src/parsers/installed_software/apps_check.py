def apps_check(line, kwd, app_type):
    parts = line.split(" [", 1)

    data = {
        "app_type": app_type,
        "kwd": kwd,
        "app_name": parts[0]
    }

    if len(parts) > 1:
        raw_date, raw_app_version = parts[1].strip("]").split(",")
        app_version = raw_app_version.strip("v")
        word, date = raw_date.split(": ")
        
        data["app_info"] = {
            "installed": date,
            "version": app_version,
        }

    return data