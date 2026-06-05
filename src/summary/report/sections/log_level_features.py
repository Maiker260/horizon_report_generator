from src.summary.utils.format_section import format_section

def log_level_features(data, component, letter):
    features = data["log_level_features"]
    content = []

    content.append(f"\n\n\n{letter}. COMPONENT LOG LEVELS")
    content.append("-" * 30)
    content.append("")

    log_levels = {}

    for reg_key in sorted(features):
        component_name = reg_key.split("\\")[-1]

        for feature in features[reg_key]:
            log_levels[component_name] = feature.get("value", "N/A")

    content.extend(format_section(log_levels, True))

    return "\n".join(content)