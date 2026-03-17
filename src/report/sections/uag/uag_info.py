import re
from src.utils.report_sections.normalize_uag_titles import normalize_uag_titles

sections = {
    "General": [
        "uagName",
        "uag_version",
    ],
    "Deployment": [
        "deploymentOption",
    ],
    "Networking": [],
    "Security": [
        "fipsEnabled",
        "minSHAHashSize",
        "tls11Enabled",
        "tls12Enabled",
        "tls13Enabled",
    ],
    "System": [
        "hostClockSyncEnabled",
        "healthCheckUrl",
    ],
    "URLs": [
        "proxyDestinationUrl",
        "proxyDestinationUrlThumbprints",
        "pcoipExternalUrl",
        "blastExternalUrl",
        "tunnelExternalUrl",
    ],
}

def uag_info(data, component, letter):
    info = data["uag_info"]
    content = []

    content.append(f"\n\n{letter}. UAG INFORMATION")
    content.append("-" * 30)

    for section, fields in sections.items():
        content.append(f"\n   {section}:")

        if section == "Networking":
            interfaces = sorted(
                [key for key in info.keys() if re.match(r"ip\d+", key)]
            )

            for interface in interfaces:
                interf_id = re.findall(r"\d+", interface)[0]

                ip = info.get(f"ip{interf_id}", "-")
                mask = info.get(f"netmask{interf_id}", "-")

                content.append(f"      NIC {interf_id}:")
                content.append(f"        - IP Address:  {ip}")
                content.append(f"        - Netmask:     {mask}")
                content.append("")

            gateway = info.get("defaultGateway", "-")
            dns = info.get("dns", "-")
            content.append(f"      - DNS:              {dns}")
            content.append(f"      - Default Gateway:  {gateway}")

            continue

        normalized_fields = [
            normalize_uag_titles(field) for field in fields
        ]

        max_width = max(len(name + ":") for name in normalized_fields)

        for field, display_name in zip(fields, normalized_fields):
            value = info.get(field, "-")

            if value.lower() in ("true", "false"):
                value = value.capitalize()
            
            content.append(
                f"      - {display_name + ':':<{max_width}}  {value}"
            )

    return "\n".join(content)