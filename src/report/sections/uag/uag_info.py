from src.utils.report_sections.normalize_uag_titles import normalize_uag_titles

sections = {
    "General": [
        "uagName",
        "uag_version",
        "fipsEnabled",
        "deploymentOption",
        "minSHAHashSize",
        "tls11Enabled",
        "tls12Enabled",
        "tls13Enabled",
        "hostClockSyncEnabled",
        "proxyDestinationUrlThumbprints",
    ],
    "URLs": [
        "healthCheckUrl",
        "blastExternalUrl",
        "pcoipExternalUrl",
        "proxyDestinationUrl",
        "tunnelExternalUrl",
    ],
    "Networking": [
        "ip0",
        "netmask0",
        "defaultGateway",
    ]
}

def uag_info(data, component, letter):
    info = data["uag_info"]
    content = []

    content.append(f"\n\n{letter}. UAG INFORMATION")
    content.append("-" * 30)

    for section, fields in sections.items():
        content.append(f"\n   {section}:")

        normalized_fields = [
            normalize_uag_titles(field) for field in fields
        ]

        max_width = max(len(name + ":") for name in normalized_fields)

        for field, display_name in zip(fields, normalized_fields):
            value = info.get(field, "-")

            if value.lower() in ("true", "false"):
                value = value.capitalize()
            
            content.append(
                f"     - {display_name + ':':<{max_width}}   {value}"
            )

    return "\n".join(content)