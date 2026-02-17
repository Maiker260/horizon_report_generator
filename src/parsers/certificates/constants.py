import re

CERT_START_RE = re.compile(r"=+\s+Certificate\s+(\d+)\s+=+")

SERIAL_RE = re.compile(r"Serial Number:\s*(.+)")
ALGO_RE = re.compile(r"Algorithm ObjectId:\s*(.+)")
CN_RE = re.compile(r"CN=([^\s]+)")
NOT_BEFORE_RE = re.compile(r"NotBefore:\s*(.+)")
NOT_AFTER_RE = re.compile(r"NotAfter:\s*(.+)")
FRIENDLY_RE = re.compile(r"CERT_FRIENDLY_NAME_PROP_ID\(11\)")
SAN_ENTRY_RE = re.compile(r"(DNS Name|IP Address)=([^=\r\n]+?)(?=\s+(?:DNS Name|IP Address)=|$)")

SECTION_HEADERS = {
    "Issuer:": "issuer",
    "Subject:": "subject",
}