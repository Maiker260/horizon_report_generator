from src.summary.utils.format_section import format_section

def horizon_features(data, component, letter):
    features = data["horizon_features"]
    content = []

    content.append(f"\n\n\n{letter}. HORIZON AGENT FEATURES")
    content.append("-" * 30)
    content.append("")


    feature_values = {}

    for reg_key in sorted(features):
        for feature in sorted(features[reg_key], key=lambda f: f.get("key", "").lower()):
            key = feature.get("key", "N/A")
            value = feature.get("value", "N/A")

            feature_values[key] = value

    content.extend(format_section(feature_values, True))

    return "\n".join(content)