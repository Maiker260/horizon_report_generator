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
]