import random

def user_info():
    user_name = input("Please enter a username: ")
    return user_name

def play_round(statements):
    player = user_info()
    quiz_statements = statements
    player_score = 0

    for i, item in enumerate(quiz_statements, start=1):
        correct_answer = item["true_statement"]
        wrong_answer = item["false_statement"]

        option_dict = assign_randomised_statements(correct_answer, wrong_answer)

        display_round(i, option_dict)  # prints the round

        user_answer = get_player_answer(option_dict, player)  # validated input

        player_score += check_answer(user_answer, option_dict, wrong_answer, player)  # add point if correct

    end_game(player_score, player)

def display_round(round_number, option_dict):
    """Display round number"""
    print(f"Round {round_number}, which one is False?")
    for letter, statement in option_dict.items():
        print(f" Choice {letter}: {statement}")

def check_answer(user_answer, option_dict, wrong_answer, player):
    """Check if user answer correct"""
    if option_dict[user_answer] == wrong_answer:
        print(f"Username {player}: Correct! You get 1 point.")
        return 1
    else:
        print(f"Username {player}: that was Incorrect answer!")
        return 0

def assign_randomised_statements(true_answer, false_answer):
    options = [true_answer, false_answer]
    random.shuffle(options)
    letter_choices = ["a", "b"]
    option_dict = dict(zip(letter_choices, options)) #zip combines the answers with the letter choices
    return option_dict

def get_player_answer(option_dict, player):
    """Get player answer"""
    #player = user_info()
    while True:
        answer = input("please choose the false statement (a/b): ").strip().lower() #input validation
        if answer in option_dict:
            return answer
        print(f"{player} That was an Invalid input! Please type one of:", ", ".join(option_dict.keys()))

def end_game(score, player):
    """Finish game"""
    print(f"Game over! Your score is {score}.")
    if score >= 3:
        print(f"{player} Great job. Go to the next round!")
    else:
        print(f"{player} AI fooled you. Better luck next time")
#need to add the replay button



