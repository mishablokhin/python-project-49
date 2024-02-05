from random import randint


def is_prime(question):
    if question <= 1:
        return False
    if question <= 3:
        return True
    if question % 2 == 0 or question % 3 == 0:
        return False
    i = 5
    while i * i <= question:
        if question % i == 0 or question % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_question_and_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
