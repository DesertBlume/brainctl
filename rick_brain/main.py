# main.py

from router import forward_question
from worker_rick.core import load_skills

def main():
    print("🔧 Loading skills...")
    load_skills()
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

