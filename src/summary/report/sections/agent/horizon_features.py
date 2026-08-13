from src.summary.utils.format_section import format_section

def horizon_features(data, component, letter):
    # Example:

    # HORIZON AGENT FEATURES
    
    # Printer Redirection:  Enabled
    # Scanner Redirection:  Disabled

    features = data["horizon_features"]
    content = []

    content.append(f"\n\n\n{letter}. HORIZON AGENT FEATURES")
    content.append("-" * 30)
    content.append("")

    if not features:
        content.append("   * No additional agent features found.")
        return "\n".join(content)

    feature_values = {}

    for reg_key in sorted(features):
        for feature in sorted(features[reg_key], key=lambda f: f.get("key", "").lower()):
            key = feature.get("key", "N/A")
            value = feature.get("value", "N/A")

            feature_values[key] = value

    content.extend(format_section(feature_values, True))

    return "\n".join(content)