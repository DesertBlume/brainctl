# brainctl/router.py

"""
Routes incoming questions to the appropriate skill, either locally
via SkillRegistry or remotely via the Flask worker, depending on config.
"""

import requests
from brainctl import config
from brainctl.worker_rick.core import SkillRegistry

def forward_question(question: str) -> str:
    """Forward a user question to the appropriate local or remote handler."""
    if config.USE_REMOTE_RICK:
        try:
            response = requests.post(
                config.REMOTE_RICK_URL,
                json={"question": question},
                timeout=3
            )
            if response.status_code == 200:
                return response.json().get("response", "⚠️ No response from remote Rick.")
            else:
                return f"❌ Remote Rick error: HTTP {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"❌ Could not reach remote Rick: {e}"
    else:
        return SkillRegistry.handle_question(question)

