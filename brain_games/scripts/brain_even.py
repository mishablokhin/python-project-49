#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.even import even_or_not


def main():
    greeting, name = welcome_user()
    print(greeting)
    return even_or_not(name)


if __name__ == '__main__':
    main()
