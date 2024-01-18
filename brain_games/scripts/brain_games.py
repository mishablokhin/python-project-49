#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    greeting, _ = welcome_user()
    print(greeting)


if __name__ == '__main__':
    main()
