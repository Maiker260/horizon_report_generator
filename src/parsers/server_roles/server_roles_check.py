from src.data.UNWANTED_ROLES import UNWANTED_ROLES
from src.data.FILES_OF_INTEREST import FILES_OF_INTEREST

def server_roles_check(zip_ctx, component):
    files = FILES_OF_INTEREST[component]["server_roles"]
    data = {}

    for filename in files:
        if not zip_ctx.exists(filename):
            continue

        with zip_ctx.open(filename) as file:
            for raw_line in file:
                line = raw_line.decode(errors="ignore").lower()

                for role, keywords in UNWANTED_ROLES.items():
                    if role in data:
                        continue

                    for kwd in keywords:
                        if kwd.lower() in line:
                            data[role] = {
                                "status": "Found",
                                "evidence": kwd,
                                "file": filename
                            }

                            break
    
    return data