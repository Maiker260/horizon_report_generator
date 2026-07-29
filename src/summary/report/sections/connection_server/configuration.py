from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT

KEY_FIXES = {
    "FipsMode": "Horizon FIPS Mode",
    "pae-SAMLEnabled": "SAML Enabled",
    "pae-RADIUSEnabled": "RADIUS",
    "pae-BypassTunnel": "HTTP(s) Secure Tunnel",
    "clientHost": "External URL",
    "pcoipClientIPAddress": "PCoIP External URL",
    "pcoipClientTCPPort": "TCP Port",
    "pcoipClientUDPPort": "UDP Port",
    "pae-BypassPCoIPSecureGateway": "PCoIP Secure Gateway",
    "appblastClientHost": "Blast External URL",
    "pae-BypassAppBlastSecureGateway": "Blast Secure Gateway",
}

GROUPS = [
    ["FipsMode","pae-SAMLEnabled","pae-RADIUSEnabled"],
    ["pae-BypassTunnel", "clientHost",],
    ["pae-BypassPCoIPSecureGateway", "pcoipClientIPAddress",],
    ["pae-BypassAppBlastSecureGateway", "appblastClientHost",],
]

# DATABASE_FIELDS = {
#     "pae-SAMLEnabled",
#     "pae-RADIUSEnabled",
#     "pae-BypassTunnel",
#     "pae-BypassPCoIPSecureGateway",
#     "pae-BypassAppBlastSecureGateway",
#     "pae-ABSGDirectHTMLAccessOnly",
# }

def _is_enabled(value):
    return str(value) == "1"


def configuration(data, component, letter):
    horizon_reg = data["configuration"].get("horizon_reg", {})
    config = data["configuration"].get("config", {})
    database = data["configuration"].get("database", {})

    configuration = {
        **horizon_reg,
        **config,
        **database,
    }

    # If database is empty, do not try to process database fields.
    DATABASE_FIELDS = DATA_TO_COLLECT[component]["configuration"]["database_file"]
    database_available = bool(database)

    external_url = configuration.get("clientHost")

    if external_url and configuration.get("clientPort"):
        external_url += f":{configuration['clientPort']}"

    blast_url = configuration.get("appblastClientHost")

    if blast_url and configuration.get("appblastClientPort"):
        blast_url += f":{configuration['appblastClientPort']}"

    max_width = max(len(KEY_FIXES.get(key, key))for key in KEY_FIXES)

    content = []

    content.append(f"\n\n\n{letter}. SERVER CONFIGURATION")
    content.append("-" * 30)
    content.append("")

    for group_index, group in enumerate(GROUPS):

        for key in group:
            # Skip database fields when the database file is empty
            if key in DATABASE_FIELDS and not database_available:
                continue

            label = KEY_FIXES.get(key, key)

            # Horizon FIPS Mode
            if key == "FipsMode":
                value = configuration[key]

            # SAML
            elif key == "pae-SAMLEnabled":
                value = ("Enabled" if _is_enabled(configuration.get(key, "0")) else "Disabled")

            # RADIUS
            elif key == "pae-RADIUSEnabled":
                value = ("Enabled" if _is_enabled(configuration.get(key, "0")) else "Disabled")

            # HTTP(s) Secure Tunnel
            elif key == "pae-BypassTunnel":
                value = ("Disabled" if _is_enabled(configuration[key]) else "Enabled")

            # PCoIP Secure Gateway
            elif key == "pae-BypassPCoIPSecureGateway":
                value = ("Disabled" if _is_enabled(configuration[key]) else "Enabled")

            # PCoIP External URL
            elif key == "pcoipClientIPAddress":
                value = configuration[key]

            # HTTP(s) External URL
            elif key == "clientHost":
                value = external_url

            # Blast External URL
            elif key == "appblastClientHost":
                value = blast_url

            # Blast Secure Gateway
            elif key == "pae-BypassAppBlastSecureGateway":
                if not _is_enabled(configuration[key]):
                    value = "Enabled for all connections"
                else:
                    html_only = configuration.get("pae-ABSGDirectHTMLAccessOnly")

                    if _is_enabled(html_only):
                        value = "HTML only"
                    else:
                        value = "Disabled for all connections"

            else:
                value = configuration[key]

            label_with_colon = f"{label}:"

            content.append(f"{label_with_colon:<{max_width + 1}}  {value}")

            # PCoIP ports
            if key == "pcoipClientIPAddress":
                if "pcoipClientTCPPort" in configuration:
                    content.append(
                        f"    - {'TCP Port:':<{max_width - 4}} "
                        f"{configuration['pcoipClientTCPPort']}"
                    )

                if "pcoipClientUDPPort" in configuration:
                    content.append(
                        f"    - {'UDP Port:':<{max_width - 4}} "
                        f"{configuration['pcoipClientUDPPort']}"
                    )

        # Add blank line between groups
        if group_index < len(GROUPS) - 1:
            content.append("")

    return "\n".join(content)