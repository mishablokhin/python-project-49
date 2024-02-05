#!/usr/bin/env python3
from brain_games.greeting import greet_user
from brain_games.game_control import run_game
from brain_games.games.even import even_or_not


def main():
    greeting, name = greet_user()
    print(greeting)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    run_game(even_or_not, name)


if __name__ == '__main__':
    main()
