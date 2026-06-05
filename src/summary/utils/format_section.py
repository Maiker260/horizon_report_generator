def format_section(data_dict, is_title = None):
    max_width = max(len(key) for key in data_dict.keys())

    lines = []
    for key, value in data_dict.items():
        label = f"{key}:"

        if is_title:
            lines.append(f"{label:<{max_width + 1}}  {value.title()}")
        else:
            lines.append(f"{label:<{max_width}}  {value}")

    return lines