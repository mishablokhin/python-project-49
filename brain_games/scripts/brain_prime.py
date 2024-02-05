#!/usr/bin/env python3
from brain_games.greeting import greet_user
from brain_games.game_control import run_game
from brain_games.games.prime import generate_question_and_answer


def main():
    greeting, name = greet_user()
    print(greeting)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(generate_question_and_answer, name)


if __name__ == '__main__':
    main()
