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
    slow_print("Let the challenge begin!")
    print("=" * 60 + "\n")

def display_menu():
    """Display category menu"""
    print("=" * 60)
    slow_print("*** CATEGORIES ***", 0.06)
    slow_print("1. Music")
    slow_print("2. Flowering plants")
    slow_print("3. Machine learning algorithms")
    slow_print("4. Wild animals")
    print("=" * 60 + "\n")

    while True:
        try:
            user_category = int(input("Select a category by entering the number: "))
            break
        except ValueError:
            print("Please enter a number: ")

    if user_category == 1:
        return "List of music artists and bands from England"
    elif user_category == 2:
        return "Flowering plants"
    elif user_category == 3:
        return "Machine learning algorithms"
    elif user_category == 4:
        return "Wild animals"
    else:
        return "User selected category doesn't exist"





