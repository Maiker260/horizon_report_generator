import sys
from pathlib import Path
from src.main import main

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: HorizonReportGenerator <zipfile>")
        sys.exit(1)

    zip_path = Path(sys.argv[1])
    main(zip_path)