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