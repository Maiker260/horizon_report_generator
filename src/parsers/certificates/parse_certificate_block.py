from .constants import (
    SERIAL_RE,
    ALGO_RE,
    CN_RE,
    NOT_BEFORE_RE,
    NOT_AFTER_RE,
    FRIENDLY_RE,
    SAN_ENTRY_RE,
    SECTION_HEADERS,
)


def parse_certificate_block(lines):
    cert = {
        "archived": False,
        "has_private_key": False,
        "private_key_exportable": None,
    }

    section = None
    capture_next = None

    simple_handlers = [
        (SERIAL_RE, "serial_number"),
        (NOT_BEFORE_RE, "not_before"),
        (NOT_AFTER_RE, "not_after"),
    ]

    for line in lines:
        stripped = line.strip()

        # Detect if the certificate is archived
        if stripped.startswith("Archived"):
            cert["archived"] = True
            continue

        # Detect Private key
        if stripped.startswith("Private Key:"):
            cert["has_private_key"] = True
            cert["private_key_exportable"] = True
            continue

        if "Private key is not exportable" in stripped:
            cert["has_private_key"] = True
            cert["private_key_exportable"] = False
            continue

        # Simple lines
        for pattern, field_name in simple_handlers:

            match = pattern.search(line)
            if (match):
                cert[field_name] = match.group(1).strip()
                break
        else:
            # Sections
            matched_section = False
            for header, sec_name in SECTION_HEADERS.items():
                if stripped.startswith(header):
                    cert[sec_name] = {}
                    section = sec_name
                    matched_section = True
                    break

            if matched_section:
                continue

            # Signature Algorithm
            if stripped.startswith("Signature Algorithm:") and "signature_algorithm" not in cert:
                section = "signature"
                continue

            if section == "signature":

                match = ALGO_RE.search(line)
                if (match):
                    cert["signature_algorithm"] = match.group(1).strip()
                    section = None
                continue

            # Friendly name
            if FRIENDLY_RE.search(line):
                capture_next = "friendly_name"
                continue

            if capture_next:
                if stripped:
                    cert[capture_next] = stripped
                capture_next = None
                continue

            # Subject Alternative Name
            if stripped.startswith("Subject Alternative Name"):
                cert["subject_alt_name"] = []
                section = "san"
                continue

            if section == "san":
                for match in SAN_ENTRY_RE.finditer(stripped):
                    cert["subject_alt_name"].append({
                        "type": match.group(1),
                        "value": match.group(2).strip()
                    })
                continue

            # issuer / subject
            if section in ("issuer", "subject"):

                match = CN_RE.search(line)
                if (match):
                    cert[section]["CN"] = match.group(1)

    return cert