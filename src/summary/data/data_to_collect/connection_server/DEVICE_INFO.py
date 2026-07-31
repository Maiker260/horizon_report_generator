from src.summary.data.data_to_collect.COMMON_DATA_TO_COLLECT import COMMON_DATA_TO_COLLECT

CS_DEVICE_INFO = (
    COMMON_DATA_TO_COLLECT["device_info"] +
    [
        "Domain",
        "Original Install Date",
        "NUMBER_OF_PROCESSORS",
        "Total Physical Memory",
        "Available Physical Memory",
        "Hotfix(s)",
    ]
)