def group_by_process(entries):
    grouped = {}

    for entry in entries:
        key = (entry["PID"], entry["process"])

        if key not in grouped:
            grouped[key] = {
                "PID": entry["PID"],
                "Process": entry["process"],
                "State": entry["state"],
                "Local Addresses": [],
                "Foreign Addresses": [],
            }

        grouped[key]["Local Addresses"].append(entry["local_address"])
        grouped[key]["Foreign Addresses"].append(entry["foreign_address"])

    return list(grouped.values())