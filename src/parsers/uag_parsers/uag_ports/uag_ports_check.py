from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.utils.read_file_with_auto_encoding import read_file_with_auto_encoding

def uag_ports_check(zip_ctx):
    files = FILES_OF_INTEREST["unified_access_gateway"]["horizon_ports"]
    ports = DATA_TO_COLLECT["unified_access_gateway"]["horizon_ports"]

    data = {
        "tcp": [],
        "udp": []
    }

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            content = read_file_with_auto_encoding(file)

            for line in content.splitlines():
                
                if line.startswith(("tcp", "udp")):
                    parts = line.split(maxsplit=7)

                    protocol = parts[0]
                    local_address = parts[3]
                    foreign_address = parts[4]

                    ip, port = local_address.rsplit(":", 1)

                    if int(port) not in ports:
                        continue

                    if protocol.startswith("tcp"):
                        protocol = "tcp"
                        state = parts[5]
                        pid_process = parts[6]
                    else:
                        protocol = "udp"
                        state = None
                        pid_process = parts[5]

                    if "/" in pid_process:
                        pid, process = pid_process.split("/", 1)
                    else:
                        pid = None
                        process = None

                    if state and not state == "LISTEN":
                        continue

                    entry = {
                        "protocol": protocol,
                        "port_number": port,
                        "local_address": ip,
                        "foreign_address": foreign_address,
                        "state": state,
                        "PID": pid,
                        "process": process
                    }
                    
                    data[protocol].append(entry)

    return data