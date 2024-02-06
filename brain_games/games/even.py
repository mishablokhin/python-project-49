from random import randint


HELP_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct_answer
