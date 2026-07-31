def create_replication_data():
    # Create the initial replication data structure.

    return {
        "neighbors": [],
        # "transport": None,
        "DSA Options": None,
        "Site Options": None,
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
