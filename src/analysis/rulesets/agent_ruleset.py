from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.agent.customization import CUSTOMIZATION_RULES
from src.analysis.rules.agent.ms_teams import MS_TEAMS_RULES
from src.analysis.rules.agent.connectivity import CONNECTIVITY_RULES

AGENT_RULESET = compile_rules(
    CUSTOMIZATION_RULES 
    + MS_TEAMS_RULES
    + CONNECTIVITY_RULES
)