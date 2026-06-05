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
        "VMware"
    ],
    "installed_software": {
        "Horizon": {
            "Omnissa": ["omnissa"],
            "VMware": ["vmware"]
        }
    },
    "log_level": {
        "registry_suffix": [
            r"Omnissa\Horizon",
            r"SOFTWARE\VMware, Inc.\VMware VDM"
        ],
        "values": [
            "DebugEnabled",
            "TraceEnabled"
        ]
    }
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
            80, 443, 8443, 4172, 389, 3389, 22389, 22636,
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
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
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
            "registry_suffix": [
                r"Installer\Features_HorizonAgent",
                "WebRTCRedir"
            ],
            "values": [
                "BlastUDP",
                "ClientDriveRedirection", 
                "FIDO2Redirection",
                "PrintRedir", 
                "ScannerRedirection", 
                "SmartCard", 
                "StorageDriveRedir", 
                "USB",
                "teamsEnabled"
            ],
        },
        "log_level_features": {
            "registry_suffix": [
                "UsbRedirection",
                "PrintRedir",
                "ViewScanner",
                "FIDO2",
                "SDR",
                "RTAV",
            ],
            "values": ["loglevel"]
        },
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
    },

    "client": {
        "device_info": COMMON_DATA_TO_COLLECT["device_info"],
        "horizon_services": COMMON_DATA_TO_COLLECT["horizon_services"],
        "horizon_ports": [443, 4172, 8443, 3389, 22443, 9427, 32111],
        "installed_software": COMMON_DATA_TO_COLLECT["installed_software"],
        "log_level": COMMON_DATA_TO_COLLECT["log_level"],
    },

    "unified_access_gateway": {
        "uag_info": {
            "General": [
                "uagName",
                "fipsEnabled",
                "deploymentOption",
                "ip0",
                "netmask0",
                "ip1",
                "netmask1",
                "ip2",
                "netmask2",
                "defaultGateway",
                "dns",
                "tls11Enabled",
                "tls12Enabled",
                "tls13Enabled",
                "hostClockSyncEnabled",
            ],
            "Horizon": [
                "minSHAHashSize",
                "healthCheckUrl",
                "blastExternalUrl",
                "pcoipExternalUrl",
                "proxyDestinationUrl",
                "proxyDestinationUrlThumbprints",
                "tunnelExternalUrl",
            ]
        },
        "horizon_ports": [9443, 443, 8443, 22443, 4172, 3389, 9427, 32111, 5500]
    },
}