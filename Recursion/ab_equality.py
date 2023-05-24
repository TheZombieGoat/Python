"""
File : ab_equality.py
Date : 04/21/2023
"""

def ab_equal(n, k, current):
        if n == 0:
                if k == 0: #returning if difference is 0 when string is complete.
                        print(current)
                return
        ab_equal(n-1,k-1,current + 'a')
        ab_equal(n-1,k+1,current + 'b')

if __name__ == '__main__':
        length = int(input("What length do you wanna run? "))
        ab_equal(length, 0, "")
