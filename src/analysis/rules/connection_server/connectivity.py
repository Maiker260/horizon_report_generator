from src.analysis.utils.rule_constructor import Rule

CONNECTIVITY_RULES = [
    Rule(
        name= "Unexpected Origin Found",
        category= "connectivity",
        match_type="regex",
        patterns= [
            r"ERROR.*Unexpected Origin:",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "Add the CSs, LBs and UAGs FQDNs to the locked.properties file",
        ],
        references= [
            "https://kb.omnissa.com/s/article/85801"
        ]
    ),
    Rule(
        name= "Configuring Windows Server 2012 to avoid port exhaustion with Horizon Connection Server",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[Root exception is java.net.SocketException: No buffer space available (maximum connections reached?): connect]",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "To avoid this problem, expand the dynamic port range for both UDP and TCP",
        ],
        references= [
            "https://kb.omnissa.com/s/article/85667"
        ]
    ),
    Rule(
        name= "Accessing connection server using HTML access results in the error message: Your session has expired",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "java.lang.IllegalStateException: removeAttribute: Session already invalidated",
            "at org.apache.catalina.session.StandardSession.removeAttribute(StandardSession.java:"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            'If you want to use a long expire time like 1 month or longer, disable session expiry on the connection server. Set "Global setting-> General Settings -> Forcibly Disconnect Users" to "Never" in the horizon admin page.',
        ],
        references= [
            "https://kb.omnissa.com/s/article/87762"
        ]
    ),
    Rule(
        name= 'After upgrading to Connection Server 2503, Users unable to launch VDIs with error message - "Failed to connect to the Connection Server"',
        is_version_specific= True,
        category= "connectivity",
        match_type="regex",
        patterns= [
            r"IDOR attempt from IP address .* failed - unmatched token"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000956"
        ]
    ),
    Rule(
        name= 'SQL exception when connecting to an Events Database after a Horizon Server Upgrade with "Certificates do not conform to algorithm constraints"',
        category= "connectivity",
        match_type="contains",
        patterns= [
            'Error: "Certificates do not conform to algorithm constraints"'
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "Upgrade certificates to use supported cipher suites of Horizon"
        ],
        references= [
            "https://kb.omnissa.com/s/article/90010"
        ]
    ),
    Rule(
        name= 'Connection Server is unable to connect to Horizon Events DB with error: "Event Database Configuration Error : Event database certificate is not trusted. Intermediate or root certificate has expired. Contact your administrator for assistance.”',
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[ExceptionHandlerAdvice] Invalid Certificate configured on Event Database Server."
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001069"
        ]
    ),
    Rule(
        name= 'A user launch request fails with the error message "Cannot create a new session: Maximum connections reached"',
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Cannot create a new session: Maximum connections reached"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/88476"
        ]
    ),
    Rule(
        name= "Horizon 2206 fails to connect to vCenter",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Certificates do not conform to algorithm constraintsat"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "In Horizon 2206, the list of acceptable certificate signature schemes has changed and may no longer include the algorithm used to sign the vCenter certificate"
        ],
        references= [
            "https://kb.omnissa.com/s/article/89331"
        ]
    ),
    Rule(
        name= "Agent Unreachable message in Administrator console report After upgrading Horizon agent",
        category= "connectivity",
        match_type="contains",
        patterns= [
            r"\[DesktopTracker\] CHANGEKEY message from agent.* is discarded as it cannot be validated"
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
        name= "Instant Clone Creation Error: Rare Edge Case A Horizon Agent sends session report message continuously with no delay leading to provisioning failures, machine status sync slowness and machines get stuck in maintenance mode or in a deleting state",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "HA message took a long time to process"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/92459"
        ]
    ),
    Rule(
        name= "AGENT_PENDING_EXPIRED - The pending session on machine has expired",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "has not been connected from the client within the allocated time, this may be due to a failure to make the protocol connection or an inability to log the user into the available session",
            "is logging off,notifying the service to block reconnects while this completes"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90352"
        ]
    ),
    Rule(
        name= "AGENT_CUSTOMIZATION_FAULT : Internal template vm-XXXX customization failed. Failed To Obtain Valid IP Address Instant Clone Creation Error",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Check DHCP server connectivity",
            "No valid network adapters found on vm",
            "Some adapters were disconnected"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90784"
        ]
    ),
    Rule(
        name= "Unified Access Gateway(UAG): UAG Gateway Error Messages in Horizon View Administrator Portal Dashboard",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[GWMonitor] Could not get health information for"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90749"
        ]
    ),
    Rule(
        name= "Unified Access Gateway(UAG): Error: CSRF attempt from IP address failed - missing token with pre-login message configured",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "failed - missing token"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/86416"
        ]
    ),
    Rule(
        name= "Unable to reconnect to Horizon Events DB, after upgrade to Horizon 2503",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Failed to recover events db connection",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000947"
        ]
    ),
    Rule(
        name= "FIPS Enabled Connection Server fails to connect to MS SQL database",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "org.bouncycastle.jsse.provider.ProvTlsClient.notifyAlertRaised raised fatal(2) certificate_unknown(46) alert: Failed to read record",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000928"
        ]
    ),
    Rule(
        name= "Horizon Connection Server Troubleshooting",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[ws_java_bridgeDLL] java.lang.OutOfMemoryError: Java heap space",
            "Disk space free threshold for log reached. No more messages will be logged until more disk space has become available or the threshold is reduced"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/83960"
        ]
    ),
    Rule(
        name= "HTTP error 500 when attempting to launch Horizon Desktops or Applications",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "[AbstractReloadingMetadataResolver] Unable to unmarshall metadata org.opensaml.saml.metadata.resolver",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/88281"
        ]
    ),
    Rule(
        name= 'The desktop sources for this desktop are not responding. Please try connecting to the desktop again later, or contact your system administrator" displayed when the number of desktops in the pool is less than the actual users',
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Error Message: failed launching connection: NoServersAvailableException$ServersNotRespondingException",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/59751"
        ]
    ),
    Rule(
        name= "Horizon Event DB Configuration Fails on a Non-English Operating System",
        category= "connectivity",
        match_type="contains",
        patterns= [
            "Unable to update database settings; database connection failed: Unable to create events tables: Invalid column name 'name'",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/85519"
        ]
    ),
]
