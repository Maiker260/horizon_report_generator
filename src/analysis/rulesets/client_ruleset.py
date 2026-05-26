from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.client.network import NETWORK_RULES

CLIENT_RULESET = compile_rules(
    NETWORK_RULES
)