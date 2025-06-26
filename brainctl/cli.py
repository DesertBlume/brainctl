# brainctl/cli.py

"""
CLI entry point for brainctl.

Usage examples:
    $ brainctl start
    $ brainctl validate
    $ brainctl

If no arguments are passed, you'll be prompted interactively.
"""

import argparse
import sys
from brainctl import main as rick_main


def start_rick():
    rick_main.main()

def validate():
    print("🚧 Validation logic not implemented yet.")

def push_config():
    print("🚧 Push config not implemented yet.")

def score():
    print("🚧 Scoring logic not implemented yet.")

def interactive_menu():
    print("\n🧠 Welcome to brainctl!")

    action_map = {
        "1": start_rick,
        "2": validate,
        "3": push_config,
        "4": score,
        "0": lambda: sys.exit(0)
    }

    while True:
        print("\nWhat would you like to do?\n")
        print("1) Start Rick")
        print("2) Validate Infrastructure")
        print("3) Push Config")
        print("4) Score Results")
        print("0) Exit")

        choice = input("\nEnter your choice: ").strip()
        action = action_map.get(choice)

        if action:
            return action()
        else:
            print("❌ Invalid choice. Please try again.")

def run():
    parser = argparse.ArgumentParser(
        prog="brainctl",
        description="Rick-powered infrastructure automation CLI."
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("start", help="Start Rick's Brain chatbot")
    subparsers.add_parser("validate", help="Run infrastructure validator")
    subparsers.add_parser("push", help="Push configuration")
    subparsers.add_parser("score", help="Score validation results")

    args = parser.parse_args()

    command_map = {
        "start": start_rick,
        "validate": validate,
        "push": push_config,
        "score": score,
    }

    if args.command in command_map:
        command_map[args.command]()
    else:
        interactive_menu()


if __name__ == "__main__":
    run()

