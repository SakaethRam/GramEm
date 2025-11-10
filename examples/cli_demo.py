# gramem-basic/examples/cli_demo.py

from gramem_basic import rephrase

# Simple interactive demo
if __name__ == "__main__":
    print("GramEm Basic Demo — Type with {TONE} and press Enter")
    print("Example: Hello world {Formal}")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye! GRAMEM ENGINE")
            break

        result = rephrase(user_input)
        if result:
            print(f"GramEm: {result}")
        else:
            print("Tip: Use {Formal}, {Casual}, {Professional}, or {Friendly}. GRAMEM ENGINE")