from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT


def open_ports(data, component, letter):
    expected_ports = DATA_TO_COLLECT[component]["horizon_ports"]
    ports = data["horizon_ports"]

    content = []
    content.append(f"\n\n\n{letter}. OPEN PORTS (HORIZON)")
    content.append("-" * 30)
    content.append("")

    field_names = [
        "State",
        "Process",
        "Local Address",
        "Foreign Address",
        "PID"
    ]
    
    max_width = max(len(key + ":") for key in field_names)

    for protocol, info in ports.items():
        content.append(f"{protocol}:")
        content.append("-" * len(protocol))

        grouped = {}

        for port in info:
            port_number = port["port_number"]

            if port_number not in grouped:
                grouped[port_number] = []

            grouped[port_number].append(port)

        for port_number in sorted(expected_ports):
            port_str = str(port_number)

            if port_str not in grouped:
                udp_ports = {
                    "connection_server": [4172, 8443],
                    "agent": [4172, 22443, 55000],
                    "client": [443, 4172, 8443, 22443],
                    "unified_access_gateway": [],
                }

                if protocol == "UDP" and port_str not in udp_ports[component]:
                    continue
                
                content.append(f"   Port {port_str}:")
                content.append("      - Port Not In Use")
                content.append("")
                continue

            content.append(f"   Port {port_str}:")

            for entry in grouped[port_str]:
                fields = {
                    "PID": entry['PID'],
                    "State": entry['state'],
                    "Process": entry['process'],
                    "Local Address": entry['local_address'],
                    "Foreign Address": entry['foreign_address'],
                }

                for key, value in fields.items():
                    content.append(f"      - {key + ':':<{max_width}}  {value}")

                content.append("")

    return "\n".join(content)