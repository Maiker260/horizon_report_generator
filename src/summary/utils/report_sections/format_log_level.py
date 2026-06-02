def format_log_level(component, reg_data):
    values_list = next(iter(reg_data.values()), [])

    flags = {
        item["key"]: item["value"].lower() == "true"
        for item in values_list
    }

    trace = flags.get("TraceEnabled")
    debug = flags.get("DebugEnabled")

    if trace is None and debug is None:
        if component == "connection_server":
            return "Debug"
        
        return "Info"

    if trace and debug:
        return "Trace"

    if not trace and debug:
        return "Debug"

    return "Info"