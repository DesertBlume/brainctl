# worker_rick/core.py

from path_bootstrap import boost_imports
boost_imports()

import importlib
import os
from pathlib import Path
from rick_brain.config import SKILLS_PATH

class SkillRegistry:
    _registry = {}

    @classmethod
    def load_skills(cls):
        skills_dir = SKILLS_PATH
        print(f"📂 Loading skills from: {skills_dir}")

        for file in os.listdir(skills_dir):
            if file.endswith(".py") and file != "__init__.py":
                skill_name = file[:-3]
                try:
                    module = importlib.import_module(f"rick_brain.worker_rick.skills.{skill_name}")
                    if hasattr(module, "handle"):
                        cls._registry[skill_name] = module.handle
                        print(f"✅ Registered skill: '{skill_name}'")
                    else:
                        print(f"⚠️ Skill '{skill_name}' does not have a 'handle()' function.")
                except Exception as e:
                    print(f"❌ Failed to load skill '{skill_name}': {e}")

        if cls._registry:
            print(f"🧠 Available skills: {', '.join(cls._registry)}")
        else:
            print("⚠️ No skills registered.")

    @classmethod
    def handle_question(cls, question: str) -> str:
        if ":" in question:
            prefix, content = question.split(":", 1)
            prefix = prefix.strip().lower()
            content = content.strip()

            if prefix in cls._registry:
                return cls._registry[prefix](content)
            else:
                return f"❓ Unknown skill '{prefix}'. Try one of: {', '.join(cls._registry)}"
        else:
            return "⚠️ Please use format like: search: your question here"

