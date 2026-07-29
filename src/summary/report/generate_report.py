import string

from src.common.report.sections.header import header
from src.common.report.sections.footer import footer

from src.summary.report.sections.common.device_information import device_information
from src.summary.report.sections.common.running_services import running_services
from src.summary.report.sections.common.open_ports import open_ports
from src.summary.report.sections.common.installed_applications import installed_applications
from src.summary.report.sections.common.log_level_features import log_level_features
from src.summary.report.sections.connection_server.replication import replication
from src.summary.report.sections.connection_server.server_roles import server_roles
from src.summary.report.sections.connection_server.certificates import certificates
from src.summary.report.sections.connection_server.locked_properties import locked_properties
from src.summary.report.sections.connection_server.configuration import configuration
from src.summary.report.sections.agent.horizon_features import horizon_features
from src.summary.report.sections.uag.uag_info import uag_info
from src.summary.report.sections.enrollment_server.service_keys import service_keys
from src.summary.report.sections.enrollment_server.es_configuration import es_configuration
from src.summary.report.sections.references_notes import summary_references_notes

from src.summary.utils.report_sections.format_log_level import format_log_level

COMMON_REPORT_SECTIONS = [
    device_information,
    running_services,
    open_ports,
    installed_applications,
]

REPORT_SECTIONS = {
    "enrollment_server": lambda: (
        COMMON_REPORT_SECTIONS[:1]
        + [es_configuration]
        + [server_roles]
        + COMMON_REPORT_SECTIONS[1:]
        + [service_keys]
    ),
    "connection_server": lambda: (
        COMMON_REPORT_SECTIONS[:1]
        + [configuration]
        + [replication]
        + [server_roles]
        + COMMON_REPORT_SECTIONS[1:]
        + [certificates]
        + [locked_properties]
    ),
    "agent": lambda: (
        COMMON_REPORT_SECTIONS 
        + [horizon_features] 
        + [log_level_features]
    ),
    "client": lambda: (
        COMMON_REPORT_SECTIONS
        + [log_level_features]
    ),
    "unified_access_gateway": lambda: [
        uag_info, open_ports
    ],
}

def generate_report(data, zip_path, component, feature):
    report = ""
    log_level = None

    if component  != "unified_access_gateway":
        log_level = format_log_level(component, data["configuration"]["horizon_reg"]["log_level"])

    # Header
    report += header(zip_path, component, feature, log_level)

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
    report += footer(component, summary_references_notes)

    return report