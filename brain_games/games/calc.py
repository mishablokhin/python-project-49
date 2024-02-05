import random
from random import randint


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b


def calculator():
    operations = ['+', '-', '*']
    a = randint(1, 25)
    b = randint(1, 25)
    operation = random.choice(operations)
    question = f"{a} {operation} {b}"
    correct_answer = str(calculate(a, b, operation))
    return question, correct_answer
