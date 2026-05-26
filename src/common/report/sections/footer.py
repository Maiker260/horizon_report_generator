from src.common.report.utils.section_title import section_title

def footer(component, feature):
    content = []
    content.append("\n\n\n\n\n\n\n")
    
    # References and Notes
    content.append(section_title("REFERENCES & NOTES"))
    
    content.append("\n*IMPORTANT NOTE: A manual review of the original evidence files is recommended to confirm findings and ensure accuracy.")
    
    content.append(feature(component))

    # Disclaimer
    content.append(section_title("DISCLAIMER"))

    content.append("\nThis tool is not an official product of Omnissa, VMware, or any other software vendor mentioned in this document. It is not endorsed, certified, or supported by any vendor.")
    content.append("\nUse of this report and its findings is at the discretion and responsibility of the reviewing party.")

    content.append("\n- Created by: Miker Gutierrez - https://github.com/Maiker260")
    content.append("- Source Code: https://github.com/Maiker260/horizon_report_generator")

    content.append("")
    content.append("")

    return "\n".join(content)