from src.analysis.utils.normalize_findings import normalize_findings
from src.analysis.utils.count_categories import count_categories

def content(data):
    normalized_data = normalize_findings(data)
    categories = count_categories(normalized_data)

    report = []

    # Summary
    report.append("\n")
    report.append("A. SUMMARY")
    report.append("-" * 30)
    report.append("")

    report.append(f"Total Findings:   {len(data)}")
    report.append(f"Unique Findings:  {len(normalized_data)}")
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

    if not normalized_data:
        report.append("")
        report.append("No findings matched the analysis patterns.")
        report.append("")
        return "\n".join(report)

    FIXED_NAMES = {
        "rule_name": "Name",
        "source_file": "Source File",
        "category": "Category",
        "occurrences": "Occurrences",
        "line_found": "Sample Line",
        "recommendations": "Recommendations",
        "references": "References"
    }

    for index, finding in enumerate(normalized_data):
        report.append("")
        report.append("-" * 20)
        report.append(f"Finding #{index + 1}")
        report.append("-" * 20)
        report.append("")

        for key, label in FIXED_NAMES.items():
            report.append(f"{label}:")
            value = finding[key]

            if isinstance(value, list):
                for item in value:
                    report.append(f"   - {item}")
            else:
                report.append(f"   {value}")

            report.append("")

    return "\n".join(report)