FILES_OF_INTEREST = {
    "connection_server": [
        "ldap_replica_status.txt", 
        r"debug-.*\.txt", 
        "info.log", 
        r"vminst.*\.log",
        "absg.log"
    ],
    "unified_access_gateway": [
        "admin.log", 
        "bsg.log", 
        "esmanager.log",
        "authbroker.log"
    ],
    "agent": [
        r"debug-.*\.txt", 
        "setuperr.log", 
        r".*-html5Server-.*\.log", 
        r"vminst.*\.log", 
        r"Blast-Worker-.*\.log",
    ],
    "client": [
        r"horizon-protocol-.*\.log", 
        r".*-horizon-client-.*\.txt",
        r"horizon-crtbora.*\.log",
        r"debug-.*\.txt",
    ],
}
