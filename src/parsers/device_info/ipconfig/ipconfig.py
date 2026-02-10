from src.parsers.device_info.ipconfig.get_dns_server import get_dns_server

def ipconfig(zip_ctx, filename, current_data):
    if not zip_ctx.exists(filename):
        return
    
    cards = current_data["systeminfo"].get("Network Card(s)")
    if not cards:
        return
    
    nic_map = {
        card["Connection Name"]: card for card in cards
    }

    data = {}
    current_block = None
    block_lines = []

    with zip_ctx.open(filename) as file:
        for raw_line in file:
            line = raw_line.decode(errors="ignore")

            if current_block:
                if not line.strip() or line[0].isspace():
                    block_lines.append(line.strip())
                    continue

                data[current_block] = block_lines
                current_block = None
                block_lines = []

            for nic in nic_map:
                if nic in line:
                    current_block = nic
                    block_lines = []

    if current_block:
        data[current_block] = block_lines
    
    for nic_name, block in data.items():
        card = nic_map.get(nic_name)
        if not card:
            continue

        dns_list = get_dns_server(block)
        
        if dns_list:
            card["DNS Servers"] = dns_list