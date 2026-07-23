import re

REPLICATION_SECTIONS = {
    "==== INBOUND NEIGHBORS ======================================": "inbound",
    "==== OUTBOUND NEIGHBORS FOR CHANGE NOTIFICATIONS ============": "outbound",
}

KCC_SECTION = "==== KCC CONNECTION OBJECTS ============================================"

NAMING_CONTEXTS = {
    "CN=Configuration,": "Configuration",
    "CN=Schema,": "Schema",
    "DC=vdi,DC=vmware,DC=int": "Horizon LDAP",
    "DC=vdi,DC=horizon,DC=internal": "Horizon LDAP",
}

SUCCESSFUL_ATTEMPT_PATTERN = re.compile(
    r"Last attempt @\s+"
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    r"\s+was\s+(successful)",
    re.IGNORECASE,
)

FAILED_ATTEMPT_PATTERN = re.compile(
    r"Last attempt @\s+"
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    r"\s+failed,\s+result\s+"
    r"(\d+)\s+\((0x[0-9a-fA-F]+)\)",
    re.IGNORECASE,
)

PARTNER_PATTERN = re.compile(
    r"Default-First-Site-Name\\(.+?)\s+via\s+RPC",
    re.IGNORECASE,
)

KCC_CONNECTION_PATTERN = re.compile(
    r"Connection name\s*:\s*(.+)",
    re.IGNORECASE,
)