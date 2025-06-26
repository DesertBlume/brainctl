# brainctl/cli.py

"""
CLI entry point for brainctl.

Usage examples:
    $ brainctl start
    $ brainctl start --remote 192.168.1.50
    $ brainctl validate
    $ brainctl         # fallback to interactive menu
"""

import argparse
import sys
from brainctl import main as rick_main
from brainctl import config

def start_rick(remote_ip=None):
    if remote_ip:
        config.USE_REMOTE_RICK = True
        config.REMOTE_RICK_URL = f"http://{remote_ip}:5000/ask"
        print(f"🌐 Using remote Rick at {config.REMOTE_RICK_URL}")
    else:
        config.USE_REMOTE_RICK = False
        print("🤖 Using local Rick")

    rick_main.main()

def validate():
    print("🚧 Validation logic not implemented yet.")

def push_config():
    print("🚧 Push config not implemented yet.")

def score():
    print("🚧 Scoring logic not implemented yet.")

def interactive_menu():
    print("\n🧠 Welcome to brainctl!")

    while True:
        print("\nWhat would you like to do?\n")
        print("1) Start Rick (local)")
        print("2) Start Rick (remote)")
        print("3) Validate Infrastructure")
        print("4) Push Config")
        print("5) Score Results")
        print("0) Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            start_rick()
        elif choice == "2":
            ip = input("Enter remote Rick's IP address: ").strip()
            start_rick(remote_ip=ip)
        elif choice == "3":
            validate()
        elif choice == "4":
            push_config()
        elif choice == "5":
            score()
        elif choice == "0":
            print("👋 Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please try again.")

def run():
    parser = argparse.ArgumentParser(
        prog="brainctl",
        description="Rick-powered infrastructure automation CLI."
    )
    subparsers = parser.add_subparsers(dest="command")

    start_parser = subparsers.add_parser("start", help="Start Rick's Brain chatbot")
    start_parser.add_argument("--remote", metavar="IP", help="Use remote Rick instance at given IP")

    subparsers.add_parser("validate", help="Run infrastructure validator")
    subparsers.add_parser("push", help="Push configuration")
    subparsers.add_parser("score", help="Score validation results")

    args = parser.parse_args()

    if args.command == "start":
        start_rick(remote_ip=args.remote)
    elif args.command == "validate":
        validate()
    elif args.command == "push":
        push_config()
    elif args.command == "score":
        score()
    else:
        interactive_menu()

if __name__ == "__main__":
    run()

