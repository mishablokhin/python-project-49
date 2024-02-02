from random import randint


def progression():
    question = ''
    progression_list = []
    progression_start = randint(1, 20)
    progression_difference = randint(1, 10)
    progression_lenght = randint(5, 10)
    for i in range(progression_lenght):
        progression_list.append(progression_start + progression_difference * i)
    hidden_digit_index = randint(0, len(progression_list) - 1)
    hidden_digit = progression_list[hidden_digit_index]
    progression_list[hidden_digit_index] = '..'
    for i in range(0, len(progression_list)):
        question += str(progression_list[i]) + ' '
    correct_answer = str(hidden_digit)
    return question, correct_answer
