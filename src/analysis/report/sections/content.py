from src.analysis.utils.count_categories import count_categories

def content(data):
    total_findings = len(data)
    categories = count_categories(data)
    report = []

    # Summary
    report.append("\n")
    report.append("A. SUMMARY")
    report.append("-" * 30)
    report.append("")

    report.append(f"Total Findings:   {total_findings}")
    report.append(f"Unique Findings:  {total_findings}")
    report.append("")

    report.append("Findings By Category:")

    if not categories:
        report.append("   No categories found.")
    else:
        max_width = max(len(key + ":") for key in categories)

        for category, count in categories.items():
            report.append(f"   {category.title() + ':':<{max_width}}  {count}")

    # Findings
    report.append("\n")
    report.append("B. FINDINGS")
    report.append("-" * 30)

    if not total_findings:
        report.append("")
        report.append("No findings matched the analysis patterns.")
        report.append("")
        return "\n".join(report)

    FIXED_NAMES = {
        "rule_name": "Name",
        "source_files": "Source File(s)",
        "category": "Category",
        "occurrences": "Occurrences",
        "last_line": "Last Seen",
        "first_line": "First Seen",
        "samples": "Samples",
        "recommendations": "Recommendations",
        "references": "References",
    }

    for index, finding in enumerate(data):
        report.append("")
        report.append("-" * 20)
        report.append(f"Finding #{index + 1}")
        report.append("-" * 20)
        report.append("")

        for key, label in FIXED_NAMES.items():
            value = finding[key]

            if not value:
                continue
            
            report.append(f"{label}:")

            if isinstance(value, list):
                for item in value:
                    report.append(f"   - {item}")
            else:
                report.append(f"   {value}")

            report.append("")

    return "\n".join(report)