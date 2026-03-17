import json

quiz_dict = [
    {
    "true_statement": "APG III system of flowering plant classification is the third version of a modern, mostly molecular-based system of plant taxonomy being developed by the Angiosperm Phylogeny Group (APG).",
    "false_statement": "Acorus is a genus of dicot flowering plants."
    },

    {
    "true_statement": "APG III system of flowering plant classification is the third version of a modern, mostly molecular-based system of plant taxonomy being developed by the Angiosperm Phylogeny Group (APG).",
    "false_statement": "Acorus is a genus of dicot flowering plants."
    },

    {
    "true_statement": "APG III system of flowering plant classification is the third version of a modern, mostly molecular-based system of plant taxonomy being developed by the Angiosperm Phylogeny Group (APG).",
    "false_statement": "Acorus is a genus of dicot flowering plants."
    },
    {
    "true_statement": "APG III system of flowering plant classification is the third version of a modern, mostly molecular-based system of plant taxonomy being developed by the Angiosperm Phylogeny Group (APG).",
    "false_statement": "Acorus is a genus of dicot flowering plants."
    }

]


def question_answer_pairs():
    print(quiz_dict)

    return quiz_dict




def play_round():
    for i in range(len(quiz_dict)):
        correct_answer = quiz_dict[i]["true_statement"]
        wrong_answer = quiz_dict[i]["false_statement"]
        print(f"Correct answers:{correct_answer}")
        print(f"Wrong answers:{wrong_answer}")

    quiz = question_answer_pairs()
    for item in quiz_dict:
        for key, val in item.items():
            print("Select True or False")
            print(val)


    score = 0
    score_list = []
    user_answer = input("Enter True or False: ")
    for question in quiz_dict:
        if user_answer == correct_answer:
            score += 1

    print(score)

    if score == 3:
        print("Great job. Go to the next round!")
        question_answer_pairs()
    else:
        print("AI fooled you. Better luck next time")
    return score_list




print(play_round())

