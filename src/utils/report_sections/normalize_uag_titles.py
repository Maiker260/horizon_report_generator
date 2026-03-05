import re

ACRONYMS = {
    "tls": "TLS",
    "sha": "SHA",
    "url": "URL",
    "ip": "IP",
    "uag": "UAG",
    "pcoip": "PCoIP",
    "fips": "FIPS",
}

def normalize_uag_titles(text: str) -> str:
    text = text.replace("_", " ")

    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)
    text = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", text)

    words = text.split()
    normalized_words = []

    for word in words:
        lower_word = word.lower()

        match = re.match(r"(tls)(\d+)", lower_word)
        if match:
            _, version = match.groups()
            if len(version) == 2:
                version = f"{version[0]}.{version[1]}"
            normalized_words.append(f"TLS {version}")
            continue

        if lower_word in ACRONYMS:
            normalized_words.append(ACRONYMS[lower_word])
        else:
            normalized_words.append(word.capitalize())

    return " ".join(normalized_words)