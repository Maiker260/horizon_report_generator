import zipfile
from src.common.reader.file_reader import ZipContext
from src.common.processing.detect_component import detect_component
from src.common.processing.validate_bundle import validate_bundle
from src.common.report.save_error_log import save_error_log
from src.common.report.save_report import save_report
from src.summary.generate_summary_report import generate_summary_report
from src.analysis.generate_log_analysis import generate_log_analysis
from src.summary.utils.validate_bundle_language import validate_bundle_language

features = {    
    "summary_report": generate_summary_report,
    "log_analysis": generate_log_analysis
}

def main(zip_path, feature):
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            zip_ctx = ZipContext(zip_file)

            component = detect_component(zip_ctx)

            validate_bundle(zip_ctx, component)

            if feature == "summary_report":
                validate_bundle_language(zip_ctx)

            report = features[feature](zip_path, zip_ctx, component, feature)
            # print(report)
            report_path = save_report(report, component, feature, zip_path)

            return report_path

    except Exception as e:
        save_error_log(e, feature)
        raise