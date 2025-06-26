# generate_tests.py

from pathlib import Path

skills_dir = Path("worker_rick/skills")
tests_dir = Path("tests")
template = """
from worker_rick.skills import {skill}

def test_{skill}_handle():
    result = {skill}.handle("test input")
    assert isinstance(result, str)
    assert result  # Ensure it's not empty
"""

def generate_tests():
    for file in skills_dir.glob("*.py"):
        if file.name == "__init__.py":
            continue
        skill_name = file.stem
        test_file = tests_dir / f"test_{skill_name}.py"
        if test_file.exists():
            print(f"✅ Test for '{skill_name}' already exists.")
            continue
        with test_file.open("w") as f:
            f.write(template.strip().format(skill=skill_name))
        print(f"🆕 Created test for '{skill_name}'.")

if __name__ == "__main__":
    generate_tests()

