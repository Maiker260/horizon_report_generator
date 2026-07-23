def normalize_replication_data(data):
    # Normalize empty replication values.

    if not data["kcc_failures"]:
        data["kcc_failures"] = None

    if not data["replication_errors"]:
        data["replication_errors"] = None