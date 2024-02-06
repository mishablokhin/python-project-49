from random import randint
from math import gcd


HELP_TEXT = 'Find the greatest common divisor of given numbers.'


def generate_game_data():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return question, correct_answer
