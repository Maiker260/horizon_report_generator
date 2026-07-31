def format_addresses(addresses):
    if len(addresses) == 1:
        return addresses[0]
    
    return ", ".join(addresses)