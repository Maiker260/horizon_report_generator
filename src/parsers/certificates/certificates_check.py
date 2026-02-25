from .constants import CERT_START_RE
from .parse_certificate_block import parse_certificate_block
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST

def certificates_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["certificates"]
    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            current_cert_number = None
            buffer = []

            for raw_line in file:
                line = raw_line.decode(errors="ignore")

                match = CERT_START_RE.search(line)
                if (match):
                    if current_cert_number is not None:
                        data[current_cert_number] = parse_certificate_block(buffer)

                    current_cert_number = int(match.group(1))
                    buffer = []
                elif current_cert_number is not None:
                    buffer.append(line)

            if current_cert_number is not None:
                data[current_cert_number] = parse_certificate_block(buffer)

    return { certificate: info for certificate, info in data.items() if not info["archived"] }