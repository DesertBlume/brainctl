# rick_brain/router.py

from worker_rick.core import handle_question

def forward_question(question: str) -> str:
    # Add more routing logic later (e.g., skill detection)
    return handle_question(question)

