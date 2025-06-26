# brainctl/main.py

from brainctl import config  # Just to ensure config loads, if needed
from brainctl.router import forward_question
from brainctl.worker_rick.core import SkillRegistry

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

