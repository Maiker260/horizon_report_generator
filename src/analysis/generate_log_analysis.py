import threading
from src.analysis.report.generate_report import generate_report
from src.analysis.processing.gather_data import gather_data
from src.analysis.processing.ProgressWindow import ProgressWindow

def generate_log_analysis(zip_path, zip_ctx, component, feature):
    progress_window = ProgressWindow()

    result = {}
    error = {}

    def analize_logs():
        try:
            data = gather_data(zip_ctx, component, progress_window.update_progress)
            result["report"] = generate_report(data, zip_path, component, feature)

        except Exception as e:
            error["exception"] = e

        finally:
            progress_window.close()

    thread = threading.Thread(
        target=analize_logs,
        daemon=True
    )

    thread.start()

    progress_window.window.mainloop()

    if "exception" in error:
        raise error["exception"]

    return result.get("report")