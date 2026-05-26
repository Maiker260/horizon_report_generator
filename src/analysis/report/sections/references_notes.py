from src.analysis.data.FILES_OF_INTEREST import FILES_OF_INTEREST

def analysis_references_notes(component):
    content = []

    # Evidence Sources:
    content.append("\nEvidence Sources:")
    content.append("  The following files were analyzed to generate this report:")

    for compnt, files in FILES_OF_INTEREST.items():
        content.append(f"\n - {compnt.replace('_', ' ').title()}:")

        for file in files:
            content.append(f"     * {file}")

    content.append("")
    content.append("")

    return "\n".join(content)