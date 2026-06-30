import sys
from pathlib import Path
from src.main import main

if len(sys.argv) < 2:
    print("No ZIP file was provided.")
    sys.exit(1)

zip_path = Path(sys.argv[1])
feature = sys.argv[2]

# Test

# zip_path = Path("tmp") / "Agent-2406.zip"
# zip_path = Path("tmp") / "Agent-2512.zip"
# zip_path = Path("tmp") / "Client-2406.zip"
# zip_path = Path("tmp") / "Client-2512T.zip"
# zip_path = Path("tmp") / "Client-Testi.zip"
# zip_path = Path("tmp") / "CS-2406.zip"
# zip_path = Path("tmp") / "CS-2512.zip"
# zip_path = Path("tmp") / "CS-Test1.zip"
# zip_path = Path("tmp") / "CS-Test2.zip"
# zip_path = Path("tmp") / "CS-Test3.zip"
# zip_path = Path("tmp") / "CS-Test4.zip"
# zip_path = Path("tmp") / "CS-Test5-20sBrete.zip"
# zip_path = Path("tmp") / "NDC.zip"
# zip_path = Path("tmp") / "UAG-Testi.zip"
# zip_path = Path("tmp") / "UAG-2406 Testi.zip"
# zip_path = Path("tmp") / "UAG-2512.zip"
# zip_path = Path("tmp") / "FIX-CS.zip"
# zip_path = Path("tmp") / "FIX-Client.zip"
# zip_path = Path("tmp") / "FIX-AGENT.zip"

# feature = "summary_report"
# feature = "log_analysis"

main(zip_path, feature)