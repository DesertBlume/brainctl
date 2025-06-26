# brainctl/config.py

import sys
from pathlib import Path

# Ensure project root is in sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Centralized paths
SRC_PATH = project_root / "brainctl"
SKILLS_PATH = SRC_PATH / "worker_rick" / "skills"
TESTS_PATH = SRC_PATH / "tests"

