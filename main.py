import services.ai_service
from welcome import display_welcome_message, display_menu



def print_welcome(rounds):
    """
    1. welcome message
    2. game name
    3. how to play
    """
    pass

def main():
    """
    1. check if Open AI API key exists
    2. initiate GameService
    3. Game setup: fetch articles + generate statements
    4. run all rounds, collect answers, call game.play()
    5. show final score and result message
    """
    display_welcome_message()
    display_menu()

    #ai_service = services.ai_service.AI_service()
    #statements = ai_service.generate_statements()


if __name__ == "__main__":
    main()