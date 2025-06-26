# path_bootstrap.py

import sys
from pathlib import Path

def boost_imports():
    project_root = Path(__file__).resolve().parent
    rick_brain = project_root / "rick_brain"

    # Add project root and rick_brain to sys.path
    for path in [project_root, rick_brain]:
        str_path = str(path)
        if str_path not in sys.path:
            sys.path.insert(0, str_path)

