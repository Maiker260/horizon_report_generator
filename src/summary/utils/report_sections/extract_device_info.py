from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT

def extract_device_info(data, component):
    sys_info = data.get("systeminfo", {})
    set_file = data.get("set", {})

    info = {
        **sys_info,
        **set_file
    }

    fields = (
        DATA_TO_COLLECT.get(component, {}).get("device_info", [])
    )

    result = {}

    for field in fields:
        if field not in ["Network Card(s)", "Hotfix(s)"]:
            result[field] = info.get(field, "N/A")

    return result