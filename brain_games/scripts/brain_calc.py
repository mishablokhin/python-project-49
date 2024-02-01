#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.game_control import run_game
from brain_games.games.calc import calculator


def main():
    greeting, name = welcome_user()
    print(greeting)
    run_game(calculator)


if __name__ == '__main__':
    main()
