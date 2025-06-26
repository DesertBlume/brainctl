# rick_brain/main.py

from path_bootstrap import boost_imports
boost_imports()

from rick_brain import config  # Ensures brainctl/ is in sys.path
from rick_brain.router import forward_question
from rick_brain.worker_rick.core import SkillRegistry

def main():
    print("🔧 Loading skills...")
    SkillRegistry.load_skills()
    print("✅ Ready! I'm Rick. Ask me anything:")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        response = forward_question(user_input)
        print(response)

if __name__ == "__main__":
    main()

