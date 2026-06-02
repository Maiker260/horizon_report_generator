from src.summary.parsers.device_info.reg_key_info.fips_check import fips_check
from src.summary.parsers.device_info.reg_key_info.log_level_check import log_level_check

def reg_keys(zip_ctx, filename, component):
    data = {}
    
    if component == "connection_server":
        data["FipsMode"] = fips_check(zip_ctx, filename)
    
    data["log_level"] =  log_level_check(zip_ctx, component)

    return data