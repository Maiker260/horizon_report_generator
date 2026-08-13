SOFTWARE_RULES = {
    "Antivirus/EDR": {

        "Microsoft": [
            "microsoft defender",
            "windows defender",
            "defender for endpoint",
            "microsoft defender for servers",
            "microsoft defender for business",
            "microsoft defender xdr",
            "sense",
        ],

        "Symantec / Broadcom": [
            "symantec endpoint protection",
            "symantec endpoint"
        ],

        "Norton": [
            "norton 360",
            "norton security"
        ],

        "McAfee / Trellix": [
            "mcafee",
            "mcafee endpoint security",
            "mcafee agent",
            "trellix",
            "trellix endpoint security",
            "trellix agent"
        ],

        "Trend Micro": [
            "trend micro",
            "apex one",
            "officescan",
            "trend micro deep security",
            "trend micro worry free",
            "deep security agent",
        ],

        "Kaspersky": [
            "kaspersky",
            "kaspersky endpoint security",
            "kaspersky security center"
        ],

        "Tanium": [
            "tanium",
            "tanium client",
        ],

        "ESET": [
            "eset",
            "nod32",
            "eset protect",
            "eset endpoint"
        ],

        "Bitdefender": [
            "bitdefender",
            "gravityzone",
            "gravity zone",
            "bitdefender endpoint security tools",
            "bitdefender eps"
        ],

        "Sophos": [
            "sophos",
            "intercept x",
            "sophos endpoint",
            "sophos central"
        ],

        "CrowdStrike": [
            "crowdstrike",
            "crowdstrike falcon",
            "falcon sensor",
            "crowdstrike identity protection"
        ],

        "SentinelOne": [
            "sentinelone",
            "sentinel one",
            "sentinel one agent",
            "sentinelone ranger",
            "sentinel agent",
        ],

        "Wazuh": [
            "wazuh",
            "wazuh agent",
        ],

        "Cylance / BlackBerry": [
            "cylance",
            "cylance protect",
            "cylanceoptics",
            "blackberry protect",
            "blackberry cylance"
        ],

        "Palo Alto Networks": [
            "cortex xdr",
            "cortex prevent",
            "palo alto cortex"
        ],

        "Fortinet": [
            "forticlient",
            "forticlient ems",
            "fortiedr"
        ],

        "Avast / AVG": [
            "avast",
            "avg antivirus"
        ],

        "Webroot": [
            "webroot",
            "secureanywhere",
            "webroot secureanywhere"
        ],

        "Malwarebytes": [
            "malwarebytes",
            "malwarebytes endpoint protection",
            "malwarebytes nebula"
        ],

        "Carbon Black / VMware": [
            "carbon black",
            "carbon black cloud",
            "carbon black defense",
            "vmware carbon black"
        ],

        "FireEye": [
            "fireeye",
            "fireeye endpoint"
        ],

        "Check Point": [
            "check point",
            "check point harmony",
            "check point endpoint security"
        ],

        "Tenable": [
            "tenable",
            "tenable agent",
            "nessus agent",
        ],

        "Cisco": [
            "cisco secure endpoint",
            "cisco amp",
            "amp for endpoints"
        ],

        "Comodo": [
            "comodo",
            "comodo advanced endpoint protection"
        ],

        "ZoneAlarm": [
            "zonealarm"
        ],

        "WithSecure / F-Secure": [
            "f-secure",
            "withsecure",
            "withsecure elements",
            "f-secure elements"
        ],

        "Panda Security": [
            "panda security",
            "panda adaptive defense",
            "panda endpoint protection"
        ],

        "VIPRE": [
            "vipre",
            "vipre endpoint security"
        ],

        "G DATA": [
            "g data",
            "gdata endpoint protection"
        ],

        "ClamAV": [
            "clamav",
            "clamwin"
        ],

        "AhnLab": ["ahnlab"],
        "Avira": ["avira", "avira endpoint", "avira antivirus pro"],
        "Cybereason": ["cybereason"],
        "Deep Instinct": ["deep instinct"],
        "Emsisoft": ["emsisoft"],
        "Ikarus": ["ikarus"],
        "Morphisec": ["morphisec"],
        "Qualys": ["qualys agent"],
        "Rapid7": ["rapid7 insight agent"],
        "SecureWorks": ["secureworks", "secureworks red cloak", "secureworks taegis"],
        "Total Defense": ["total defense"],
        "WatchGuard": ["watchguard endpoint", "watchguard epdr"],
        "Quick Heal / Seqrite": ["quick heal", "seqrite"],
        "Dr.Web": ["dr web"]
    },

    "Firewall / Network Security": {
        "Cloudflare": [
            "cloudflare warp",
            "cloudflare warp client",
            "cloudflare",
        ],

        "Cisco": [
            "cisco secure endpoint",
            "cisco amp",
            "amp for endpoints",
            "cisco umbrella",
        ],

        "Microsoft": [
            "azure vpn",
            "azure network adapter",
            "microsoft tunnel",
        ],

        "Forcepoint": [
            "forcepoint",
            "forcepoint one",
            "forcepoint endpoint",
        ],

        "Symantec / Broadcom": [
            "symantec endpoint protection",
            "symantec web protection",
            "symantec web security",
        ],

        "McAfee / Trellix": [
            "mcafee",
            "trellix",
            "trellix web control",
            "trellix endpoint security",
        ],

        "Zscaler": ["zscaler"],
        "Check Point": ["check point"],
        "Netskope": ["netskope"],
        "iboss": ["iboss"],
        "Palo Alto Networks": ["globalprotect"],
    },

    "Monitoring Agent": {
        "Datadog": [
            "datadog",
            "datadog agent",
        ],

        "New Relic": [
            "new relic",
            "newrelic",
            "new relic infrastructure agent",
        ],

        "Sentry": [
            "sentry",
            "sentry agent",
        ],

        "AppDynamics": [
            "appdynamics",
            "appdynamics agent",
        ],

        "SolarWinds": [
            "solarwinds",
            "solarwinds agent",
        ],

        "ScienceLogic": [
            "sciencelogic",
            "sl1 agent",
        ],

        "Splunk": [
            "splunk",
            "splunk universal forwarder",
        ],

        "Elastic": [
            "elastic agent",
            "elastic beats",
            "filebeat",
            "winlogbeat",
        ],

        "ControlUp": ["controlup"],
        "Nexthink": ["nexthink"],
        "Lakeside": ["lakeside"],
        "SysTrack": ["systrack"],
        "Liquidware": ["liquidware"],
        "UberAgent": ["uberagent"],
        "Dynatrace": ["dynatrace", "dynatrace oneagent", "dynatrace one agent"]
    },

    "Remote Tool": {
        "RustDesk": [
            "rustdesk",
        ],

        "Chrome Remote Desktop": [
            "chrome remote desktop",
            "chromeremotedesktop",
        ],

        "Splashtop": [
            "splashtop",
            "splashtop streamer",
            "splashtop remote",
        ],

        "RemotePC": [
            "remotepc",
        ],

        "Zoho": [
            "zoho assist",
            "zoho",
        ],

        "GoTo": [
            "gotoassist",
            "goto resolve",
            "logmein",
        ],

        "DWService": [
            "dwagent",
            "dwservice",
        ],

        "MeshCentral": [
            "meshcentral",
            "mesh agent",
        ],

        "TeamViewer": ["teamviewer"],
        "AnyDesk": ["anydesk"],
        "ConnectWise": ["connectwise"],
        "Kaseya": ["kaseya"],
        "ScreenConnect": ["screenconnect"],
        "LogMeIn": ["logmein"],
        "BeyondTrust": ["beyondtrust"]
    },

    "VPN Agent": {
        "OpenVPN": [
            "openvpn",
            "openvpn connect",
        ],

        "WireGuard": [
            "wireguard",
        ],

        "GlobalProtect": [
            "globalprotect",
            "pan gps",
        ],

        "Citrix": [
            "citrix secure access",
            "citrix gateway",
        ],

        "F5": [
            "f5 vpn",
            "f5 big-ip edge client",
            "big-ip edge",
        ],

        "SonicWall": [
            "sonicwall",
            "sonicwall netextender",
            "sonicwall vpn"
        ],

        "Pulse Secure": [
            "pulse secure",
            "pulse secure client",
        ],

        "OpenConnect": [
            "openconnect",
        ],

        "Cisco AnyConnect": ["anyconnect"],
        "Netskope": ["netskope"],
        "Ivanti": ["ivanti"],
    }
}