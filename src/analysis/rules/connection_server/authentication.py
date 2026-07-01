from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    Rule(
        name="Logging in to a Horizon View Connection Server using Smartcard Authentication fails",
        category="authentication",
        match_type="contains",
        patterns=[
            "The user's tokenGroups attribute needs to be obtained so that their group membership based entitlements can be determined",
            "Please ensure in Active Directory that the computer account for this Connection Server has access to this user's tokenGroups attribute",
        ],
        source_files=[
            r"debug-.*\.txt"
        ],
        recommendations=[
            "To resolve this issue, provide the required permission to the user on the Active Directory"
        ],
        references=[
            "https://kb.omnissa.com/s/article/2103964"
        ]
    ),
    Rule(
        name= "SAML authentication fails in the Connection Server due to a ClassCastException encountered while resolving the SAML artifact",
        is_version_specific= True,
        category= "authentication",
        match_type="contains",
        patterns= [
            "java.lang.ClassCastException: class org.opensaml.saml.saml2.core.impl.StatusImpl cannot be cast to class org.opensaml.saml.saml2.core.ArtifactResponse",
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations= [],
        references= [
            "https://kb.omnissa.com/s/article/6001000"
        ]
    ),
    Rule(
        name="Unified Access Gateway(UAG): Unable to configure Ping IDP",
        category="authentication",
        match_type="contains",
        patterns=[
            "InvalidArgument(parameter: server.staticMetadata): StaticMetadata with this entityID already in use"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/81209"
        ]
    ),
    Rule(
        name='[Nutanix]Horizon Agent Installation on Golden Image Fails with "Authentication (AuthSSPI) AcceptSecurityContext Failed" During Registration',
        is_version_specific= True,
        category="authentication",
        match_type="contains",
        patterns=[
            "Authentication (AuthSSPI) function AcceptSecurityContext failed, return value"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/6001394"
        ]
    ),
    Rule(
        name='Smart card login for Horizon administrators option does not function. Error "A valid smart card is required for login. Please try again"',
        category="authentication",
        match_type="contains",
        patterns=[
            "UPN missing for mandatory smart card authentication for Admin",
            "Authentication failed, Unexpected fault: ERROR_AUTH_SMARTCARD_REQUIRED"
        ],
        source_files=[
            r"debug-.*\.txt",
        ],
        recommendations=[],
        references=[
            "https://kb.omnissa.com/s/article/83617"
        ]
    ),
]