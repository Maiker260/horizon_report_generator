import datetime

date = datetime.datetime.now()

def header(zip_path):
    now = date.strftime("%c")

    header = []
    header.append("=" * 50)
    header.append("SERVER REPORT")
    header.append(f"Generated: {now} (Local Time)")
    
    # NEED TO ADAPT DEPENDING OF EACH FILE
    header.append("Horizon Product: Connection Server")
    header.append(f"Bundle: {zip_path}")
    header.append("=" * 50)

    return "\n".join(header)