#!/usr/bin/env python3
from brain_games.game_control import run_game
from brain_games.games import even as even_game
from brain_games.games.even import HELP_TEXT


def main():
    run_game(even_game, HELP_TEXT)


if __name__ == '__main__':
    main()
