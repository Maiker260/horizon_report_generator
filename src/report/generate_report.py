import string
from src.report.sections.header import header
from src.report.sections.device_information import device_information
from src.report.sections.server_roles import server_roles
from src.report.sections.running_services import running_services
from src.report.sections.open_ports import open_ports
from src.report.sections.installed_applications import installed_applications
from src.report.sections.certificates import certificates
from src.report.sections.footer import footer

COMMON_REPORT_SECTIONS = [
    device_information,
    running_services,
    open_ports,
    installed_applications,
]

REPORT_SECTIONS = {
    "connection_server": lambda: (
        COMMON_REPORT_SECTIONS[:1]
        + [server_roles]
        + COMMON_REPORT_SECTIONS[1:]
        + [certificates]
    ),
    "agent": lambda: COMMON_REPORT_SECTIONS,
    "client": lambda: COMMON_REPORT_SECTIONS,
    "unified_access_gateway": lambda: [],
}

def generate_report(data, zip_path, component):
    if component not in REPORT_SECTIONS:
        raise ValueError(f"Invalid component: {component}")
     
    report = ""

    # Header
    report += header(zip_path, component)

    # Content
    sections = REPORT_SECTIONS.get(component, lambda: [])()

    for index, report_section in enumerate(sections):
        try:
            letter = string.ascii_uppercase[index]
            report += report_section(data, component, letter)

        except Exception as e:
            raise RuntimeError(
                f"Report Error in section '{report_section.__name__}' "
            ) from e

    # Footer
    report += footer(component)

    return report