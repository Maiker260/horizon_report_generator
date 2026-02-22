from src.report.sections.header import header
from src.report.sections.server_information import server_information
from src.report.sections.server_roles import server_roles
from src.report.sections.running_services import running_services
from src.report.sections.open_ports import open_ports
from src.report.sections.installed_applications import installed_applications

def generate_report(data, zip_path):
    # # Check Data
    # for section, content in data.items():
    #     if content:
    #         print(f"{section}:\n")
    #         for k, v in content.items():
    #             print(f"   {k}: {v}\n")
    #     else:
    #         print(f"{section}:\n")
    #         print("   None\n")

    try:
        report = ""
        report += header(zip_path)
        report += server_information(data)
        report += server_roles(data)
        report += running_services(data)
        report += open_ports(data)
        report += installed_applications(data)

        print(report)
    except Exception as e:
            print(e)

    # with open("report.txt", "w") as file:
    #     file.write(report)