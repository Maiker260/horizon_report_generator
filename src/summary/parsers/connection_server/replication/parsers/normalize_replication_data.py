def normalize_replication_data(data):
    # Normalize empty replication values.
    data["neighbors"] = sorted(data["neighbors"])