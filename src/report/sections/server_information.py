from src.utils.report_sections.format_sub_sections import format_sub_sections
from src.utils.report_sections.extract_device_info import extract_device_info

def server_information(data):
    device_info = data["device_info"]
    systeminfo = device_info["systeminfo"]

    info = extract_device_info(device_info)
    max_width = max(len(key) for key in info)

    hotfixes = systeminfo.get("Hotfix(s)", "N/A")
    network_cards = systeminfo.get("Network Card(s)", "N/A")

    content = []
    content.append("\n\nA. SERVER INFORMATION")
    content.append("-" * 30)

    # One line content
    for key, value in info.items():
        content.append(f"{key + ':':<{max_width + 1}}  {value}")

    # Hotfixes
    content.append(f"\nInstalled Patches:")
    for patch in hotfixes:
        content.append(f"   - {patch}")

    # NICs
    field_names = [
        "Index",
        "Adapter",
        "Interface",
        "IP Addresses",
        "DNS Servers"
    ]

    max_width_nic = max(len(key) for key in field_names)
    content.append(f"\nNetwork Interfaces:")
    
    for i, nic in enumerate(network_cards, start=1):
        fields = {
            "Adapter": nic.get("Adapter", "N/A"),
            "Interface": nic.get("Connection Name", "N/A"),
            "IP Addresses": nic.get("IP Addresses", []),
            "DNS Servers": nic.get("DNS Servers", [])
        }

        content.append(f"\n   #{i}")

        for key in field_names[1:]:
            value = fields.get(key, "N/A")

            if key in ("IP Addresses", "DNS Servers"):
                content.append(f"     - {key + ':':<{max_width_nic}} ")
                format_sub_sections(value, content, max_width_nic)
                continue

            content.append(f"     - {key + ':':<{max_width_nic}}   {value}")

    return "\n".join(content)