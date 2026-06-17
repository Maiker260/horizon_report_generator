from src.analysis.utils.rule_constructor import Rule

PROVISION_RULES = [
    Rule(
        name="Unable to create connection pool, Pre-authentication information was invalid (24)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "LdapException: unable to create connection pool, resultCode=82 (local error), errorMessage=An error occurred while attempting to initialize the JAAS login context for GSSAPI authentication: LoginException(Pre-authentication information was invalid (24))"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This can occur with multiple Active Directory sites environment where the virtual machine account creation and customization happen on different sites when the virtual machines are not yet fully replicated",
        ],
        references=[
            "https://kb.omnissa.com/s/article/2147129"
        ]
    ),
    Rule(
        name="Fail on the DNS Lookup in Active Directory",
        category="provisioning",
        match_type="contains",
        patterns=[
            "DnsException: Unable to DNS lookup for _kerberos._tcp.domain.name"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Ensure all basic connectivity checks are performed between the components involved",
        ],
        references=[
            "https://kb.omnissa.com/s/article/91068"
        ]
    ),
    Rule(
        name="Fail to create computer account, resultCode=52 (unavailable)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "- unable to create entry, resultCode=52 (unavailable)"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Indicates that the server is currently not available to process the requested operation",
            "Server not ready to process request",
            "Resources that the server is reliant on are unavailable due to administrative operations or other causes."
        ],
        references=[
            "https://kb.omnissa.com/s/article/91066"
        ]
    ),
    Rule(
        name="Fail to create computer account, resultCode=68 (entry already exists)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "resultCode=68 (entry already exists), errorMessage"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Indicates the presence of an existing entry in the database that is a match for the requested DN"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91066"
        ]
    ),
    Rule(
        name="Unable to create connection pool, resultCode=81 (Server Down)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "- unable to contact peer: unable to create entry, resultCode=81 (server down)"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Indicates that an existing connection to the server is no longer valid",
            "Check the if there are Antivirus or Firewall interference",
            "Check a Network issue",
        ],
        references=[
            "https://kb.omnissa.com/s/article/91071"
        ]
    ),
    Rule(
        name="Unable to create connection pool, ResultCode=91 (connect error)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "LdapConnectionException: unable to contact peer: unable to create connection pool, resultCode=91 (connect error)"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This code is indicative of a connection failure to the Domain Controller",
            "A server is currently down or not accepting new connections",
            "A networking problem prevents the Horizon agent machine from reaching the DC",
            "The client encounters a connection timeout before the connection can be established"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91071"
        ]
    ),
    Rule(
        name="Unable to create connection pool, KDC has no support for encryption type (14)",
        category="provisioning",
        match_type="contains",
        patterns=[
            "LoginException(KDC has no support for encryption type (14))"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Create a new instant clone domain user account in AD and use this account to provision pools"
        ],
        references=[
            "https://kb.omnissa.com/s/article/92285"
        ]
    ),
    Rule(
        name="Fail to reset computer account, resultCode=53 (unwilling to perform)",
        category="provisioning",
        match_type="regex",
        patterns=[
            r"AD_FAULT_FATAL.*resultCode=53 \(unwilling to perform\), errorMessage"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/92582"
        ]
    ),
    Rule(
        name="After waiting for 300 seconds internal template VM",
        category="provisioning",
        match_type="regex",
        patterns=[
            r"CPException: After waiting for 300 seconds internal template VM.*is still not powered off"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "The internal template has a default of 5 minutes (300 seconds) to complete customization before it will time out",
            "Domain join usually takes more than a minute. So for instance , if a gpupdate takes more than 4 minutes, it's going to timeout"
        ],
        references=[
            "https://kb.omnissa.com/s/article/76469"
        ]
    ),
    Rule(
        name="After waiting for 600 seconds Replica vm-xxxx still has not finished customization",
        category="provisioning",
        match_type="regex",
        patterns=[
            r"UNKNOWN_FAULT_FATAL After waiting for 600 seconds Replica.*still has not finished customization"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "As this is an intermittent issue, a second attempt at an image push is often successful",
            "Another option is to temporarily disable DRS during the image push to mitigate the intermittent failure risk of the replica-vm customization"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91753"
        ]
    ),
    Rule(
        name="Failed to retrieve snapshot for the vm",
        category="provisioning",
        match_type="contains",
        patterns=[
            "UNKNOWN_FAULT_FATAL: Failed to retrieve snapshot for the"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "The cause of this issue is related to the failure of Internal VM customization during the initial Push Image attempt, which prevents the snapshot from being taken",
            "If DEBUG mode is enabled, the problematic Internal VM will not be cleaned up, leading to errors during subsequent image pushes"
        ],
        references=[
            "https://kb.omnissa.com/s/article/91750"
        ]
    ),
    Rule(
        name="Please check the KMServers. None is available",
        category="provisioning",
        match_type="contains",
        patterns=[
            "CPException: Please check the KMServers. None is available"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This issue occurs due to a the KMS server(s) being unavailable",
            "Ensure that the correct KMS Servers are available and responsive on the KMIP port from the Esxi Hosts",
            "Validate the health and availability of certificates",
            "Add other Key Management Servers (KMS) as needed and as required"
        ],
        references=[
            "https://kb.omnissa.com/s/article/92109"
        ]
    ),
    Rule(
        name="VC_FAULT_FATAL- An error occurred while communicating with the remote host",
        category="provisioning",
        match_type="contains",
        patterns=[
            "Fault type is VC_FAULT_FATAL - An error occurred while communicating with the remote host"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This message is sent to Horizon when there is an issue with ESXi host communication",
            "Verify the health of the ESXi host identified in Horizon Logging as faulting - enter maintenance mode and restart",
        ],
        references=[
            "https://kb.omnissa.com/s/article/90419"
        ]
    ),
    Rule(
        name="VC_FAULT_FATAL - No host is compatible with the virtual machine",
        category="provisioning",
        match_type="contains",
        patterns=[
            "Fault type is VC_FAULT_FATAL - No host is compatible with the virtual machine"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This error is sent when there is an incompatibility with the host",
            "This might occur, for example, if no host can satisfy the virtual machine's CPU or memory resource needs or if no host currently has network or storage access needed by the virtual machine",
        ],
        references=[
            "https://kb.omnissa.com/s/article/90419",
            "https://knowledge.broadcom.com/external/article/320852/virtual-machine-not-compatible-with-any.html"
        ]
    ),
    Rule(
        name="VC_FAULT_FATAL - The host does not have sufficient memory resources to satisfy the reservation",
        category="provisioning",
        match_type="contains",
        patterns=[
            "CPVcSubsystemException: The host does not have sufficient memory resources to satisfy the reservation"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "This can be a reservation on memory/insufficient memory resources on the underlying host"
        ],
        references=[
            "https://kb.omnissa.com/s/article/90419"
        ]
    ),
    Rule(
        name="VC_FAULT_FATAL - javax.xml.ws.soap.SOAPFaultException fault was thrown by the VC server Instant Clone Creation Error",
        category="provisioning",
        match_type="contains",
        patterns=[
            "Cause: org.apache.cxf.binding.soap.SoapFault: Permission to perform this operation was denied"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "Validate vCenter permissions for the Account used by Horizon",
            "Browse the Vcenter directly with the Managed Object Browser (MOB) with the Horizon Credentials"
        ],
        references=[
            "https://kb.omnissa.com/s/article/90406"
        ]
    ),
    Rule(
        name="VC_FAULT_FATAL - javax.xml.ws.soap.SOAPFaultException fault was thrown by the VC server Instant Clone Creation Error",
        category="provisioning",
        match_type="contains",
        patterns=[
            "' has already been deleted or has not been completely created"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90406"
        ]
    ),
    Rule(
        name="SERVER_FAULT_FATAL: Unable to automatically reconnect to PBM subsystem Instant Clone Creation Error",
        category="provisioning",
        match_type="contains",
        patterns=[
            "[PBMClient] Connection Lost to PBM subsystem"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90575"
        ]
    ),
    Rule(
        name="AGENT_CUSTOMIZATION_FAULT - Internal template vm-XXXX customization failed Error description not set by agent Instant Clone Creation Error",
        category="provisioning",
        match_type="contains",
        patterns=[
            "customization failed. Error description not set by agent"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90781"
        ]
    ),
    Rule(
        name="AGENT_CUSTOMIZATION_FAULT - Internal template vm-XXXX customization failed Error Domain Join Failed. Verify DNS Failed In NGA Instant Clone Creation Error",
        category="provisioning",
        match_type="contains",
        patterns=[
            "customization failed Error Domain Join Failed. Verify DNS Failed In NGA"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90783"
        ]
    ),
]