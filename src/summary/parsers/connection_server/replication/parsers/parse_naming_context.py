from src.summary.parsers.connection_server.replication.PATTERNS import NAMING_CONTEXTS

def parse_naming_context(line):
    # Detect a replication naming context from the current line.

    for prefix, naming_context in NAMING_CONTEXTS.items():

        if line.startswith(prefix) or line == prefix:
            return naming_context

    return None