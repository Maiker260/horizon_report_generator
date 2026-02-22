from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

files = FILES_OF_INTEREST["horizon_ports"]
ports = DATA_TO_COLLECT["horizon_ports"]

def horizon_ports_check(zip_ctx):
    data = {
        "TCP": [],
        "UDP": []
    }

    seen_entries = set()
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

                    ip, port = local_address.rsplit(":", 1)

                    if int(port) not in ports:
                        last_entry = None
                        continue

                    if protocol == "TCP":
                        state = parts[3]
                        pid = parts[4]
                    else:
                        state = None
                        pid = parts[3]

                    if state and not state == "LISTENING":
                        last_entry = None
                        continue

                    last_entry = {
                        "protocol": protocol,
                        "port_number": port,
                        "local_address": local_address,
                        "foreign_address": foreign_address,
                        "state": state,
                        "PID": pid,
                        "process": None
                    }

                elif line.startswith("[") and last_entry:
                    process_name = line.strip("[]")
                    last_entry["process"] = process_name
                    protocol = last_entry["protocol"]

                    ip_part, port_part = last_entry["local_address"].rsplit(":", 1)
                    unique_key = (protocol, ip_part, port_part, process_name)

                    if unique_key not in seen_entries:
                        seen_entries.add(unique_key)
                        data[last_entry["protocol"]].append(last_entry)

                    last_entry = None

    return data