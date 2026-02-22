def open_ports(data):
    ports = data["horizon_ports"]

    content = []
    content.append("\n\n\nD. OPEN PORTS (HORIZON)")
    content.append("-" * 30)
    content.append("")

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
            content.append(f"  Port {port_number}:")

            for entry in grouped[port_number]:
                state = entry['state']
                process = entry['process']
                local_address = entry['local_address']
                foreign_address = entry['foreign_address']
                process_id = entry['PID']

                content.append(f"      State: {state}")
                content.append(f"      Process: {process}")
                content.append(f"      Local Address: {local_address}")
                content.append(f"      Foreign Address: {foreign_address}")
                content.append(f"      PID: {process_id}")
                content.append("")

    return "\n".join(content)