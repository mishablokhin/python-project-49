from random import randint


def even_or_not():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct_answer
