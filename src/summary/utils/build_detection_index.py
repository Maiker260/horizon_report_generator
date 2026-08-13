import re

def build_detection_index(rules_dict):
    detection_index = []

    for category, vendors in rules_dict.items():
        for vendor, aliases in vendors.items():
            for alias in aliases:
                # Match aliases as complete words, ignoring case
                pattern = re.compile(
                    rf"\b{re.escape(alias)}\b",
                    re.IGNORECASE
                )
                
                detection_index.append({
                    "pattern": pattern,
                    "category": category,
                    "vendor": vendor,
                    "alias": alias
                })

    return detection_index