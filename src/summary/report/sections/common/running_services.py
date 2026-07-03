def running_services(data, component, letter):
    services = data["horizon_services"]

    content = []
    content.append(f"\n\n\n{letter}. RUNNING SERVICES (HORIZON)")
    content.append("-" * 30)

    for name, info in services.items():
        content.append(f"\n{name} Services:\n")

        for service in info:
            content.append(f"   - {service}")

    return "\n".join(content)