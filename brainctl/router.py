# brainctl/router.py

"""
Routes incoming questions to the appropriate skill via the SkillRegistry.
"""

from brainctl.worker_rick.core import SkillRegistry

def forward_question(question: str) -> str:
    """Forward a user question to the registered skill handler."""
    return SkillRegistry.handle_question(question)

