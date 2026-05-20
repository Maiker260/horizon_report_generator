import re

def search_keyword(line, word):
    pattern = re.compile(rf"^{re.escape(word)}\s*:", re.IGNORECASE)
    
    return bool(pattern.search(line))