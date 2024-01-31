def run_game(game_name):
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_name()
        print('Question:', question)
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again")
            return

    print("Congratulations, you've won!")
