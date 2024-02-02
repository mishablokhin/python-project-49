from random import randint
from math import gcd


def greatest_common_divisor():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return question, correct_answer
