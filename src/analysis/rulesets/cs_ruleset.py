from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.connection_server.replication import REPLICATION_RULES
from src.analysis.rules.connection_server.connectivity import CONNECTIVITY_RULES
from src.analysis.rules.connection_server.provisioning import PROVISION_RULES

CONNECTION_SERVER_RULESET = compile_rules(
    REPLICATION_RULES +
    CONNECTIVITY_RULES +
    PROVISION_RULES
)

