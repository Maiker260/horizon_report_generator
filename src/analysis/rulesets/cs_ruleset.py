from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.connection_server.replication import REPLICATION_RULES
from src.analysis.rules.connection_server.connectivity import CONNECTIVITY_RULES

CONNECTION_SERVER_RULESET = compile_rules(
    REPLICATION_RULES +
    CONNECTIVITY_RULES
)

