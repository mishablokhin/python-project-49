#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.game_control import run_game
from brain_games.games.prime import is_prime


def main():
    greeting, name = welcome_user()
    print(greeting)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(is_prime)


if __name__ == '__main__':
    main()
