from random import randint


def even_or_not(name):
    correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers < 3:
        question = randint(1, 100)
        print('Question:', question)
        user_answer = input('Your answer: ')

        if (question % 2 == 0 and user_answer == 'yes') or \
                (question % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            correct_answers += 1
        else:
            correct_answer = 'yes' if question % 2 == 0 else 'no'
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print("Let's try again,", name)
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")
