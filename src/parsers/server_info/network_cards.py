import re

def parse_nics(lines):
    cards = []
    current = None

    for raw_line in lines:
        line = raw_line.strip()

        nic_match = re.match(r"\[(\d+)\]:\s+(?![0-9a-fA-F:]+$)(.+)", line)

        if nic_match:
            if current:
                cards.append(current)

            current = {
                "Index": nic_match.group(1),
                "Adapter": nic_match.group(2),
                "Connection Name": None,
                "IP Addresses": []
            }
            continue

        if not current:
            continue

        if "Connection Name" in line:
            current["Connection Name"] = line.split(":", 1)[1].strip()

        elif re.search(r"\[\d+\]:\s+.+", line):
            ip = line.split(":", 1)[1].strip()
            current["IP Addresses"].append(ip)

    if current:
        cards.append(current)

    return cards