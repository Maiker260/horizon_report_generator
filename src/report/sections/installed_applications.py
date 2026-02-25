from src.utils.report_sections.format_vendor import format_vendor

SECTION_TITLES = {
    "Antivirus/EDR": "Antivirus / EDR",
    "vpn_agent": "VPN Agent",
    "monitoring_agent": "Monitoring Agent",
    "remote_tool": "Remote Tool"
}

def installed_applications(data, component, letter):
    applications = data["installed_software"]

    content = []
    content.append(f"\n\n{letter}. INSTALLED APPLICATIONS")
    content.append("-" * 30)
    content.append("")

    content.append("*Note: Only Horizon and security-related software are included in this section.\n")

    for app_type, info in applications.items():
        title = "Horizon" if app_type == "horizon_apps" else "Security Software"
        content.append(f"{title}:\n")

        # Group by Type
        grouped = {}

        if not info:
            content.append(f"   No Antivirus/EDR, VPN, Monitoring Agent or Remote Tool found.")
            continue

        for kwd in info:
            software_type = kwd["app_type"]

            if software_type not in grouped:
                grouped[software_type] = []

            grouped[software_type].append(kwd)

        for rule in sorted(grouped.keys()):
            app_data = grouped[rule]
            section_name = SECTION_TITLES.get(rule, rule.title())

            if app_type != "horizon_apps":
                content.append(f"   {section_name}: ({len(app_data)} item(s) found)")
                content.append("   " + ("-" * len(section_name)))
                content.append("")

            # Group by Vendor
            vendor_group = {}

            for app in app_data:
                vendor_name = app["kwd"]

                if vendor_name not in vendor_group:
                   vendor_group[vendor_name] = []
                
                vendor_group[vendor_name].append(app)

            for vendor, entry in sorted(vendor_group.items()):
                content.append(f"        {format_vendor(vendor)}:")
                
                for app in entry:
                    app_info = app.get("app_info") or {}
    
                    if not app_info:
                        continue

                    name = app.get("app_name", "Unknown")
                    installed = app_info.get("installed", "N/A")
                    version = app_info.get("version", "N/A")

                    content.append(f"           - {name}")
                    content.append(f"               Installed:  {installed}")
                    content.append(f"               Version:    {version}")
                    content.append("")

    return "\n".join(content)