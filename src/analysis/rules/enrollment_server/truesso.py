from src.analysis.utils.rule_constructor import Rule

TRUESSO_RULES = [
    Rule(
        name='TrueSSO - Public Key Infrastructure: Unable to add a TrueSSO connector Cannot create connector on the enrollment server on a domain with NOT_VALID enrollment certificate status',
        category="truesso",
        match_type="contains",
        patterns=[
            "No valid Enrollment Certificates installed for forest",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/86228"
        ]
    ),
    Rule(
        name="TrueSSO - Enrollment Server unable to connect to CA: The authentication service is unknown",
        category="truesso",
        match_type="contains",
        patterns=[
            "The authentication service is unknown"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90682"
        ]
    ),
    Rule(
        name='TrueSSO - Public Key Infrastructure - CRL : Error: "Encountered unexpected error during execution" seen when using vdmutil to reconfigure Horizon TrueSSO',
        category="truesso",
        match_type="contains",
        patterns=[
            "LDAPObjectStore write() Naming Exceptionjavax.naming.directory.InvalidAttributeValueException: [LDAP: error code 19 - 000020B1: AtrErr: DSID-030F158A"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/85571"
        ]
    ),
    Rule(
        name="TrueSSO - Public Key Infrastructure: Certificate Distribution Point Location expiration results in a VDI Launch Failure",
        category="truesso",
        match_type="contains",
        patterns=[
            "The revocation function was unable to check revocation because the revocation server was offline"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/90491"
        ]
    ),
]