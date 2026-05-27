from src.summary.processing.gather_data import gather_data
from src.summary.report.generate_report import generate_report

def generate_summary_report(zip_path, zip_ctx, component, feature):
    data = gather_data(zip_ctx, component)
    report = generate_report(data, zip_path, component, feature)

    return report