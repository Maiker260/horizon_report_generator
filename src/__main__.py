# import sys
from pathlib import Path
from src.main import main

# zip_path = Path(sys.argv[1])
zip_path = Path("tmp") / "Agent-2512.zip"
# zip_path = Path("tmp") / "CS-2512.zip"

main(zip_path)