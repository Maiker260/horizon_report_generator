from src.analysis.rulesets.uag_ruleset import UAG_RULESET
from src.analysis.rulesets.cs_ruleset import CONNECTION_SERVER_RULESET
from src.analysis.rulesets.agent_ruleset import AGENT_RULESET
from src.analysis.rulesets.client_ruleset import CLIENT_RULESET
from src.analysis.rulesets.es_ruleset import ENROLLMENT_SERVER_RULESET

RULESETS = {
    "unified_access_gateway": UAG_RULESET,
    "enrollment_server": ENROLLMENT_SERVER_RULESET,
    "connection_server": CONNECTION_SERVER_RULESET,
    "agent": AGENT_RULESET,
    "client": CLIENT_RULESET,
}