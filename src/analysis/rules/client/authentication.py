from src.analysis.utils.rule_constructor import Rule

AUTHENTICATION_RULES = [
    # Rule(
    #     name="Logging in to a Horizon View Connection Server using Smartcard Authentication fails",
    #     category="authencation",
    #     match_type="contains",
    #     patterns=[
    #         "The user's tokenGroups attribute needs to be obtained so that their group membership based entitlements can be determined",
    #         "Please ensure in Active Directory that the computer account for this Connection Server has access to this user's tokenGroups attribute",
    #     ],
    #     source_files=[
    #         r"horizon-protocol-.*\.log", r".*-horizon-client-.*\.txt"
    #     ],
    #     recommendations=[
    #         "failed to return any values. This occurs when access to tokenGroups is denied in Active Directory",
    #         "This error typically indicates that a certificate issue is impeding connection",
    #         "In the Client, try setting the 'Certificate Checking Mode' to 'Do not verify server identity certificates'"
    #     ],
    #     references=[
    #         "https://kb.omnissa.com/s/article/2103964"
    #     ]
    # ),
]