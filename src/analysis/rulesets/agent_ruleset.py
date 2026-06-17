from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.agent.customization import CUSTOMIZATION_RULES
from src.analysis.rules.agent.ms_teams import MS_TEAMS_RULES
from src.analysis.rules.agent.connectivity import CONNECTIVITY_RULES
from src.analysis.rules.agent.upgrade import UPGRADE_RULES
from src.analysis.rules.agent.authentication import AUTHENTICATION_RULES

AGENT_RULESET = compile_rules(
    CUSTOMIZATION_RULES 
    + MS_TEAMS_RULES
    + CONNECTIVITY_RULES
    + UPGRADE_RULES
    + AUTHENTICATION_RULES
)