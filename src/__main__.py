import sys
from pathlib import Path
from src.main import main

if len(sys.argv) < 2:
    print("Usage: loganalysis <zipfile>")
    sys.exit(1)

zip_path = Path(sys.argv[1])
# zip_path = Path("tmp") / "CS-2512.zip"

main(zip_path)