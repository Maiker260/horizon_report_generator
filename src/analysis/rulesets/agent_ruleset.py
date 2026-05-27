from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.agent.customization import CUSTOMIZATION_RULES

AGENT_RULESET = compile_rules(
    CUSTOMIZATION_RULES
)