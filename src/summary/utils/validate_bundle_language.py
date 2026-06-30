from src.exceptions import UnsupportedComponentError

REQUIRED_SYSTEMINFO_KEYS = (
    "Host Name:",
    "OS Name:",
    "OS Version:",
    "System Boot Time"
)

def validate_bundle_language(zip_ctx):
    if not zip_ctx.exists("systeminfo.txt"):
        return

    with zip_ctx.open("systeminfo.txt") as f:
        systeminfo_text = f.read().decode("utf-8", errors="ignore")

    if not all(key in systeminfo_text for key in REQUIRED_SYSTEMINFO_KEYS):
        raise UnsupportedComponentError(
            "This support bundle was generated from a non-English Windows installation.\n\n"
            "The parser currently supports only Horizon bundles generated "
            "from English Windows installations."
        )