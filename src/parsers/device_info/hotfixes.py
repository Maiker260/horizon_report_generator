import re

def parse_hotfixes(lines):
    hotfixes = []

    for line in lines:
        line = line.strip()
        
        # Match the pattern "[XX]: KBXXXX"
        match = re.match(r"\[\d+\]:\s+(KB\d+)", line)

        if match:
            hotfixes.append(match.group(1))
    
    return hotfixes