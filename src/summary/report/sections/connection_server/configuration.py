KEY_FIXES = {
    "FipsMode": "Horizon FIPS Mode",
    "clientHost": "External URL",
    "clientPort": "Port",
    "pcoipClientIPAddress": "PCoIP External URL",
    "pcoipClientUDPPort": "UDP Port",
    "pcoipClientTCPPort": "TCP Port",
    "appblastClientHost": "Blast External URL",
    "appblastClientPort": "Port",
}

GROUPS = [
    ["FipsMode"],
    ["clientHost"],
    ["pcoipClientIPAddress"],
    ["appblastClientHost"],
]

def configuration(data, component, letter):
    configuration = {
        **data["configuration"].get("horizon_reg", {}),
        **data["configuration"].get("config", {})
    }

    external_url = configuration.get("clientHost")
    if external_url and configuration.get("clientPort"):
        external_url += f":{configuration['clientPort']}"

    blast_url = configuration.get("appblastClientHost")
    if blast_url and configuration.get("appblastClientPort"):
        blast_url += f":{configuration['appblastClientPort']}"

    max_width = max(
        len(KEY_FIXES.get(key, key))
        for key in KEY_FIXES
    )

    content = []
    content.append(f"\n\n\n{letter}. SERVER CONFIGURATION")
    content.append("-" * 30)
    content.append("")

    for group in GROUPS:
        for key in group:
            if key not in configuration:
                continue

            label = f"{KEY_FIXES.get(key, key)}:"

            if key == "clientHost":
                value = external_url
            elif key == "appblastClientHost":
                value = blast_url
            else:
                value = configuration[key]

            content.append(
                f"{label:<{max_width + 1}}  {value}"
            )

            # PCoIP
            if key == "pcoipClientIPAddress":
                if "pcoipClientTCPPort" in configuration:
                    content.append(
                        f"    - {'TCP Port:':<14} "
                        f"{configuration['pcoipClientTCPPort']}"
                    )

                if "pcoipClientUDPPort" in configuration:
                    content.append(
                        f"    - {'UDP Port:':<14} "
                        f"{configuration['pcoipClientUDPPort']}"
                    )


    if content[-1] == "":
        content.pop()

    return "\n".join(content)