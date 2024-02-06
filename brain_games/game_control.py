import prompt


GAME_ROUND_COUNT = 3


def run_game(game_module, help_text):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(help_text)
    for _ in range(GAME_ROUND_COUNT):
        question, correct_answer = game_module.generate_game_data()
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
