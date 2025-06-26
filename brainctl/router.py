# rick_brain/router.py

from worker_rick.core import SkillRegistry

def forward_question(question: str) -> str:
    return SkillRegistry.handle_question(question)

