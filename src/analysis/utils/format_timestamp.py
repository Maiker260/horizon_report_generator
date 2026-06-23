def format_timestamp(dt):
    if dt is None:
        return "Unknown"

    return dt.strftime("%Y-%m-%d %H:%M:%S %z")