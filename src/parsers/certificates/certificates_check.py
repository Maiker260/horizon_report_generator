import re
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.data.CERTIFICATE_DATA import CERTIFICATE_DATA

files = FILES_OF_INTEREST["certificates"]
keywords = DATA_TO_COLLECT["certificates"]

def certificates_check(zip_ctx):
    data = {}

    cert_sub_fields = {
        k.lower(): v for k, v in CERTIFICATE_DATA.items()
    }

    cert_start_pattern = re.compile(r"=+\s+Certificate\s+\d+\s+=+")
    field_pattern = re.compile(
        r"^\s*(" + "|".join(re.escape(k) for k in keywords) + r"):",
        re.IGNORECASE
    )

    for filename in files:
        if not zip_ctx.exists(filename):
            continue
    
        with zip_ctx.open(filename) as file:
            current_cert = None
            current_field = None
            cert_number = None

            for raw_line in file:
                line = raw_line.decode(errors="ignore")
                stripped = line.strip()

                cert_match = cert_start_pattern.search(line)
                if cert_match:
                    cert_number = int(re.search(r'Certificate\s+(\d+)', line).group(1))

                    data[cert_number] = {}
                    current_cert = data[cert_number]
                    current_field = None
                    continue

                if current_cert is None:
                    continue

                field_match = field_pattern.search(line)
                if field_match:
                    field_name = field_match.group(1).lower()
                    current_cert[field_name] = {}
                    current_field = field_name
                    continue

                if current_field and current_field in cert_sub_fields:
                    for sub_kw in cert_sub_fields[current_field]:
                        if sub_kw.lower() in stripped.lower():
                            current_cert[current_field].setdefault(sub_kw, []).append(stripped)

    return data