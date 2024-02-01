import random
from random import randint


def calculator():
    operations_list = ['+', '-', '*']
    a = randint(1, 25)
    b = randint(1, 25)
    operation = random.choice(operations_list)
    question = f"{a} {operation} {b}"
    correct_answer = str(eval(question))
    return question, correct_answer
