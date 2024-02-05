#!/usr/bin/env python3
from brain_games.greeting import greet_user
from brain_games.game_control import run_game
from brain_games.games.calc import calculator


def main():
    greeting, name = greet_user()
    print(greeting)
    print('What is the result of the expression?')
    run_game(calculator, name)


if __name__ == '__main__':
    main()
