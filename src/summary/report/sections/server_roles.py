def server_roles(data, component, letter):
    roles = data["server_roles"]

    content = []
    content.append(f"\n\n\n{letter}. ADDITIONAL SERVER ROLES")
    content.append("-" * 30)

    if not roles:
        content.append("\n   No Additional Roles Found.")
        return "\n".join(content)

    for role, info in roles.items():
        fields = {
            "Status": "Detected (Running)",
            "Evidence": info["evidence"],
            "File": info["file"],
        }

        max_width = max(len(key + ":") for key in fields)

        content.append(f"\n{role}")

        for key, value in fields.items():
            content.append(f"   - {key  + ':':<{max_width}}  {value}")

    return "\n".join(content)