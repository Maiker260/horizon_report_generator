import datetime

date = datetime.datetime.now()

def header(zip_path, component):
    component = component.replace("_", " ").title()
    now = date.strftime("%c")

    field_names = [
        "Generated",
        "Horizon Product",
        "Bundle",
    ]

    max_width = max(len(key + ":") for key in field_names)

    header = []
    header.append("=" * 50)
    header.append("LOG BUNDLE REPORT")
    header.append(f"{'Generated' + ':':<{max_width}}  {now} (Local Time)")
    
    header.append(f"{'Bundle' + ':':<{max_width}}  {zip_path}")
    header.append(f"{'Horizon Product' + ':':<{max_width}}  {component}")
    header.append("=" * 50)

    return "\n".join(header)