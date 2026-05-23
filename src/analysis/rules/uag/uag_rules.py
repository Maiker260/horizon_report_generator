from src.analysis.rules.uag.authentication_rules import AUTHENTICATION_RULES
from src.analysis.rules.uag.certificate_rules import CERTIFICATE_RULES
from src.analysis.rules.uag.general_rules import GENERAL_RULES
from src.analysis.rules.uag.network_rules import NETWORK_RULES

UAG_RULES = (
    AUTHENTICATION_RULES +
    CERTIFICATE_RULES +
    GENERAL_RULES +
    NETWORK_RULES
)