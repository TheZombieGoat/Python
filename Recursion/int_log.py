"""
File : int_log.py
Date : 04/21/2023
"""

def int_log(base,number):
        if number <= 1:
                return 0
        return int_log(base,number // base) + 1

if __name__ == '__main__':
        base = int(input("What is the base of the logarithm? "))
        number = int(input("What number are we taking the log of? "))
        print(int_log(base,number))
