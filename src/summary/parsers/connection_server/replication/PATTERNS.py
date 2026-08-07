import re

REPLICATION_SECTIONS = {
    "==== INBOUND NEIGHBORS ======================================": "inbound",
    "==== OUTBOUND NEIGHBORS FOR CHANGE NOTIFICATIONS ============": "outbound",
}

NAMING_CONTEXTS = {
    "CN=Configuration,": "Configuration",
    "CN=Schema,": "Schema",
    "DC=vdi,DC=vmware,DC=int": "Horizon",
    "DC=vdi,DC=horizon,DC=internal": "Horizon",
    "DC=vdiglobal,DC=vmware,DC=int": "Horizon Global",
    "DC=vdiglobal,DC=horizon,DC=internal": "Horizon Global",
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