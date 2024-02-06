#!/usr/bin/env python3
from brain_games.game_control import run_game
from brain_games.games import progression as progression_game
from brain_games.games.progression import HELP_TEXT


def main():
    run_game(progression_game, HELP_TEXT)


if __name__ == '__main__':
    main()
