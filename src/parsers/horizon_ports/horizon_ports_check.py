import re
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

files = FILES_OF_INTEREST["horizon_ports"]
ports = DATA_TO_COLLECT["horizon_ports"]

def horizon_ports_check(zip_ctx):
    data = {
        "TCP": [],
        "UDP": []
    }

    last_entry = None

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            for raw_line in file:
                line = raw_line.decode(errors="ignore").strip()

                if line.startswith(("TCP", "UDP")):
                    parts = line.split()

                    protocol = parts[0]
                    local_address = parts[1]
                    foreign_address = parts[2]

                    if local_address.startswith("["):
                        ip, port = local_address.split("]:")
                        ip = ip + "]"
                    else:
                        ip, port = local_address.split(":")

                    if int(port) not in ports:
                        last_entry = None
                        continue

                    if protocol == "TCP":
                        state = parts[3]
                        pid = parts[4]
                    else:
                        state = None
                        pid = parts[3]

                    last_entry = {
                        "protocol": protocol,
                        "local_address": local_address,
                        "foreign_address": foreign_address,
                        "state": state,
                        "PID": pid,
                        "process": None
                    }

                    data[protocol].append(last_entry)

                elif line.startswith("[") and last_entry:
                    last_entry["process"] = line.strip("[]")

    return data