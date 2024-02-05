#!/usr/bin/env python3
from brain_games.greeting import greet_user
from brain_games.game_control import run_game
from brain_games.games.progression import progression


def main():
    greeting, name = greet_user()
    print(greeting)
    print('What number is missing in the progression?')
    run_game(progression, name)


if __name__ == '__main__':
    main()
