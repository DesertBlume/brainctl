# worker_rick/skills/help.py
from worker_rick.core import skill_registry

def handle(_: str) -> str:
    return "Here are the available skills:\n" + "\n".join(f"- {s}" for s in skill_registry)

