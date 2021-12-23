#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 15, 2021
# This program allows a user to see if they are
# allowed to date a grandparents grandchild

import time


def main():
    # Asks questions and gets user input
    print("Are you good enough to date my grandchild?")
    print(" ")
    time.sleep(1)
    user_answer_1 = (input("Are you rich? y/n: "))
    print(" ")
    time.sleep(1)
    user_answer_2 = (input("Are you really good looking? y/n: "))
    print(" ")
    time.sleep(1)

    # Evaluates user answers and determines if they are good enough to date.
    if user_answer_1 == "y" and user_answer_2 == "y":
        print("You are rich and good looking, please date my grandchild!")
    elif user_answer_1 == "y":
        print("You are rich, you can date my grandchild.")
    elif user_answer_1 == "y" and user_answer_2 == "n":
        print("You are really good looking, you can date my grandchild.")
    elif user_answer_2 == "y" and user_answer_1 == "n":
        print("You are really good looking, you can date my grandchild.")
    elif user_answer_2 == "n" and user_answer_1 == "n":
        print("You cannot date my grandchild.")
    else:
        print("Invalid input, try again.")


if __name__ == "__main__":
    main()
