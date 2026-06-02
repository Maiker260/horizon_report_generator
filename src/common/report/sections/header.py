import datetime
from src.common.report.utils.NAME_FIXES import FEATURE_FIXES

date = datetime.datetime.now()

def header(zip_path, component, feature, log_level):
    component = component.replace("_", " ").title()
    now = date.strftime("%c")

    field_names = [
        "Generated",
        "Horizon Product",
        "Bundle",
        "Horizon Log Level"
    ]

    max_width = max(len(key + ":") for key in field_names)

    header = []
    header.append("=" * 50)
    header.append(FEATURE_FIXES[feature].upper())
    header.append(f"{'Generated' + ':':<{max_width}}  {now} (Local Time)")
    
    header.append(f"{'Bundle' + ':':<{max_width}}  {zip_path}")
    header.append(f"{'Horizon Product' + ':':<{max_width}}  {component}")

    if log_level:
        header.append(f"{'Horizon Log Level' + ':':<{max_width}}  {log_level}")
        
    header.append("=" * 50)

    return "\n".join(header)