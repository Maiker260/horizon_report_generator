def server_roles(data):
    roles = data["server_roles"]

    content = []
    content.append("\n\n\nB. ADDITIONAL SERVER ROLES")
    content.append("-" * 30)

    if not roles:
        content.append("\nNo Additional Roles found.")

    for role, info in roles.items():
        status = info["status"]
        evidence = info["evidence"]
        file = info["file"]

        content.append(f"\n{role}")
        content.append(f" -Status: Detected (Running)")
        content.append(f" -Process: {evidence}")
        content.append(f" -File: {file}")

    return "\n".join(content)