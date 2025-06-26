# rick_brain/config.py

import sys
from pathlib import Path

# Ensure brainctl/ root is in the import path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Useful paths
SKILLS_PATH = project_root / "rick_brain" / "worker_rick" / "skills"
TESTS_PATH = project_root / "tests"

