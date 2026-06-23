from src.analysis.utils.compile_rules import compile_rules
from src.analysis.rules.connection_server.replication import REPLICATION_RULES
from src.analysis.rules.connection_server.connectivity import CONNECTIVITY_RULES
from src.analysis.rules.connection_server.provisioning import PROVISION_RULES
from src.analysis.rules.connection_server.console import CONSOLE_RULES
from src.analysis.rules.connection_server.authentication import AUTHENTICATION_RULES
from src.analysis.rules.connection_server.customization import CUSTOMIZATION_RULES
from src.analysis.rules.connection_server.upgrade import UPGRADE_RULES

CONNECTION_SERVER_RULESET = compile_rules(
    REPLICATION_RULES 
    + CONNECTIVITY_RULES 
    + PROVISION_RULES
    + CONSOLE_RULES
    + AUTHENTICATION_RULES
    + CUSTOMIZATION_RULES
    + UPGRADE_RULES
)