def horizon_features(data, component, letter):
    features = data["horizon_features"]
    content = []

    content.append(f"\n\n\n{letter}. HORIZON AGENT FEATURES")
    content.append("-" * 30)

    for reg_key in sorted(features):
        content.append(f"\n{reg_key}:")

        for feature in sorted(features[reg_key], key=lambda f: f.get("key", "").lower()):
            key = feature.get("key", "N/A")
            value = feature.get("value", "N/A")

            content.append(f"\n   {key}:")
            content.append(f"      Value: {value}")

    return "\n".join(content)