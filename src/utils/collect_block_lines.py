def collect_block_lines(file):
    lines = []
    next_line = None

    for raw_line in file:
        # Collect and return the lines that start with a space or with tab.
        if raw_line.startswith(b" ") or raw_line.startswith(b"\t"):
            lines.append(raw_line.decode(errors="ignore"))
        else:
            # Parsing will read the next line when its done, so it returns it back for parsing
            next_line = raw_line.decode(errors="ignore")
            break
    
    return lines, next_line