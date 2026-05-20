import re

def get_dns_server(block):
    dns_list = []

    collecting_dns = False

    for raw_line in block:
        line = raw_line.strip()

        if "DNS Servers" in line:
            collecting_dns = True

            parts = line.split(":", 1)

            if len(parts) > 1:
                dns = parts[1].strip()
                
                if dns:
                    dns_list.append(dns)
            continue

        if collecting_dns:
            match = re.match(r"^[0-9]", line)
            
            if line and match:
                dns_list.append(line)
            else:
                break

    return dns_list