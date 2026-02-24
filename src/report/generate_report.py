from src.report.sections.header import header
from src.report.sections.server_information import server_information
from src.report.sections.server_roles import server_roles
from src.report.sections.running_services import running_services
from src.report.sections.open_ports import open_ports
from src.report.sections.installed_applications import installed_applications
from src.report.sections.certificates import certificates
from src.report.sections.footer import footer
from pathlib import Path

def generate_report(data, zip_path):
    try:
        report = ""
        report += header(zip_path)
        report += server_information(data)
        report += server_roles(data)
        report += running_services(data)
        report += open_ports(data)
        report += installed_applications(data)
        report += certificates(data)
        report += footer()

        # print(report)
    except Exception as e:
            print(e)

    # Create .txt File
    base_name = "Horizon Report"
    extension = ".txt"
    file_path = Path(f"{base_name}{extension}")
    counter = 1

    while file_path.exists():
        file_path = Path(f"{base_name} ({counter}){extension}")
        counter += 1

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)