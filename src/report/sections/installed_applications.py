from src.utils.report_sections.format_vendor import format_vendor

SECTION_TITLES = {
    "Antivirus/EDR": "Antivirus / EDR",
    "vpn_agent": "VPN Agent",
    "monitoring_agent": "Monitoring Agent",
    "remote_tool": "Remote Tool"
}

def installed_applications(data):
    applications = data["installed_software"]

    content = []
    content.append("\n\n\nE. INSTALLED APPLICATIONS")
    content.append("-" * 30)
    content.append("")

    content.append("*Note: Only Horizon and security-related software are included in this section.\n")

    for app_type, info in applications.items():
        title = "Horizon" if app_type == "horizon_apps" else "Security Software"
        content.append(f"\n{title}:")

        # Group by Type
        grouped = {}

        for kwd in info:
            software_type = kwd["app_type"]

            if software_type not in grouped:
                grouped[software_type] = []

            grouped[software_type].append(kwd)

        for rule in sorted(grouped.keys()):
            app_data = grouped[rule]
            section_name = SECTION_TITLES.get(rule, rule.title())

            if app_type != "horizon_apps":
                content.append(f"\n   {section_name}:")
                content.append("   " + ("-" * len(section_name)))

            # Group by Vendor
            vendor_group = {}

            for app in app_data:
                vendor_name = app["kwd"]

                if vendor_name not in vendor_group:
                   vendor_group[vendor_name] = []
                
                vendor_group[vendor_name].append(app)

            for vendor, entry in sorted(vendor_group.items()):
                content.append(f"\n        {format_vendor(vendor)}:")
                
                for app_info in entry:
                    name = app_info["app_name"]
                    installed = app_info["app_info"]["installed"]
                    version = app_info["app_info"]["version"]

                    content.append(f"            - {name}")
                    content.append(f"               Installed: {installed}")
                    content.append(f"               Version: {version}")

    return "\n".join(content)