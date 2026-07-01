from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    Rule(
        name= "Certain Smartcards do not function due to an incompatibility with newer windows crypto modules in Horizon 8.4 and later",
        category= "authentication",
        match_type="contains",
        patterns= [
            "Error code is 0xc0000225. Is the card inserted?",
            "is reporting that it has no card present"
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/90634"
        ]
    ),
    Rule(
        name= 'TrueSSO - Public Key Infrastructure: "The request is not supported" while launching a published Application or Desktop',
        category= "authentication",
        match_type="contains",
        patterns= [
            "Reported authentication failure. Status=0xC00000BB (WinErr=50)",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/59953"
        ]
    ),
    Rule(
        name='TrueSSO - Public Key Infrastructure - CRL : Error: "The attempted logon is invalid. The revocation status of the certificate used for authentication could not be determined',
        category="authentication",
        match_type="contains",
        patterns=[
            "This is either due to a bad username or authentication information. The revocation status of the certificate used for authentication could not be determined"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/89994"
        ]
    ),
    Rule(
        name="TrueSSO - Public Key Infrastructure: Certificate Distribution Point Location expiration results in a VDI Launch Failure",
        category="authentication",
        match_type="contains",
        patterns=[
            "Broker failed to provide a Certificate, Reason: Certificate generation request failed and not resubmitted"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90491"
        ]
    ),
    Rule(
        name='TrueSSO - Public Key Infrastructure - Error: "The attempted logon is invalid. This is either due to a bad username or authentication information. An untrusted certificate authority was detected while processing the domain controller certificate"',
        category="authentication",
        match_type="contains",
        patterns=[
            "An untrusted certificate authority was detected while processing the domain controller certificate used for authentication"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/94971"
        ]
    ),
]