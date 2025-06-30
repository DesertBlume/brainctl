# brainctl/config.py

from dotenv import load_dotenv
load_dotenv()
import sys
import os
from pathlib import Path

# Ensure project root is in sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Centralized paths
SRC_PATH = project_root / "brainctl"
SKILLS_PATH = SRC_PATH / "worker_rick" / "skills"
TESTS_PATH = SRC_PATH / "tests"

# API Keys (set these as environment variables)
HIBP_API_KEY = os.getenv("HIBP_API_KEY")
OWM_API_KEY = os.getenv("OWM_API_KEY")

# Default values (overridden at runtime)
USE_REMOTE_RICK = False
REMOTE_RICK_URL = None

