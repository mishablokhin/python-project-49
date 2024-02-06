#!/usr/bin/env python3
from brain_games.game_control import run_game
from brain_games.games import calc as calc_game
from brain_games.games.calc import HELP_TEXT


def main():
    run_game(calc_game, HELP_TEXT)


if __name__ == '__main__':
    main()
