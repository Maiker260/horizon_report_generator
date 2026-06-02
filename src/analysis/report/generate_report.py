from src.common.report.sections.header import header
from src.analysis.report.sections.content import content
from src.common.report.sections.footer import footer
from src.analysis.report.sections.references_notes import analysis_references_notes

def generate_report(data, zip_path, component, feature):     
    report = ""
    log_level = False

    # Header
    report += header(zip_path, component, feature, log_level)

    # Content
    report += content(data)

    # Footer
    report += footer(component, analysis_references_notes)

    return report