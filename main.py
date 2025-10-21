import argparse
import sys
import traceback

from agent.graph import agent


def main():
    parser = argparse.ArgumentParser(description="Run engineering project planner")
    parser.add_argument(
        "--recursion-limit", "-r", type=int, default=100,
        help="Recursion limit for processing (default: 100)"
    )

    args = parser.parse_args()

    try:
        print("=" * 60)
        print("🚀 Engineering Project Builder Started")
        print("=" * 60)
        user_prompt = input("Enter your project prompt: ")

        print("\n[1/4] 🧠 Running Planner Agent...")
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": args.recursion_limit}
        )

        print("\n[2/4] 🏗️  Architect Agent completed.")
        print("[3/4] 💻 Coder Agent executing implementation tasks...")
        print("[4/4] ✅ All tasks executed successfully.\n")

        print("=" * 60)
        print("🎉 Process finished successfully!")
        print("Final State Output:\n")
        print(result)
        print("=" * 60)

    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user.")
        sys.exit(0)

    except Exception as e:
        print("\n❌ An unexpected error occurred:\n", file=sys.stderr)
        traceback.print_exc()
        print(f"\nError message: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
