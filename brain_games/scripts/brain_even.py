#!/usr/bin/env python3
from brain_games.cli import welcome_user



def main():
    greeting, name = welcome_user()
    print(greeting)
    print('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()