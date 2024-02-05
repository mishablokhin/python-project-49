def run_game(game_name, user_name):
    for _ in range(3):
        question, correct_answer = game_name()
        print('Question:', question)
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
