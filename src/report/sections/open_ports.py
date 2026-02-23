def open_ports(data):
    ports = data["horizon_ports"]

    content = []
    content.append("\n\n\nD. OPEN PORTS (HORIZON)")
    content.append("-" * 30)
    content.append("")

    field_names = [
        "State",
        "Process",
        "Local Address",
        "Foreign Address",
        "PID"
    ]
    
    max_width = max(len(key) for key in field_names)

    for protocol, info in ports.items():
        content.append(f"{protocol}:")
        content.append("-" * len(protocol))

        grouped = {}

        for port in info:
            port_number = port["port_number"]

            if port_number not in grouped:
                grouped[port_number] = []

            grouped[port_number].append(port)

        for port_number in sorted(grouped.keys(), key=int):
            content.append(f"   Port {port_number}:")

            for entry in grouped[port_number]:
                fields = {
                    "State": entry['state'],
                    "Process": entry['process'],
                    "Local Address": entry['local_address'],
                    "Foreign Address": entry['foreign_address'],
                    "PID": entry['PID']
                }

                for key, value in fields.items():
                    content.append(f"      - {key:<{max_width}} : {value}")

                content.append("")

    return "\n".join(content)