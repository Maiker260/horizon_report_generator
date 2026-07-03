from src.summary.utils.format_section import format_section

def service_keys(data, component, letter):
    service_keys = data["service_keys"]
    content = []

    content.append(f"\n\n\n{letter}. ENROLLMENT SERVICE KEYS")
    content.append("-" * 30)
    content.append("")

    if not service_keys:
        content.append("   * No enrollment service keys found.")
        return "\n".join(content)

    service_keys_values = {}

    for reg_key in sorted(service_keys):
        for ser_key in sorted(service_keys[reg_key], key=lambda f: f.get("key", "").lower()):
            key = ser_key.get("key", "N/A")
            value = ser_key.get("value", "N/A")

            service_keys_values[key] = value

    content.extend(format_section(service_keys_values, True))

    return "\n".join(content)