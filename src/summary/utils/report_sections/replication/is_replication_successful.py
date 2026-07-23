SUCCESS_STATUSES = {
    "SUCCESS",
    "SUCCESSFUL",
}

def is_replication_successful(neighbor):
    status = neighbor.get("status", "").upper()
    return status in SUCCESS_STATUSES