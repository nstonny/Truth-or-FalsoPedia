import random
#from  ..services.ai_service import AI_service
#from .services import ai_service


"""def get_quiz_statement():
    #you need to get question from storage location
    service = AI_service()
    dummy_true_or_false =  service.generate_statements()

    return dummy_true_or_false"""


def play_round(statements):
    quiz_statements = statements
    player_score = 0
    for i, item in enumerate(quiz_statements, start=1):
        #get the statements
        correct_answer = item["true_statement"]
        wrong_answer = item["false_statement"]

      # randomised and assigned statements
        option_dict = assign_randomised_statements(correct_answer, wrong_answer)

        print(f"Round {i}, which one is False?")
        for letter, statement in option_dict.items():
            print(f" Choice {letter}: {statement}")

        user_answer = get_player_answer()
        if option_dict[user_answer] == wrong_answer:
            print("correct, you have one point")
            player_score += 1
        else:
            print("incorrect")

    end_game(player_score)


def assign_randomised_statements(true_answer, false_answer):
    options = [true_answer, false_answer]
    random.shuffle(options)
    letter_choices = ["a", "b"]
    option_dict = dict(zip(letter_choices, options)) #zip combines the answers with the letter choices
    return option_dict

def get_player_answer():
    answer = input("choose the false statement: ")
    return answer


def end_game(score):
    if score >= 3:
        print("Great job. Go to the next round!")
    else:
        print("AI fooled you. Better luck next time")
#need to add the replay button



