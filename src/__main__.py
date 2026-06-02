import sys
from pathlib import Path
from src.main import main

if len(sys.argv) < 2:
    print("No ZIP file was provided.")
    sys.exit(1)

zip_path = Path(sys.argv[1])
feature = sys.argv[2]

# zip_path = Path("tmp") / "CS-2512.zip"
# zip_path = Path("tmp") / "Agent-2406.zip"
# zip_path = Path("tmp") / "Agent-2512.zip"
# zip_path = Path("tmp") / "Client-2406.zip"
# zip_path = Path("tmp") / "Client-2512T.zip"
# zip_path = Path("tmp") / "NDC.zip"
# zip_path = Path("tmp") / "UAG-2406 Testi.zip"

# feature = "summary_report"
# feature = "log_analysis"

main(zip_path, feature)