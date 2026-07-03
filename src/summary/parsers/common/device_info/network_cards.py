import re
import ipaddress

def parse_nics(lines):
    cards = []
    current = None

    for raw_line in lines:
        line = raw_line.strip()

        nic_match = re.match(r"\[(\d+)\]:\s+(.+\s.+)", line)
        ip_match = re.match(r"\[\d+\]:\s+(\S+)", line)

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

        if line.startswith("Connection Name"):
            current["Connection Name"] = line.split(":", 1)[1].strip()
            continue

        if ip_match:
            ip_candidate = ip_match.group(1)

            try:
                ipaddress.ip_address(ip_candidate)
                current["IP Addresses"].append(ip_candidate)
            except ValueError:
                pass

    if current:
        cards.append(current)

    return cards