from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.data.UNWANTED_ROLES import UNWANTED_ROLES
from src.summary.data.SOFTWARE_RULES import SOFTWARE_RULES

def summary_references_notes(component):
    content = []

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

        max_width = max(len(key + ":") for key in UNWANTED_ROLES)

        for role, indicators in UNWANTED_ROLES.items():
            indicators_list = ", ".join(indicators)
            content.append(f" - {role + ':':<{max_width}}  {indicators_list}")

    # Software Classification Methodology
    if not component == "unified_access_gateway":
        content.append("\n\nSoftware Classification Categories:")
        content.append("  Installed applications are categorized using keyword-based matching.")

        for category, vendors in SOFTWARE_RULES.items():
            content.append(f"\n - {category}:")
            for vendor in vendors:
                content.append(f"     * {vendor}")

    content.append("")
    content.append("")

    return "\n".join(content)