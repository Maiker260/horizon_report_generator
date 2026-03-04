from src.data.HORIZON_COMPONENT_MARKERS import HORIZON_COMPONENT_MARKERS
from src.exceptions import UnsupportedComponentError

def detect_component(zip_ctx):
    scores = {k: 0 for k in HORIZON_COMPONENT_MARKERS}

    for component, evidence in HORIZON_COMPONENT_MARKERS.items():
        for d in evidence.get("dirs", []):
            if zip_ctx.exists_dir(d):
                scores[component] += 1

        for f in evidence.get("files", []):
            if zip_ctx.exists(f):
                scores[component] += 1

        for pattern in evidence.get("patterns", []):
            if zip_ctx.exists_pattern(pattern):
                scores[component] += 1

    best_component = max(scores, key=scores.get)
    best_score = scores[best_component]

    if best_score == 0:
        raise UnsupportedComponentError(
            "The provided ZIP file does not match any supported Horizon component.\n\n"
            "Please verify that you are analyzing a valid Horizon support bundle and not "
            "a nested bundle (ZIP file inside another ZIP file)."
        )

    return best_component