"""
File : number_guesser.py
Date: 02/28/2023
"""

import sys
from random import randint,seed

if __name__ == '__main__':
    goal = randint(1,100)
    cond = True
    count = 0
    while cond:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > goal:
            print("Your guess is too high.")
        elif guess < goal:
            print("Your guess is too low.")
        elif guess == goal:
            print("You guessed the value ! It took you",count+1,"steps.")
            cond = False
        count += 1
