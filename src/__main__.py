import sys
from pathlib import Path
from src.main import main

# if len(sys.argv) < 2:
#     print("No ZIP file was provided.")
#     sys.exit(1)

# zip_path = Path(sys.argv[1])
# feature = sys.argv[2]

zip_path = Path("tmp") / "CS-2406.zip"
# feature = "log_summary"
feature = "log_analysis"

main(zip_path, feature)