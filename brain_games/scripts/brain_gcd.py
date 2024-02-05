#!/usr/bin/env python3
from brain_games.greeting import greet_user
from brain_games.game_control import run_game
from brain_games.games.gcd import greatest_common_divisor


def main():
    greeting, name = greet_user()
    print(greeting)
    print('Find the greatest common divisor of given numbers.')
    run_game(greatest_common_divisor, name)


if __name__ == '__main__':
    main()
