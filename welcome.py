import time


def slow_print(text, delay=0.06):
    """ time for displaying the text """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # new line at the end


def display_welcome_message():
    """Display welcome message"""
    print("=" * 60)
    slow_print("WELCOME TO TRUE OR FALSEOPEDIA!", 0.06)
    slow_print("The ultimate Wikipedia truth challenge!\n", 0.06)

    slow_print("Each round uses a real Wikipedia article.")
    slow_print("The AI generates two statements:")
    slow_print("• One TRUE")
    slow_print("• One FALSE (but convincing)\n")

    slow_print("Your mission: SPOT THE LIE!\n", 0.06)
    slow_print("Final results:")
    slow_print("3/3 -> Well done — you beat the AI!")
    slow_print("0/3 -> The AI controls you!")
    slow_print("1–2 -> The AI almost fooled you!\n")

    slow_print("Let the challenge begin!")
    print("=" * 60 + "\n")
    #input("Press ENTER to continue...\n")  # pause for dramatic effect


def display_menu():
    """Display category menu"""
    print("=" * 60)
    slow_print("*** CATEGORIES ***", 0.06)
    slow_print("1. Music")
    slow_print("2. Science")
    slow_print("3. History")
    slow_print("4. Geography")
    print("=" * 60 + "\n")
    input("Select a category by entering the number: ")



