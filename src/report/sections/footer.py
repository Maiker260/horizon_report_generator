from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.UNWANTED_ROLES import UNWANTED_ROLES
from src.data.SOFTWARE_CATEGORIES import SOFTWARE_CATEGORIES

def footer(component):
    content = []
    content.append("\n\n\n\n\n\n\n")
    content.append("=" * 50)
    content.append("REFERENCES & NOTES")
    content.append("=" * 50)

    content.append("\n*IMPORTANT NOTE: A manual review of the original evidence files is recommended to confirm findings and ensure accuracy.")

    # Evidence Sources:
    content.append("\nEvidence Sources:")
    content.append("  The following files were analyzed to generate this report:")

    for category, files in FILES_OF_INTEREST[component].items():
        content.append(f"\n - {category.replace('_', ' ').title()}:")
        for file in files:
            content.append(f"     * {file}")

    # Role Detection Criteria
    if component == "connection_server":
        content.append("\n\nRole Detection Indicators:")
        content.append("  Server roles are identified based on running processes and services.")
        content.append("  The following processes/services names are used as indicators:\n")

        role_field_names = [
            "Domain Controller",
            "DHCP Server",
            "DNS Server",
            "Certificate Authority",
            "Hyper-V",
            "WSUS",
            "IIS"
        ]

        max_width = max(len(key + ":") for key in role_field_names)

        for role, indicators in UNWANTED_ROLES.items():
            indicators_list = ", ".join(indicators)
            content.append(f" - {role + ':':<{max_width}}  {indicators_list}")

    # Software Classification Methodology
    content.append("\n\nSoftware Classification Categories:")
    content.append("  Installed applications are categorized using keyword-based matching.")

    for category, vendors in SOFTWARE_CATEGORIES.items():
        content.append(f"\n - {category}:")
        for vendor in vendors:
            content.append(f"     * {vendor}")

    content.append("")
    content.append("")

    return "\n".join(content)