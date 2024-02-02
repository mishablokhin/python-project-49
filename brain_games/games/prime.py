from random import randint


def is_prime():
    question = randint(2, 3571)
    if question in get_primes_up_to_3571():
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def get_primes_up_to_3571():
    limit = 3571
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return primes
