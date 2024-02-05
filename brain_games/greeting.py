import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greeting = f"Hello, {name}!"
    return greeting, name
