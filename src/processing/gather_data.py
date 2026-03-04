from src.data.COMPONENT_CHECKS import COMPONENT_CHECKS

def gather_data(zip_ctx, component):
    parsers = COMPONENT_CHECKS[component]["parsers"]
    data = {}

    for name, parser_func in parsers.items():
        try:
            if component == "unified_access_gateway":
                data[name] = parser_func(zip_ctx)
            else:
                data[name] = parser_func(zip_ctx, component)
        except Exception as e:
            data[name] = {
                "Error": str(e)
            }

    return data