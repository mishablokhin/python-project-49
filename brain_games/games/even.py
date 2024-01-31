from random import randint
from brain_games.check_answer import check_answer


def even_or_not(name):
    correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers < 3:
        question = randint(1, 100)
        print('Question:', question)
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if question % 2 == 0 else 'no'

        if check_answer(correct_answer, user_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again,", name)
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")
