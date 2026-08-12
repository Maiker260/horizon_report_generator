from src.analysis.utils.rule_constructor import Rule

CONNECTIVITY_RULES = [
    Rule(
        name= "Agent secure pairing fails: No Network Communication between the View Agent and Connection Server",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Message could not be validated: Signature invalid for identity broker/broker",
            "java.lang.Exception: Identity validation failed: UNKNOWN is not known identity for: null"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "For affected customers uninstall Dynatrace OneAgent from the connection server machine",
        ],
        references= [
            "https://kb.omnissa.com/s/article/89582"
        ]
    ),
    Rule(
        name= "Agent Unreachable message in Administrator console report After upgrading Horizon agent",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[]The JVM has exited with code 6",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/2038679"
        ]
    ),
    Rule(
        name= 'Horizon View Manual Agent status "Waiting for Agent Communication"',
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[AgentRegistryConfig] Failed to get current MAC address. Restarting JMS",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/81895"
        ]
    ),
    Rule(
        name= 'Horizon Agent Authentication Failure in Multi-Domain Environments with Debug Message: "..Received partial credentials, no SSO" in the Agent log',
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[wsnm_desktop] StartSession APPLICATION request for user (null)",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000914"
        ]
    ),
    Rule(
        name= "Connectivity Issues with Agent Machines Configured with Multiple Distinct GPU Types",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "RegEnc-Intel: VNCEncodeRegionIntelCreate: Failed to create the Intel HW encoder sesFailed to destroy the Intel HW encoder. Status:MFX_ERR_INVALID_HANDLEsion",
        ],
        source_files=[
            r"Blast-Worker-.*\.log"
        ],
        recommendations= [
            "Disable the AMD display driver in Device Manager"
        ],
        references= [
            "https://kb.omnissa.com/s/article/6001373"
        ]
    ),
    Rule(
        name= "Cannot connect VDI with PCoIP due to insufficient TCP MSS in the network",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "MGMT_PCOIP_DATA :Invite packet not received, aborting session",
        ],
        source_files=[
            r"pcoip_server_.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/93504"
        ]
    ),
    Rule(
        name= "Horizon VGPU: Mouse Misbehavior and Session freezing over Blast",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Access is denied.), LocalSystem: True Removed reason: (0x00000000) : The operation completed successfully. trying again...",
        ],
        source_files=[
            r"Blast-Worker-SessionId.*\.log"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/94184"
        ]
    ),
    Rule(
        name= "Intermittent RDSH published App Launch failure",
        category= "connectivity",
        match_type="regex",
        patterns= [
            r"VMRdsProtocolListener.*::CreateSession\(\): Connection failed error 3",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/92943"
        ]
    ),
    Rule(
        name= "Omnissa Session Monitor fails to Start resulting in Horizon Agent Errors, including configuration errors",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[wsnm_desktop] Failed to open Session Monitor, status unexpected, error=2.  Windows Session Tracker watcher will retry in 10 seconds",
            "[ws_sm] Failed to open KSM status 5, error: 31.  Retrying in 10 seconds"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90648"
        ]
    ),
]