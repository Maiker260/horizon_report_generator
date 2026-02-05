import re

def search_keyword(line, word):
    pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
    
    return bool(pattern.search(line))