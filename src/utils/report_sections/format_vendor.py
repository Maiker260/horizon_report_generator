from src.data.BRAND_FIXES import BRAND_FIXES

def format_vendor(name):
    name = name.strip().lower()
    return BRAND_FIXES.get(name, name.title())