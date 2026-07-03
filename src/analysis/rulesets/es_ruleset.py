from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.enrollment_server import TRUESSO_RULES

ENROLLMENT_SERVER_RULESET = compile_rules(
    TRUESSO_RULES
)