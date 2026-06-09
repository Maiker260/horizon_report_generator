from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.uag.authentication import AUTHENTICATION_RULES
from src.analysis.rules.uag.certificate import CERTIFICATE_RULES
from src.analysis.rules.uag.general import GENERAL_RULES
from src.analysis.rules.uag.network import NETWORK_RULES

UAG_RULESET = compile_rules(
    AUTHENTICATION_RULES 
    + CERTIFICATE_RULES 
    + GENERAL_RULES 
    + NETWORK_RULES
)