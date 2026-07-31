from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.summary.parsers.connection_server.replication.PATTERNS import REPLICATION_SECTIONS, KCC_SECTION
from src.summary.parsers.connection_server.replication.parsers.parse_naming_context import parse_naming_context
from src.summary.parsers.connection_server.replication.parsers.parse_partner import parse_partner
from src.summary.parsers.connection_server.replication.parsers.parse_replication_attempt import parse_replication_attempt
from src.summary.parsers.connection_server.replication.parsers.parse_kcc_line import parse_kcc_line
from src.summary.parsers.connection_server.replication.parsers.parse_options import parse_options

def parse_replication_file(zip_ctx, filename, data):
    # Parse a single replication log file.

    current_section = None
    current_nc = None
    current_partner = None
    current_attempt = None

    with zip_ctx.open(filename) as file:
        reader = read_file_with_auto_encoding(file)

        for raw_line in reader:

            line = raw_line.strip()

            if not line:
                continue

            # Replication options
            if parse_options(line, data):
                continue

            # Section detection
            section = REPLICATION_SECTIONS.get(line)
            
            if section:
                current_section = section
                current_nc = None
                current_partner = None
                current_attempt = None

                continue

            if line == KCC_SECTION:
                current_section = "kcc"
                current_nc = None
                current_partner = None
                current_attempt = None

                continue

            # Replication parsing
            if current_section in REPLICATION_SECTIONS.values():
                naming_context = parse_naming_context(line)

                if naming_context:
                    current_nc = naming_context
                    current_partner = None
                    current_attempt = None

                    continue
                
                partner = parse_partner(line, data)

                if partner:
                    current_partner = partner
                    data["transport"] = "Intra-Site RPC"

                    continue

                current_attempt = parse_replication_attempt(
                    line,
                    current_section,
                    current_nc,
                    current_partner,
                    current_attempt,
                    data,
                )

                continue

            # KCC parsing
            if current_section == "kcc":
                parse_kcc_line(line, data)