from src.utils.report_sections.format_sub_sections import format_sub_sections
from src.utils.report_sections.extract_device_info import extract_device_info

def server_information(data):
    max_width = max(len(key) for key in data.keys())
    device_info = data["device_info"]
    systeminfo = device_info["systeminfo"]

    info = extract_device_info(device_info)
    hotfixes = systeminfo.get("Hotfix(s)", "N/A")
    network_cards = systeminfo.get("Network Card(s)", "N/A")

    content = []
    content.append("\n\nA. SERVER INFORMATION")
    content.append("-" * 30)

    # One line content
    for key, value in info.items():
        content.append(f"{key:<{max_width}} : {value}")

    # Hotfixes
    content.append(f"\nInstalled Patches:")
    for patch in hotfixes:
        content.append(f" -{patch}")

    # NICs
    content.append(f"\nNetwork Interfaces:")
    for nic in network_cards:
        index = nic.get("Index", "N/A")
        adapter = nic.get("Adapter", "N/A")
        connection = nic.get("Connection Name", "N/A")

        ips = nic.get("IP Addresses", [])
        dns = nic.get("DNS Servers", [])

        content.append(f"\n #{index}")
        content.append(f"   -Adapter: {adapter}")
        content.append(f"   -Interface: {connection}")

        content.append(f"   -IP Addresses:")
        format_sub_sections(ips, content)
        
        content.append(f"   -DNS Servers:")
        format_sub_sections(dns, content)

    return "\n".join(content)