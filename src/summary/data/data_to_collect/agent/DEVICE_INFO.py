from src.summary.data.data_to_collect.COMMON_DATA_TO_COLLECT import COMMON_DATA_TO_COLLECT

AGENT_DEVICE_INFO = (
    COMMON_DATA_TO_COLLECT["device_info"] +
    [
        "Domain",
        "Original Install Date",
        "Total Physical Memory",
        "Available Physical Memory",
        "Hotfix(s)",
    ]
)