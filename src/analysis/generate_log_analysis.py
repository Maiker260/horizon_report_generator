from src.analysis.report.generate_report import generate_report
from src.analysis.processing.gather_data import gather_data

def generate_log_analysis(zip_path, zip_ctx, component, feature):
    data = gather_data(zip_ctx, component)
    report = generate_report(data, zip_path, component, feature)

    return report