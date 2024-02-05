from random import randint


def progression():
    progression_start = randint(1, 20)
    progression_difference = randint(1, 10)
    progression_length = randint(5, 10)
    progression_list = list(
        range(
            progression_start,
            progression_start + progression_difference * progression_length,
            progression_difference
        )
    )
    hidden_digit_index = randint(0, progression_length - 1)
    hidden_digit = progression_list[hidden_digit_index]
    progression_list[hidden_digit_index] = '..'

    question = ' '.join(map(str, progression_list))
    correct_answer = str(hidden_digit)

    return question, correct_answer
