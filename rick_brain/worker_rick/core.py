# worker_rick/core.py

import importlib
import os
from pathlib import Path

# Skill prefix -> module.handle mapping
skill_registry = {}

def load_skills():
    skills_dir = Path(__file__).parent / "skills"
    for file in os.listdir(skills_dir):
        if file.endswith(".py") and file != "__init__.py":
            skill_name = file[:-3]  # Remove ".py"
            try:
                module = importlib.import_module(f"worker_rick.skills.{skill_name}")
                if hasattr(module, "handle"):
                    skill_registry[skill_name] = module.handle
                else:
                    print(f"⚠️ Skill '{skill_name}' does not have a 'handle()' function.")
            except Exception as e:
                print(f"❌ Failed to load skill '{skill_name}': {e}")

def handle_question(question: str) -> str:
    if ":" in question:
        prefix, content = question.split(":", 1)
        prefix = prefix.strip().lower()
        content = content.strip()

        if prefix in skill_registry:
            return skill_registry[prefix](content)
        else:
            return f"❓ Unknown skill '{prefix}'. Try one of: {list(skill_registry.keys())}"
    else:
        return "⚠️ Please use format like: search: your question here"

