from src.summary.parsers.connection_server.replication.PATTERNS import PARTNER_PATTERN

def parse_partner(line, data):
    # Detect and register a replication partner.

    partner_match = PARTNER_PATTERN.search(line)

    if not partner_match:
        return None

    partner = partner_match.group(1)

    if partner not in data["neighbors"]:
        data["neighbors"].append(partner)

    return partner