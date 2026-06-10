from src.analysis.report.generate_report import generate_report
from src.analysis.processing.gather_data import gather_data
from src.analysis.processing.ProgressWindow import ProgressWindow

def generate_log_analysis(zip_path, zip_ctx, component, feature):
    progress_window = ProgressWindow()

    try:
        data = gather_data(zip_ctx, component, progress_window.update_progress)
        report = generate_report(data, zip_path, component, feature)

        return report
    
    finally:
        progress_window.close()