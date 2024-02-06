#!/usr/bin/env python3
from brain_games.game_control import run_game
from brain_games.games import prime as prime_game
from brain_games.games.prime import HELP_TEXT


def main():
    run_game(prime_game, HELP_TEXT)


if __name__ == '__main__':
    main()
