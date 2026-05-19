import sys
from pathlib import Path
from src.main import main

if len(sys.argv) < 2:
    print("No ZIP file was provided.")
    sys.exit(1)

zip_path = Path(sys.argv[1])
# zip_path = Path("tmp") / "CS-2406.zip"

main(zip_path)