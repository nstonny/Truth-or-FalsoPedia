import services.ai_service
from welcome import display_welcome_message, display_menu
from game.game_round import play_round
#import pygame

def main():
    # Set gold background for entire console session
    print("\033[48;2;255;215;0m\033[30m", end="")  # yellow background
    print("\033[38;2;128;0;128m", end="") #purple text

    display_welcome_message()
    user_choice = True
    while user_choice:
        user_display = display_menu()
        ai_service = services.ai_service.AI_service(user_display)
        statements = ai_service.generate_statements()
        play_round(statements)
        user_choice = input("Do you want to play again? Press y for yes and n for no: ")
        if user_choice.lower() == "n":
            print("Thank you for playing. Goodbye.") #replace with Stu's suggestion
            break

if __name__ == "__main__":
    main()