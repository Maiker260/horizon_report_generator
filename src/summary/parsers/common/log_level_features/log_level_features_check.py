from src.summary.data.FILES_OF_INTEREST import FILES_OF_INTEREST
from src.summary.data.DATA_TO_COLLECT import DATA_TO_COLLECT
from src.summary.utils.extract_reg_key_info import extract_reg_key_info

def log_level_features_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["log_level_features"]
    features = DATA_TO_COLLECT[component]["log_level_features"]

    return extract_reg_key_info(zip_ctx, files, features)