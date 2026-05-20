def format_section(data_dict):
    max_width = max(len(key) for key in data_dict.keys())

    lines = []
    for key, value in data_dict.items():
        lines.append(f"{key:<{max_width}} : {value}")

    return lines