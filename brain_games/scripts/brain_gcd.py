#!/usr/bin/env python3
from brain_games.game_control import run_game
from brain_games.games import gcd as gcd_game
from brain_games.games.gcd import HELP_TEXT


def main():
    run_game(gcd_game, HELP_TEXT)


if __name__ == '__main__':
    main()
