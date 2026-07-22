import re
from src.common.utils.read_file_with_auto_encoding import read_file_with_auto_encoding
from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST

def replication_status_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["replication"]

    data = {
        "neighbors": [],
        "transport": None,
        "kcc_connections": 0,
        "kcc_failures": None,
        "replication_errors": None,

        "inbound": {
            "Configuration": [],
            "Schema": [],
            "Horizon LDAP": [],
        },

        "outbound": {
            "Configuration": [],
            "Schema": [],
            "Horizon LDAP": [],
        },
    }

    sections = ["inbound", "outbound"]
    databases = ["DC=vdi,DC=vmware,DC=int", "DC=vdi,DC=horizon,DC=internal"]

    for filename in files:
        if not zip_ctx.exists(filename):
            return

        current_section = None
        current_nc = None

        with zip_ctx.open(filename) as file:
            reader = read_file_with_auto_encoding(file)

            for raw_line in reader:
                line = raw_line.strip()

                if not line:
                    continue

                # Detect sections
                if line == "==== INBOUND NEIGHBORS ======================================":
                    current_section = "inbound"
                    current_nc = None
                    continue

                if line == "==== OUTBOUND NEIGHBORS FOR CHANGE NOTIFICATIONS ============":
                    current_section = "outbound"
                    current_nc = None
                    continue

                if line == "==== KCC CONNECTION OBJECTS ============================================":
                    current_section = "kcc"
                    current_nc = None
                    continue

                # Partner / DSA
                if current_section in sections:
                    partner_match = re.search(
                        r"Default-First-Site-Name\\(.+?)\s+via\s+RPC",
                        line
                    )

                    if partner_match:
                        current_partner = partner_match.group(1)

                        if current_partner not in data["neighbors"]:
                            data["neighbors"].append(current_partner)

                        data["transport"] = "Intra-Site RPC"

                        continue

                # Replication Naming Context
                if current_section in sections:

                    if line.startswith("CN=Configuration,"):
                        current_nc = "Configuration"
                        continue

                    if line.startswith("CN=Schema,"):
                        current_nc = "Schema"
                        continue

                    if line in databases:
                        current_nc = "Horizon LDAP"
                        continue

                # Last attempt
                if current_section in sections:

                    attempt_match = re.search(
                        r"Last attempt @\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+was\s+(\w+)",
                        line,
                        re.IGNORECASE
                    )

                    if attempt_match and current_nc and current_partner:
                        timestamp = attempt_match.group(1)
                        status = attempt_match.group(2).upper()

                        data[current_section][current_nc].append({
                            "neighbor": current_partner,
                            "status": status,
                            "last_attempt": timestamp,
                        })

                        if status not in ("SUCCESS", "SUCCESSFUL"):
                            data["replication_errors"] = True

                        continue

                # KCC connection
                if current_section == "kcc":

                    connection_match = re.match(
                        r"Connection name\s*:\s*(.+)",
                        line,
                        re.IGNORECASE
                    )

                    if connection_match:
                        data["kcc_connections"] += 1
                        continue

                    if line == "No Failures.":
                        data["kcc_failures"] = None
                        continue

                    # KCC failure
                    if "Failure" in line or "failed" in line.lower():
                        data["kcc_failures"] = line
                        continue

        # Normalize empty values
        if not data["kcc_failures"]:
            data["kcc_failures"] = None

        if not data["replication_errors"]:
            data["replication_errors"] = None

    return data