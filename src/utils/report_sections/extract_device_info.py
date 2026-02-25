from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT

def extract_device_info(data, component):
    sys_info = data.get("systeminfo", {})

    fields = (
        DATA_TO_COLLECT.get(component, {}).get("device_info", [])
    )

    result = {}

    for field in fields:
        if field not in ["Network Card(s)", "Hotfix(s)"]:
            result[field] = sys_info.get(field, "N/A")

    if component == "connection_server":
        horizon_reg = data.get("horizon_reg", {})
        result["Horizon Fips Mode"] = horizon_reg.get("FipsMode", "N/A")

    return result