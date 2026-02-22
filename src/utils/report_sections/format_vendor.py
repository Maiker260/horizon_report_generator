BRAND_FIXES = {

    # Microsoft
    "defender for endpoint": "Microsoft Defender for Endpoint",

    # McAfee / Trellix
    "mcafee": "McAfee",

    # Trend Micro
    "apex one": "Trend Micro Apex One",
    "officescan": "Trend Micro OfficeScan",

    # ESET
    "eset": "ESET",
    "nod32": "ESET NOD32",

    # Bitdefender
    "gravityzone": "Bitdefender GravityZone",

    # Sophos
    "intercept x": "Sophos Intercept X",

    # CrowdStrike
    "crowdstrike": "CrowdStrike",
    "falcon sensor": "CrowdStrike Falcon Sensor",

    # SentinelOne
    "sentinelone": "SentinelOne",

    # Palo Alto
    "cortex xdr": "Cortex XDR",
    "globalprotect": "GlobalProtect",

    # Fortinet
    "forticlient": "FortiClient",

    # Avast / AVG
    "avg antivirus": "AVG Antivirus",


    # FireEye
    "fireeye": "FireEye",

    # Cisco
    "cisco secure endpoint": "Cisco Secure Endpoint",
    "amp for endpoints": "Cisco AMP for Endpoints",
    "anyconnect": "Cisco AnyConnect",

    # ZoneAlarm
    "zonealarm": "ZoneAlarm",

    # F-Secure
    "f-secure": "F-Secure",

    # VIPRE
    "vipre": "VIPRE",

    # G DATA
    "g data": "G DATA",

    # ClamAV
    "clamav": "ClamAV",

    # Monitoring Agents
    "controlup": "ControlUp",
    "lakeside": "Lakeside SysTrack",
    "systrack": "SysTrack",
    "uberagent": "uberAgent",

    # Remote Tools
    "teamviewer": "TeamViewer",
    "anydesk": "AnyDesk",
    "connectwise": "ConnectWise",
    "screenconnect": "ScreenConnect",
    "logmein": "LogMeIn",
    "beyondtrust": "BeyondTrust",

    # VPN
    "sonicwall vpn": "SonicWall VPN",
}

def format_vendor(name):
    name = name.strip().lower()
    return BRAND_FIXES.get(name, name.title())