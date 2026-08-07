from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.parsers.connection_server.replication.parsers.create_replication_data import create_replication_data
from src.summary.parsers.connection_server.replication.parsers.parse_replication_file import parse_replication_file
from src.summary.parsers.connection_server.replication.parsers.normalize_replication_data import normalize_replication_data

def replication_status_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["replication"]

    replication = {
        "local": None,
        "global": None,
    }

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        data = create_replication_data()

        parse_replication_file(zip_ctx, filename, data)
        normalize_replication_data(data)

        if filename.endswith("-global.txt"):
            replication["global"] = data
        else:
            replication["local"] = data

    return replication