import sys
import argparse
from .core import rephrase

def main():
    parser = argparse.ArgumentParser(prog="gramem", description="{TONE} rephrasing")
    parser.add_argument("text", nargs="?")
    parser.add_argument("--process", action="store_true", help="read stdin")
    args = parser.parse_args()

    text = sys.stdin.read().strip() if args.process else args.text
    if not text:
        print("Usage: echo 'Hello {Formal}' | gramem --process")
        sys.exit(1)

    result = rephrase(text)
    print(result if result else "No valid {TONE} trigger. GRAMEM ENGINE")
    sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()