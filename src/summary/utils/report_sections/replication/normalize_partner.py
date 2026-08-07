def normalize_partner(partner):
    if partner == "Unknown":
        return partner

    parts = partner.split("$", 1)

    if len(parts) == 1:
        return partner

    return (
        f"{parts[0]} (Global)"
        if parts[1] == "OmnissaHzeDSG"
        else parts[0]
    )