COMMON_DATA_TO_COLLECT = {
    "device_info": [
        "Host Name", 
        "OS Name", 
        "OS Version", 
        "System Boot Time",
        "Time Zone",
        "Network Card(s)"
    ],
    "horizon_services": [
        "Omnissa", 
        "VDMDS", 
        "VMware"
    ],
    "installed_software": {
        "horizon": [
            "Omnissa", "VMware"
        ]
    },
}

DATA_TO_COLLECT = {
    "connection_server": {
        "device_info": (
            COMMON_DATA_TO_COLLECT["device_info"] +
            [
                "Domain",
                "Original Install Date",
                "Total Physical Memory",
                "Available Physical Memory",
                "Hotfix(s)",
            ]
        ),
        "server_roles": [],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": [
            80, 443, 8443, 4172, 3389, 22389, 22636,
            18443, 4001, 4002, 4100, 4101, 8009, 8472,
        ],
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "certificates": [
            "serial number",
            "signature algorithm",
            "issuer",
            "subject",
            "certificate extensions",
            "cert_friendly_name_prop_id(11)"
        ],
    },

    "agent": {
        "device_info": (
            COMMON_DATA_TO_COLLECT["device_info"] +
            [
                "Domain",
                "Original Install Date",
                "Total Physical Memory",
                "Available Physical Memory",
                "Hotfix(s)",
            ]
        ),
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": [3389, 4172, 22443, 9427, 32111, 4001, 4002, 55000],
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "horizon_features": {
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Omnissa\Horizon\Installer\Features_HorizonAgent": [
                "ClientDriveRedirection", 
                "PrintRedir", 
                "ScannerRedirection", 
                "SmartCard", 
                "StorageDriveRedir", 
                "USB"
            ],
        }
        
    },

    "client": {
        "device_info": COMMON_DATA_TO_COLLECT["device_info"],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": [443, 4172, 8443, 3389, 22443, 9427, 32111],
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
    },

    "unified_access_gateway": {},
}