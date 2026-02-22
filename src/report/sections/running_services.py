def running_services(data):
    services = data["horizon_services"]

    content = []
    content.append("\n\n\nC. RUNNING SERVICES (HORIZON)")
    content.append("-" * 30)

    for name, info in services.items():
        content.append(f"\n{name} Services\n")

        for service in info:
            content.append(f" -{service}")

    content.append("\nSource: net-start.txt")

    return "\n".join(content)