KEY_FIXES = {
    "FipsMode": "Horizon FIPS Mode",
}

GROUPS = [
    ["FipsMode"],
]

def es_configuration(data, component, letter):
    configuration = {
        **data["configuration"].get("horizon_reg", {}),
    }

    max_width = max(len(KEY_FIXES.get(key, key)) for key in KEY_FIXES)

    content = []
    content.append(f"\n\n\n{letter}. SERVER CONFIGURATION")
    content.append("-" * 30)
    content.append("")

    for group in GROUPS:
        for key in group:
            if key not in configuration:
                continue

            label = f"{KEY_FIXES.get(key, key)}:"

            value = configuration[key]

            content.append(f"{label:<{max_width + 1}}  {value}")

    if content[-1] == "":
        content.pop()

    return "\n".join(content)