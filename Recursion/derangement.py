"""
File : derangement.py
Date : 04/21/2023 
"""


def derangement(n):
    if n == 0:
        return 1
    return n*derangement(n-1)+(-1)**n

if __name__ == '__main__':
    for i in range(20):
        print(i,derangement(i))
