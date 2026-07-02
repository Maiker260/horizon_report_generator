from src.analysis.utils.rule_constructor import Rule

CONSOLE_RULES = [
    Rule(
        name= "After a reboot, the Horizon Connection Server may fail to start properly and users may be unable to connect",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "LDAP connection failure to 127.0.0.1:389",
            "Shared memory connection failure to Node Manager"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "The issue stops after changing the Omnissa Horizon Connection Server (wsbroker) service startup type to Automatic (Delayed Start)"
        ],
        references= [
            "https://kb.omnissa.com/s/article/6001393"
        ]
    ),
    Rule(
        name= "Omnissa Horizon Connection Server Inaccessible over HTTP/HTTPS",
        category= "console",
        match_type="contains",
        patterns= [
            "Certificate thumbprint verification failed, no matching thumbprint. Presented identity: router/cs-hostname",
            "General error occurred: Unexpected certificate: router/cs-hostname"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [
            "Contact Omnissa Support to obtain the resolution script", 
            "Run the script to resolve the issue"
        ],
        references= [
            "https://kb.omnissa.com/s/article/6000184"
        ]
    ),
    Rule(
        name= "After restarting a Connection Server, the error 'Cannot look up datacenter from Virtual Center.' is displayed in the Horizon Console",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "Attempt to update tracker ended with a permanent failure",
            "Failed to perform update on tracker after 3 attempts"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001328"
        ]
    ),
    Rule(
        name= "Horizon Admin Console not accessible after connection server upgrade",
        category= "console",
        match_type="contains",
        patterns= [
            "Error creating topic config for topic: TrackerTopic",
            "MS connection failed while connecting to topic",
            "javax.net.ssl.SSLHandshakeException: no cipher suites in common"
        ],
        source_files=[
            r"debug-.*\.txt", 
            "info.log"
        ],
        recommendations= [
            "Clearing the unsupported or deprecated cipher suites from the configuration. This will allow the application to fall back to its default set of supported cipher suites, ensuring compatibility and enabling successful TLS communication",
            "Configure the supported cipher suites as per the documentation to ensure TLS compatibility and resolve the issue"
        ],
        references= [
            "https://kb.omnissa.com/s/article/6001288"
        ]
    ),
    Rule(
        name= 'Horizon Connection Server Console displays "Internal Error Occurred", after an upgrade to 8.6 or later',
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "InvalidArgument(parameter: connectionServers): A null value is invalid",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/89986"
        ]
    ),
    Rule(
        name= '"Unable to connect" Error on Connection Server Admin Portal after Upgrade',
        category= "console",
        match_type="contains",
        patterns= [
            "Certificate authentication enabled, but no trustKeyfile specified",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/94287"
        ]
    ),
    Rule(
        name= "Horizon Connection server service goes down due to JMS exception",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "com.swiftmq.jms.RequestTimeoutException: Request time out (60000) ms!",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000997"
        ]
    ),
    Rule(
        name= 'Connection Server unable to accept vCenter thumbprint with an error "There was an error identifying the validity of the server"',
        category= "console",
        match_type="contains",
        patterns= [
            "[CertMatchingTrustManager] invalid certificate (and no trusted thumbprint) for",
            "message:'ValidateCertificateChain Result: FAIL, EndEntityReasons: , ChainReasons: partialChain, noTrust']",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [
            "Import the vCenter certificate along with the root certificates to Connection Server trusted root folder in all the connection server ( this is the windows certificate store"
        ],
        references= [
            "https://kb.omnissa.com/s/article/67701"
        ]
    ),
    Rule(
        name= "Viewdbchk scanMachines fails with failure of connection to vCenter Server",
        category= "console",
        match_type="contains",
        patterns= [
            "message:'ValidateCertificateChain Result: FAIL, EndEntityReasons: cantCheckRevoked, ChainReasons: partialChain, noTrust']",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/59635"
        ]
    ),
    Rule(
        name= "vCenter Server enters an error state when a replica Connection Server is added to your Horizon View Environment",
        category= "console",
        match_type="contains",
        patterns= [
            "NoTrustedThumbprintException: InvalidCertificateException[reasons:notTrusted;cantCheckRevoked;chainReasons:invalid",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/93701"
        ]
    ),
    Rule(
        name= "Installing the Omnissa Horizon View Client on a Connection Server interrupts Connection Server functionality",
        category= "console",
        match_type="contains",
        patterns= [
            "service::StartWinlogonNotification Failed Loading SysNtfy.dll: 0x8007007e",
            "[ws_winauth] Cannot load vlicheck dll, error: 126 (The specified module could not be found.)"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/2084138"
        ]
    ),
    Rule(
        name= 'After upgrade to Horizon Connection Server 2503, Connection Server settings cannot be saved due to the error "Failed to fetch GSS Authenticator Configuration"',
        category= "console",
        match_type="contains",
        patterns= [
            'Cannot invoke "com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer$ConnectionServerInfo.getId()" because "csInfo" is null at com.omnissa.vdi.vlsi.server.infrastructure.GSSAPIAuthenticatorManager.populateGSSAPIAuthenticatorInfo'
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000870"
        ]
    ),
    Rule(
        name= "Failure to upgrade to Horizon 2209 or Later from 2206 or earlier when message security is MIXED",
        category= "console",
        match_type="contains",
        patterns= [
            "[BrokerMessageSecurity]Could not configure message security: Invalid parameter for levelString: null",
            "Message validation failure: Mismatch of signature 'tunnel/ | MSMessageSecurity] Failed to sign message"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [
            "Set message security to ON or ENHANCED before upgrading and ensure all components have moved to your chosen steady-state mode."
        ],
        references= [
            "https://kb.omnissa.com/s/article/90251"
        ]
    ),
    Rule(
        name= "Dashboard alerts for unrecognized requests for XML Api protocol connection in Horizon 2209 (8.7) and above",
        category= "console",
        match_type="contains",
        patterns= [
            "[ConnectionServerHandler] Incrementing the warning count : Reason : unrecognized request detected"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90398"
        ]
    ),
    Rule(
        name= "Unable to connect to admin page and stops accepting Horizon Client connections at Horizon 2303 and later",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "PooledProcessor] Problem processing HTTP connection: Software caused connection abort: socket write error"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/93026"
        ]
    ),
    Rule(
        name= "Blast gateway not running when a Certificate generated from IIS is used",
        category= "console",
        match_type="contains",
        patterns= [
            "keystoreutil.exe failed to load certificate from",
            "Failed to acquire private key handle (error"
        ],
        source_files=[
            "absg.log",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/89820"
        ]
    ),
    Rule(
        name= "Unable to Add Virtual Desktops to Manual Pools with error: ADMIN_POOL_ADD_FAILED",
        category= "console",
        match_type="contains",
        patterns= [
            "Marshalling Error: Error writing request body to server",
            "Could not find cached VM %s to validate Storage Accelerator against"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001334"
        ]
    ),
    Rule(
        name= "Admin UI not loading because of the JMS errors during start up",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "[JMSMessagePublisher] Failed to publish message, keeping: com.swiftmq.jms.RequestTimeoutException: Request time out",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001245"
        ]
    ),
    Rule(
        name= "After upgrade to 2312.2, Events to File System stopped working",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "java.lang.ClassNotFoundException: org.apache.commons.io.FileUtils at java.base/java.net.URLClassLoader.findClass(Unknown Source)",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001037"
        ]
    ),
    Rule(
        name= "Horizon console is not displaying 'site name' under the 'guest customization' while editing or creating a pool",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "Error fetching sites from AD",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000146"
        ]
    ),
    Rule(
        name= "Horizon OCSP based revocation check doesn't work in FIPS installation",
        is_version_specific= True,
        category= "console",
        match_type="contains",
        patterns= [
            "Could not start the Ice Server MBean",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/93115"
        ]
    ),
    Rule(
        name= "PCoIP Security Gateway shows red alert in Services Status",
        category= "console",
        match_type="contains",
        patterns= [
            "Server certificate validation failed for host localhost, Cert CN PCoIP Security Gateway",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/84067"
        ]
    ),
    Rule(
        name= "Omnissa Horizon Admin Console inaccessible after importing CA signed certificate",
        category= "console",
        match_type="contains",
        patterns= [
            "Request contained unexpected header: vdmCertError=[]",
            "Request contained unexpected header: vdmConnectionSource=[]"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000390"
        ]
    ),
    Rule(
        name= 'Expanding VM for Dedicated Instant Clone Pool Fails with Error "Invalid Value for Member" in Horizon 8 (2312 and Later)',
        category= "console",
        match_type="contains",
        patterns= [
            "usedVMPolicy is only applicable for automated desktop pool with floating user assignment",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6000678"
        ]
    ),
    Rule(
        name= 'Horizon Console reports "Certificate Validation Failed" for vCenter after environmental maintenance',
        category= "console",
        match_type="contains",
        patterns= [
            "UnexpectedFault: Unexpected failure during certificate validation",
            "CERTIFICATE_VALIDATION_FAILED",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/86414"
        ]
    ),
    Rule(
        name= "Unable to load or edit Applications or Desktops in Horizon Console",
        category= "console",
        match_type="contains",
        patterns= [
            "Global entitlement dn must be present in global assignment",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/88797"
        ]
    ),
]