# rick_brain/router.py

from rick_brain.worker_rick.core import SkillRegistry

def forward_question(question: str) -> str:
    return SkillRegistry.handle_question(question)

