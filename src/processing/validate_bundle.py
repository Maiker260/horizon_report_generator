from src.data.BUNDLE_VALIDATION import BUNDLE_VALIDATION
from src.exceptions import UnsupportedComponentError

KEY_FIXES = {
    "connection_server": "Connection Server",
    "unified_access_gateway": "UAG",
}

def validate_bundle(zip_ctx, component):
    markers = BUNDLE_VALIDATION[component]
    component = KEY_FIXES.get(component, component.title())

    missing_required = [
        f for f in markers["required"] if not zip_ctx.exists(f)
    ]

    structural_found = any(
        zip_ctx.exists_dir(s) or zip_ctx.exists_pattern(s) or zip_ctx.exists(s)
        for s in markers["structural"]
    )

    if missing_required or not structural_found:
        raise UnsupportedComponentError(
            f"Incomplete {component} support bundle.\n\n"
            f"Missing required files: {missing_required}\n\n"
            "Please verify that you are analyzing a complete Horizon support bundle."
        )