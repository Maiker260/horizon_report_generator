def extract_device_info(data):
    sys_info = data["systeminfo"]
    horizon_reg = data["horizon_reg"]

    return {
        "Hostname": sys_info.get("Host Name", "N/A"),
        "Windows Version": sys_info.get("OS Name", "N/A"),
        "Build Version": sys_info.get("OS Version", "N/A"),
        "Installation Date": sys_info.get("Original Install Date", "N/A"),
        "Uptime": sys_info.get("System Boot Time", "N/A"),
        "Time Zone": sys_info.get("Time Zone", "N/A"),
        "Total Memory": sys_info.get("Total Physical Memory", "N/A"),
        "Available Memory": sys_info.get("Available Physical Memory", "N/A"),
        "Domain": sys_info.get("Domain", "N/A"),
        "Horizon Fips Mode": horizon_reg.get("FipsMode", "N/A"),
    }