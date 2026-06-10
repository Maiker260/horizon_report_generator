from src.analysis.analyzers.analyze_logs import analyze_logs

def gather_data(zip_ctx, component, progress_callback=None):
    try:
        return analyze_logs(zip_ctx, component, progress_callback)

    except Exception as e:
        return [{
            "component": component,
            "error": str(e)
        }]